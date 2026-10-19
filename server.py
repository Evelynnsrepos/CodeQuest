#!/usr/bin/env python3
"""CodeQuest: a self-hosted, game-style coding course for Python, GDScript, Lua and Rust.

Run it on your computer, then open it from any browser on your network:

    python3 server.py              # serves on port 8000 to your whole local network
    python3 server.py --pin 4821   # ask for a PIN before anyone can run code
    python3 server.py --local-only # only this computer can open it

Python and Lua lessons run inside the browser (Pyodide, wasmoon). GDScript and Rust lessons are
compiled and run on this computer, so Godot 4 and Rust need to be installed here.
Only the Python standard library is required.
"""

import argparse
import datetime as dt
import json
import mimetypes
import os
import re
import shutil
import socket
import sqlite3
import subprocess
import sys
import tempfile
import threading
import webbrowser
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent
LESSONS_DIR = ROOT / "lessons"
STATIC_DIR = ROOT / "static"
VENDOR_DIR = ROOT / "vendor"
RUNNERS_DIR = ROOT / "runners"
DATA_DIR = ROOT / "data"

LANGUAGES = {
    "python": {"name": "Python", "ext": "py", "runs_on": "browser"},
    "gdscript": {"name": "GDScript", "ext": "gd", "runs_on": "server"},
    "lua": {"name": "Lua", "ext": "lua", "runs_on": "browser"},
    "rust": {"name": "Rust", "ext": "rs", "runs_on": "server"},
}

RUN_TIMEOUT = 10  # seconds a learner program may run
COMPILE_TIMEOUT = 60  # seconds rustc may take
MAX_OUTPUT = 20_000  # characters of output sent back to the page
MAX_CODE = 100_000  # characters of code accepted from the page

mimetypes.add_type("application/wasm", ".wasm")
mimetypes.add_type("text/javascript", ".mjs")
mimetypes.add_type("text/javascript", ".js")
mimetypes.add_type("application/manifest+json", ".webmanifest")
mimetypes.add_type("image/svg+xml", ".svg")


# ---------------------------------------------------------------- lessons ---

def parse_front_matter(text):
    """Split '---\\nkey: value\\n---\\nbody' into (dict, body)."""
    meta = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            for line in text[3:end].strip().splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    meta[key.strip()] = value.strip()
            text = text[end + 4:].lstrip("\n")
    return meta, text


def read_optional(path):
    return path.read_text(encoding="utf-8") if path.exists() else None


def load_courses():
    """Return {course_id: course}. Each folder in lessons/ is a course.

    A course's optional course.json sets its language (default: the folder name),
    name, icon, blurb, display order and an optional hidden prelude file that runs
    before the learner's code (used to provide practice APIs).
    """
    courses = {}
    if not LESSONS_DIR.is_dir():
        return courses
    for course_dir in LESSONS_DIR.iterdir():
        if not course_dir.is_dir():
            continue
        meta_file = course_dir / "course.json"
        meta = json.loads(meta_file.read_text(encoding="utf-8")) if meta_file.exists() else {}
        lang = meta.get("lang", course_dir.name)
        if lang not in LANGUAGES:
            continue
        ext = LANGUAGES[lang]["ext"]
        lessons = []
        for folder in sorted(p for p in course_dir.iterdir() if p.is_dir()):
            lesson_md = folder / "lesson.md"
            if not lesson_md.exists():
                continue
            front, body = parse_front_matter(lesson_md.read_text(encoding="utf-8"))
            lessons.append({
                "course": course_dir.name,
                "lang": lang,
                "slug": folder.name,
                "title": front.get("title", folder.name),
                "xp": int(front.get("xp", 10)),
                "body": body,
                "starter": read_optional(folder / f"starter.{ext}") or "",
                "solution": read_optional(folder / f"solution.{ext}"),
                "expected_output": read_optional(folder / "expected_output.txt"),
                "check": read_optional(folder / f"check.{ext}"),
                "tests": read_optional(folder / "tests.rs"),
            })
        prelude = meta.get("prelude")
        courses[course_dir.name] = {
            "id": course_dir.name,
            "lang": lang,
            "name": meta.get("name", LANGUAGES[lang]["name"]),
            "icon": meta.get("icon"),
            "blurb": meta.get("blurb"),
            "order": meta.get("order", 100),
            "prelude": read_optional(course_dir / prelude) if prelude else None,
            "lessons": lessons,
        }
    return dict(sorted(courses.items(), key=lambda kv: (kv[1]["order"], kv[0])))


def find_lesson(course_id, slug):
    course = load_courses().get(course_id)
    for lesson in (course["lessons"] if course else []):
        if lesson["slug"] == slug:
            return lesson
    return None


# --------------------------------------------------------------- progress ---

DB_LOCK = threading.Lock()


def db():
    DATA_DIR.mkdir(exist_ok=True)
    conn = sqlite3.connect(DATA_DIR / "progress.db")
    conn.row_factory = sqlite3.Row
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS progress (
            lang TEXT NOT NULL,
            slug TEXT NOT NULL,
            code TEXT,
            attempts INTEGER NOT NULL DEFAULT 0,
            completed_at TEXT,
            PRIMARY KEY (lang, slug)
        );
        CREATE TABLE IF NOT EXISTS profile (
            key TEXT PRIMARY KEY,
            value TEXT
        );
        """
    )
    return conn


def get_profile(conn):
    values = {row["key"]: row["value"] for row in conn.execute("SELECT key, value FROM profile")}
    xp = int(values.get("xp", 0))
    streak = int(values.get("streak", 0))
    last_day = values.get("last_day")
    # A streak only counts if you practised today or yesterday.
    if last_day:
        gap = (dt.date.today() - dt.date.fromisoformat(last_day)).days
        if gap > 1:
            streak = 0
    level, into, needed = level_for(xp)
    completed = conn.execute("SELECT COUNT(*) FROM progress WHERE completed_at IS NOT NULL").fetchone()[0]
    return {
        "xp": xp,
        "level": level,
        "level_xp": into,
        "level_needed": needed,
        "streak": streak,
        "practised_today": last_day == dt.date.today().isoformat(),
        "completed": completed,
    }


def level_for(xp):
    """Each level costs 50 XP more than the one before: 50, 100, 150, ..."""
    level, floor, step = 1, 0, 50
    while xp >= floor + step:
        floor += step
        level += 1
        step += 50
    return level, xp - floor, step


def set_profile(conn, **values):
    for key, value in values.items():
        conn.execute(
            "INSERT INTO profile (key, value) VALUES (?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value = excluded.value",
            (key, str(value)),
        )


def record_attempt(lang, slug, code, passed, lesson_xp):
    """Save code and, on a first pass, award XP and extend the streak."""
    with DB_LOCK:
        conn = db()
        row = conn.execute("SELECT completed_at FROM progress WHERE lang=? AND slug=?", (lang, slug)).fetchone()
        already_done = bool(row and row["completed_at"])
        conn.execute(
            "INSERT INTO progress (lang, slug, code, attempts) VALUES (?, ?, ?, 1) "
            "ON CONFLICT(lang, slug) DO UPDATE SET code = excluded.code, attempts = attempts + 1",
            (lang, slug, code),
        )
        gained = 0
        if passed and not already_done:
            gained = lesson_xp
            now = dt.datetime.now().isoformat(timespec="seconds")
            conn.execute("UPDATE progress SET completed_at=? WHERE lang=? AND slug=?", (now, lang, slug))
            profile = get_profile(conn)
            today = dt.date.today()
            values = {row["key"]: row["value"] for row in conn.execute("SELECT key, value FROM profile")}
            last_day = values.get("last_day")
            streak = profile["streak"]
            if last_day != today.isoformat():
                streak = streak + 1 if last_day == (today - dt.timedelta(days=1)).isoformat() else 1
            set_profile(conn, xp=profile["xp"] + gained, streak=streak, last_day=today.isoformat())
        conn.commit()
        profile = get_profile(conn)
        conn.close()
    return gained, profile


def save_draft(lang, slug, code):
    with DB_LOCK:
        conn = db()
        conn.execute(
            "INSERT INTO progress (lang, slug, code) VALUES (?, ?, ?) "
            "ON CONFLICT(lang, slug) DO UPDATE SET code = excluded.code",
            (lang, slug, code),
        )
        conn.commit()
        conn.close()


def progress_map():
    conn = db()
    rows = conn.execute("SELECT lang, slug, code, completed_at FROM progress").fetchall()
    conn.close()
    return {(r["lang"], r["slug"]): dict(r) for r in rows}


# ---------------------------------------------------------------- runners ---

def find_godot(explicit=None):
    candidates = [explicit, os.environ.get("GODOT_BIN")]
    candidates += [shutil.which(n) for n in ("godot", "godot4", "Godot", "godot-mono")]
    tools = ROOT / "tools"
    if tools.is_dir():
        found = sorted(p for p in tools.rglob("*") if p.name.lower().startswith("godot") and p.is_file()
                       and (os.name != "nt" or p.suffix.lower() == ".exe"))
        # On Windows only the *_console.exe build reports output, so try it first.
        found.sort(key=lambda p: "console" not in p.name.lower())
        candidates += [str(p) for p in found]
    for c in candidates:
        if c and Path(c).is_file() and os.access(c, os.X_OK):
            return c
    return None


def find_rustc():
    found = shutil.which("rustc")
    if found:
        return found
    cargo_bin = Path.home() / ".cargo" / "bin" / ("rustc.exe" if os.name == "nt" else "rustc")
    return str(cargo_bin) if cargo_bin.exists() else None


def clip(text):
    text = text or ""
    if len(text) > MAX_OUTPUT:
        return text[:MAX_OUTPUT] + "\n... (output cut short)"
    return text


# On Windows, stop Godot and Rust from flashing a console window for every run.
NO_WINDOW = {"creationflags": 0x08000000} if os.name == "nt" else {}


def run_process(cmd, cwd, timeout):
    env = dict(os.environ, RUST_BACKTRACE="0")
    try:
        proc = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout,
            encoding="utf-8", errors="replace", env=env, **NO_WINDOW,
        )
        return proc.returncode, proc.stdout, proc.stderr, False
    except subprocess.TimeoutExpired as exc:
        out = exc.stdout.decode("utf-8", "replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        return None, out, "", True


def outputs_match(actual, expected):
    norm = lambda s: "\n".join(line.rstrip() for line in s.strip().splitlines())
    return norm(actual) == norm(expected)


GD_ERROR_RE = re.compile(r"gdscript://[^:]*\.gd:(\d+)")


def clean_godot_errors(stderr_text, stdout_text):
    """Turn Godot's error dump into short 'Line N: message' lines."""
    lines = (stdout_text + "\n" + stderr_text).splitlines()
    messages = []
    for i, line in enumerate(lines):
        if line.startswith(("SCRIPT ERROR:", "ERROR:")) and "runner.gd" not in line:
            message = line.split(":", 1)[1].strip()
            line_no = None
            for follow in lines[i + 1:i + 3]:
                m = GD_ERROR_RE.search(follow)
                if m:
                    line_no = m.group(1)
                    break
            if "Failed to load script" in message or "reload" in message.lower() and not line_no:
                continue
            messages.append(f"Line {line_no}: {message}" if line_no else message)
    seen = []
    for m in messages:
        if m not in seen:
            seen.append(m)
    return "\n".join(seen)


def run_gdscript(lesson, code, mode, godot):
    if not godot:
        return {"ok": False, "output": "", "error":
                "Godot isn't set up on the computer running CodeQuest. Download Godot 4, put it in "
                "CodeQuest's tools folder (on Windows, use the _console.exe file) and restart CodeQuest."}
    with tempfile.TemporaryDirectory(prefix="codequest-gd-") as tmp:
        tmp = Path(tmp)
        shutil.copy(RUNNERS_DIR / "runner.gd", tmp / "runner.gd")
        (tmp / "user.gd").write_text(code, encoding="utf-8")
        check = lesson["check"] if mode == "submit" else None
        if check:
            (tmp / "check.gd").write_text(check, encoding="utf-8")
        cmd = [godot, "--headless", "--no-header", "--log-file", str(tmp / "godot.log"),
               "--script", "runner.gd", "--", "user.gd"] + (["check.gd"] if check else [])
        code_rc, out, err, timed_out = run_process(cmd, tmp, RUN_TIMEOUT)

    if timed_out:
        return {"ok": False, "output": clip(extract_between(out)), "error":
                f"Your program ran for more than {RUN_TIMEOUT} seconds and was stopped. Is there a loop that never ends?"}
    program_output = extract_between(out)
    if "__CQ_COMPILE_ERROR__" in out:
        return {"ok": False, "output": "", "error": clean_godot_errors(err, out) or "Your script has an error."}
    runtime_errors = clean_godot_errors(err, out)
    result = {"ok": not runtime_errors, "output": clip(program_output)}
    if runtime_errors:
        result["error"] = runtime_errors
    if mode == "submit":
        result.update(judge(lesson, program_output, check_message=extract_check(out), has_check=bool(check),
                            runtime_error=runtime_errors))
    return result


def extract_between(out):
    if "__CQ_BEGIN__" not in out:
        return ""
    body = out.split("__CQ_BEGIN__", 1)[1]
    body = body.split("__CQ_END__", 1)[0]
    return body.lstrip("\n")


def extract_check(out):
    m = re.search(r"__CQ_CHECK__ (.*)", out)
    if not m:
        return None
    return json.loads(m.group(1))


def run_rust(lesson, code, mode, rustc):
    if not rustc:
        return {"ok": False, "output": "", "error":
                "Rust isn't installed on the computer running CodeQuest. Install it from rustup.rs, then restart the server."}
    exe = "main.exe" if os.name == "nt" else "main"
    with tempfile.TemporaryDirectory(prefix="codequest-rs-") as tmp:
        tmp = Path(tmp)
        (tmp / "main.rs").write_text(code, encoding="utf-8")
        rc, out, err, timed_out = run_process(
            [rustc, "--edition", "2021", "--color", "never", "-o", exe, "main.rs"], tmp, COMPILE_TIMEOUT)
        if timed_out or rc != 0:
            return {"ok": False, "output": "", "error": clip(err.strip() or "Compiling took too long.")}
        warnings = err.strip()
        rc, out, err, timed_out = run_process([str(tmp / exe)], tmp, RUN_TIMEOUT)
        if timed_out:
            return {"ok": False, "output": clip(out), "error":
                    f"Your program ran for more than {RUN_TIMEOUT} seconds and was stopped. Is there a loop that never ends?"}
        program_output = out
        runtime_error = err.strip() if rc != 0 else ""
        result = {"ok": rc == 0, "output": clip(program_output)}
        if runtime_error:
            result["error"] = clip(runtime_error)
        if warnings:
            result["warnings"] = clip(warnings)
        if mode != "submit":
            return result

        check_message = None
        if lesson["tests"]:
            test_src = (code + "\n\n#[cfg(test)]\nmod codequest_tests {\n    #[allow(unused_imports)]\n    use super::*;\n\n"
                        + lesson["tests"] + "\n}\n")
            (tmp / "tests.rs").write_text(test_src, encoding="utf-8")
            test_exe = "tests.exe" if os.name == "nt" else "tests"
            rc, out, err, timed_out = run_process(
                [rustc, "--edition", "2021", "--color", "never", "--test", "-A", "warnings", "-o", test_exe, "tests.rs"],
                tmp, COMPILE_TIMEOUT)
            if timed_out or rc != 0:
                check_message = {"passed": False, "message": "The checks couldn't compile against your code. "
                                 "Did you keep the function names and types from the lesson?\n\n" + clip(err.strip())}
            else:
                rc, out, err, timed_out = run_process([str(tmp / test_exe), "--test-threads", "1"], tmp, RUN_TIMEOUT)
                if timed_out:
                    check_message = {"passed": False, "message": "The checks took too long. Is there a loop that never ends?"}
                elif rc != 0:
                    check_message = {"passed": False, "message": summarize_rust_tests(out)}
                else:
                    check_message = {"passed": True, "message": ""}
        result.update(judge(lesson, program_output, check_message=check_message, has_check=bool(lesson["tests"]),
                            runtime_error=runtime_error))
        return result


def summarize_rust_tests(out):
    panics = re.findall(r"panicked at [^\n]*\n(.*)", out)
    failed = re.findall(r"^test codequest_tests::(\w+) \.\.\. FAILED", out, re.M)
    lines = []
    for name, panic in zip(failed, panics + [""] * len(failed)):
        lines.append(f"{name.replace('_', ' ')}: {panic.strip()}" if panic else name.replace("_", " "))
    return "\n".join(lines) or out[-2000:]


def judge(lesson, program_output, check_message, has_check, runtime_error=""):
    """Combine expected-output and check results into a pass/fail with a message."""
    if runtime_error:
        return {"passed": False, "message": "Your program stopped with an error."}
    if lesson["expected_output"] is not None and not outputs_match(program_output, lesson["expected_output"]):
        return {"passed": False, "message": "The output doesn't match yet.",
                "expected": lesson["expected_output"].strip()}
    if has_check:
        if not check_message:
            return {"passed": False, "message": "The checks didn't finish. Look for an error above."}
        if not check_message.get("passed"):
            return {"passed": False, "message": check_message.get("message") or "Not quite yet."}
    return {"passed": True, "message": ""}


# -------------------------------------------------------------- HTTP layer ---

class Handler(BaseHTTPRequestHandler):
    server_version = "CodeQuest/1.0"
    pin = None
    godot = None
    rustc = None
    port = 8000

    def log_message(self, fmt, *args):
        if os.environ.get("CODEQUEST_LOG"):
            super().log_message(fmt, *args)

    # -- helpers
    def send_json(self, payload, status=HTTPStatus.OK):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def read_json(self):
        length = int(self.headers.get("Content-Length") or 0)
        if length > MAX_CODE * 2:
            raise ValueError("Request too large")
        return json.loads(self.rfile.read(length) or b"{}")

    def authorized(self):
        return not self.pin or self.headers.get("X-CodeQuest-Pin") == self.pin

    def send_file(self, path):
        if not path.is_file():
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        ctype = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
        data = path.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        # Vendor files never change between releases; let phones cache them.
        self.send_header("Cache-Control", "public, max-age=604800" if VENDOR_DIR in path.parents else "no-cache")
        self.end_headers()
        self.wfile.write(data)

    def safe_join(self, base, rel):
        target = (base / rel).resolve()
        return target if base.resolve() in target.parents or target == base.resolve() else None

    # -- routes
    def do_GET(self):
        path = unquote(urlparse(self.path).path)
        if path in ("/", "/index.html") or path.startswith("/learn/"):
            return self.send_file(STATIC_DIR / "index.html")
        if path.startswith("/static/"):
            target = self.safe_join(STATIC_DIR, path[len("/static/"):])
            return self.send_file(target) if target else self.send_error(HTTPStatus.NOT_FOUND)
        if path.startswith("/vendor/"):
            target = self.safe_join(VENDOR_DIR, path[len("/vendor/"):])
            return self.send_file(target) if target else self.send_error(HTTPStatus.NOT_FOUND)
        if path == "/api/info":
            return self.send_json({
                "app": "codequest",
                "pin_required": bool(self.pin),
                "urls": lan_urls(self.port),
                "godot": bool(self.godot),
                "rust": bool(self.rustc),
            })
        if not path.startswith("/api/"):
            return self.send_error(HTTPStatus.NOT_FOUND)
        if not self.authorized():
            return self.send_json({"error": "pin"}, HTTPStatus.UNAUTHORIZED)

        if path == "/api/courses":
            return self.send_json(self.courses_payload())
        m = re.fullmatch(r"/api/lesson/([\w-]+)/([\w-]+)", path)
        if m:
            return self.lesson_payload(*m.groups())
        self.send_error(HTTPStatus.NOT_FOUND)

    def do_POST(self):
        path = urlparse(self.path).path
        if not self.authorized():
            return self.send_json({"error": "pin"}, HTTPStatus.UNAUTHORIZED)
        try:
            data = self.read_json()
        except ValueError as exc:
            return self.send_json({"error": str(exc)}, HTTPStatus.BAD_REQUEST)
        course, slug, code = data.get("course"), data.get("slug"), data.get("code", "")
        if not isinstance(code, str) or len(code) > MAX_CODE:
            return self.send_json({"error": "Code is too long"}, HTTPStatus.BAD_REQUEST)
        lesson = find_lesson(course, slug) if isinstance(course, str) else None
        if not lesson:
            return self.send_json({"error": "No such lesson"}, HTTPStatus.NOT_FOUND)
        lang = lesson["lang"]

        if path == "/api/save":
            save_draft(course, slug, code)
            return self.send_json({"saved": True})

        if path == "/api/run":
            mode = "submit" if data.get("mode") == "submit" else "run"
            if lang == "gdscript":
                result = run_gdscript(lesson, code, mode, self.godot)
            elif lang == "rust":
                result = run_rust(lesson, code, mode, self.rustc)
            else:
                return self.send_json({"error": "This language runs in the browser"}, HTTPStatus.BAD_REQUEST)
            if mode == "submit":
                if "passed" not in result:
                    result.update(passed=False, message="Fix the error below first.")
                gained, profile = record_attempt(course, slug, code, result.get("passed", False), lesson["xp"])
                result.update(gained=gained, profile=profile)
            return self.send_json(result)

        if path == "/api/complete":
            # Python and Lua lessons are checked in the browser and report back here.
            gained, profile = record_attempt(course, slug, code, bool(data.get("passed")), lesson["xp"])
            return self.send_json({"gained": gained, "profile": profile})

        self.send_error(HTTPStatus.NOT_FOUND)

    def courses_payload(self):
        progress = progress_map()
        courses = []
        for course in load_courses().values():
            lang = course["lang"]
            info = LANGUAGES[lang]
            available = info["runs_on"] == "browser" or bool(self.godot if lang == "gdscript" else self.rustc)
            courses.append({
                "id": course["id"],
                "lang": lang,
                "name": course["name"],
                "icon": course["icon"],
                "blurb": course["blurb"],
                "runs_on": info["runs_on"],
                "available": available,
                "lessons": [{
                    "slug": l["slug"], "title": l["title"], "xp": l["xp"],
                    "completed": bool(progress.get((course["id"], l["slug"]), {}).get("completed_at")),
                } for l in course["lessons"]],
            })
        conn = db()
        profile = get_profile(conn)
        conn.close()
        return {"courses": courses, "profile": profile}

    def lesson_payload(self, course_id, slug):
        course = load_courses().get(course_id)
        lesson = find_lesson(course_id, slug)
        if not lesson:
            return self.send_json({"error": "No such lesson"}, HTTPStatus.NOT_FOUND)
        saved = progress_map().get((course_id, slug), {})
        lessons = course["lessons"]
        index = next(i for i, l in enumerate(lessons) if l["slug"] == slug)
        payload = {
            "course": course_id,
            "course_name": course["name"],
            "lang": lesson["lang"],
            "slug": slug,
            "title": lesson["title"],
            "xp": lesson["xp"],
            "body": lesson["body"],
            "starter": lesson["starter"],
            "code": saved.get("code") or lesson["starter"],
            "completed": bool(saved.get("completed_at")),
            "solution": lesson["solution"] if saved.get("completed_at") else None,
            "has_solution": lesson["solution"] is not None,
            "index": index + 1,
            "total": len(lessons),
            "next": lessons[index + 1]["slug"] if index + 1 < len(lessons) else None,
            "prev": lessons[index - 1]["slug"] if index > 0 else None,
        }
        if LANGUAGES[lesson["lang"]]["runs_on"] == "browser":
            payload["expected_output"] = lesson["expected_output"]
            payload["check"] = lesson["check"]
            payload["prelude"] = course["prelude"]
        return self.send_json(payload)


def lan_urls(port):
    """Best guess at the addresses other devices on the network can use."""
    addresses = set()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("10.255.255.255", 1))  # no packet is sent; this just picks the outgoing interface
            addresses.add(s.getsockname()[0])
    except OSError:
        pass
    try:
        for info in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET):
            addresses.add(info[4][0])
    except OSError:
        pass
    addresses = sorted(a for a in addresses if not a.startswith("127."))
    return [f"http://{a}:{port}" for a in addresses]


def main():
    parser = argparse.ArgumentParser(description="Run CodeQuest on your local network.")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--local-only", action="store_true", help="only allow this computer to connect")
    parser.add_argument("--pin", help="require this PIN before any code can run (recommended on shared Wi-Fi)")
    parser.add_argument("--godot", help="path to the Godot 4 executable")
    parser.add_argument("--open", action="store_true", help="open CodeQuest in your browser once it's running")
    args = parser.parse_args()

    host = "127.0.0.1" if args.local_only else "0.0.0.0"
    Handler.pin = args.pin
    Handler.godot = find_godot(args.godot)
    Handler.rustc = find_rustc()
    Handler.port = args.port

    if not (VENDOR_DIR / "pyodide" / "pyodide.js").exists():
        print("Warning: vendor/pyodide is missing, so Python lessons won't run.", file=sys.stderr)

    local_url = f"http://localhost:{args.port}"
    try:
        server = ThreadingHTTPServer((host, args.port), Handler)
    except OSError as exc:
        print(f"\n  Port {args.port} is already in use ({exc.strerror}).")
        print(f"  If CodeQuest is already running, open {local_url}")
        print("  Otherwise pick another port with --port 9000.\n")
        if args.open:
            webbrowser.open(local_url)
        sys.exit(1)
    if args.open:
        threading.Timer(0.5, webbrowser.open, [local_url]).start()
    print("\n  CodeQuest is running.\n")
    print(f"  On this computer:   {local_url}")
    if not args.local_only:
        for url in lan_urls(args.port):
            print(f"  On your phone/tablet (same Wi-Fi): {url}")
        if not args.pin:
            print("\n  Anyone on this network can run code here. Add --pin 1234 to require a PIN.")
    print(f"\n  Python:   runs in the browser")
    print(f"  Lua:      runs in the browser")
    print(f"  GDScript: {'Godot found at ' + Handler.godot if Handler.godot else 'Godot not found (use --godot PATH)'}")
    print(f"  Rust:     {'rustc found at ' + Handler.rustc if Handler.rustc else 'rustc not found (install from rustup.rs)'}")
    print("\n  Press Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
