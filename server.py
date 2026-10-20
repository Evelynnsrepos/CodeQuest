#!/usr/bin/env python3
"""CodeQuest: a self-hosted, game-style coding course for Python, GDScript, Lua, Rust, Nix and Git.

Run it on your computer, then open it from any browser on your network:

    python3 server.py              # serves on port 8000 to your whole local network
    python3 server.py --pin 4821   # ask for a PIN before anyone can run code
    python3 server.py --local-only # only this computer can open it

Python and Lua lessons run inside the browser (Pyodide, wasmoon). GDScript, Rust, Nix and Git
lessons run on this computer, so Godot 4, Rust, Nix and Git need to be installed here.
Only the Python standard library is required.
"""

import argparse
import datetime as dt
import json
import mimetypes
import os
import re
import shlex
import shutil
import socket
import sqlite3
import subprocess
import sys
import tempfile
import textwrap
import threading
import time
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
    "nix": {"name": "Nix", "ext": "nix", "runs_on": "server"},
    # Git lessons are short scripts of shell-style commands; checks are Python run by this server.
    "git": {"name": "Git", "ext": "sh", "check_ext": "py", "runs_on": "server"},
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
                "check": read_optional(folder / f"check.{LANGUAGES[lang].get('check_ext', ext)}"),
                "setup": read_optional(folder / "setup.sh"),
                "tests": read_optional(folder / "tests.rs"),
            })
        prelude = meta.get("prelude")
        prelude_code = read_optional(course_dir / prelude) if prelude else None
        for lesson in lessons:
            lesson["prelude"] = prelude_code  # server-run languages (Nix) need it next to the lesson
        courses[course_dir.name] = {
            "id": course_dir.name,
            "lang": lang,
            "name": meta.get("name", LANGUAGES[lang]["name"]),
            "icon": meta.get("icon"),
            "blurb": meta.get("blurb"),
            "order": meta.get("order", 100),
            "prelude": prelude_code,
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


def find_nix():
    """nix-instantiate evaluates Nix expressions without building anything."""
    found = shutil.which("nix-instantiate")
    if found:
        return found
    for c in ("/run/current-system/sw/bin/nix-instantiate", "/nix/var/nix/profiles/default/bin/nix-instantiate",
              str(Path.home() / ".nix-profile" / "bin" / "nix-instantiate")):
        if Path(c).is_file():
            return c
    return None


def find_git():
    found = shutil.which("git")
    if found:
        return found
    if os.name == "nt":
        for base in (os.environ.get("ProgramFiles", r"C:\Program Files"),
                     str(Path(os.environ.get("LOCALAPPDATA", "")) / "Programs")):
            c = Path(base) / "Git" / "cmd" / "git.exe"
            if c.is_file():
                return str(c)
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


# On Windows, stop Godot, Rust and Git from flashing a console window for every run.
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


# Nix: the learner's file is evaluated (never built) with nix-instantiate. A lesson's check.nix is a
# function { result, prelude, expect }: [ checks ], where each check is (expect condition "message").
# The checks are tried in order and the first failing message is shown. A course prelude.nix
# can provide practice inputs (a mock nixpkgs) and a `show` function for what Run prints.
NIX_JUDGE = """
let
  result = import ./main.nix;
  prelude = if builtins.pathExists ./prelude.nix then import ./prelude.nix else { };
  expect = cond: msg: if cond then null else msg;
  checks = import ./check.nix { inherit result prelude expect; };
  go = i:
    if i >= builtins.length checks then ""
    else let m = builtins.elemAt checks i; in if m == null then go (i + 1) else m;
in go 0
"""
NIX_SHOW = "(import ./prelude.nix).show (import ./main.nix)\n"


def clean_nix_errors(text, tmp):
    """Keep the last 'error:' and where it happened; drop the trace through CodeQuest's own files."""
    text = text.replace(str(tmp) + os.sep, "").replace(str(tmp), ".")
    lines = [l for l in text.strip().splitlines() if "(stack trace truncated" not in l]
    starts = [i for i, l in enumerate(lines) if l.strip().startswith("error:")]
    if starts:
        lines = lines[starts[-1]:]
    return textwrap.dedent("\n".join(lines)).strip()


NIX_TOKEN_RE = re.compile(r'"(?:[^"\\]|\\.)*"|[{}\[\];=]|[^\s{}\[\];="]+')


def format_nix_value(text, width=60):
    """Lay out nix-instantiate's one-line output over several lines when it's long."""
    tokens = NIX_TOKEN_RE.findall(text)
    pos = 0

    def parse():
        nonlocal pos
        tok = tokens[pos]
        pos += 1
        if tok == "{":
            items = []
            while tokens[pos] != "}":
                key = tokens[pos]
                pos += 2  # key and =
                items.append((key, parse()))
                pos += 1  # ;
            pos += 1
            return ("set", items)
        if tok == "[":
            items = []
            while tokens[pos] != "]":
                items.append(parse())
            pos += 1
            return ("list", items)
        return ("atom", tok)

    def inline(node):
        kind, value = node
        if kind == "atom":
            return value
        if kind == "set":
            return "{ " + "".join(f"{k} = {inline(v)}; " for k, v in value) + "}" if value else "{ }"
        return "[ " + "".join(inline(v) + " " for v in value) + "]" if value else "[ ]"

    def block(node, level, column):
        flat = inline(node)
        kind, value = node
        if kind == "atom" or column + len(flat) <= width:
            return flat
        pad = "  " * (level + 1)
        if kind == "set":
            body = "".join(f"{pad}{k} = {block(v, level + 1, len(pad) + len(k) + 3)};\n" for k, v in value)
            return "{\n" + body + "  " * level + "}"
        body = "".join(f"{pad}{block(v, level + 1, len(pad))}\n" for v in value)
        return "[\n" + body + "  " * level + "]"

    try:
        tree = parse()
        if pos != len(tokens):
            return text
        return block(tree, 0, 0)
    except (IndexError, ValueError):
        return text


def run_nix(lesson, code, mode, nix):
    if not nix:
        return {"ok": False, "output": "", "error":
                "Nix isn't installed on the computer running CodeQuest. Install it from nixos.org/download "
                "(it comes with NixOS), then restart CodeQuest."}
    with tempfile.TemporaryDirectory(prefix="codequest-nix-") as tmp:
        tmp = Path(tmp)
        (tmp / "main.nix").write_text(code, encoding="utf-8")
        if lesson["prelude"]:
            (tmp / "prelude.nix").write_text(lesson["prelude"], encoding="utf-8")
            (tmp / "show.nix").write_text(NIX_SHOW, encoding="utf-8")
        target = "show.nix" if lesson["prelude"] else "main.nix"
        rc, out, err, timed_out = run_process([nix, "--eval", "--strict", target], tmp, RUN_TIMEOUT)
        if timed_out:
            return {"ok": False, "output": "", "error":
                    f"Evaluating took more than {RUN_TIMEOUT} seconds and was stopped. Does something call itself forever?"}
        if rc != 0:
            return {"ok": False, "output": "", "error": clip(clean_nix_errors(err, tmp) or "Nix couldn't evaluate your code.")}
        result = {"ok": True, "output": clip(format_nix_value(out.strip()))}
        if err.strip():
            result["warnings"] = clip(clean_nix_errors(err, tmp))
        if mode != "submit":
            return result

        check_message = None
        if lesson["check"]:
            (tmp / "check.nix").write_text(lesson["check"], encoding="utf-8")
            (tmp / "judge.nix").write_text(NIX_JUDGE, encoding="utf-8")
            rc, out, err, timed_out = run_process([nix, "--eval", "--strict", "--json", "judge.nix"], tmp, RUN_TIMEOUT)
            if timed_out:
                check_message = {"passed": False, "message": "The checks took too long. Does something call itself forever?"}
            elif rc != 0:
                check_message = {"passed": False, "message": "The checks hit an error while using your code:\n\n"
                                 + clip(clean_nix_errors(err, tmp))}
            else:
                message = json.loads(out)
                check_message = {"passed": message == "", "message": message}
        result.update(judge(lesson, result["output"], check_message=check_message, has_check=bool(lesson["check"])))
        return result


# Git: lessons are short scripts, one command per line, run in a fresh practice folder. Only git and a
# few file commands are understood (no real shell), so this works the same on Windows. git's settings
# point at a private config file in the practice folder, so the learner's real git setup is untouched.
GIT_FILE_COMMANDS = ("echo", "cat", "ls", "mkdir", "rm", "cd", "pwd")
GIT_SANDBOX_CONFIG = """[user]
\tname = CodeQuest Learner
\temail = learner@codequest.local
[init]
\tdefaultBranch = main
[advice]
\tdetachedHead = false
[core]
\tautocrlf = false
"""


class GitSandbox:
    def __init__(self, git, root):
        self.git_bin = git
        self.root = root.resolve()
        self.cwd = self.root / "project"
        self.cwd.mkdir()
        home = self.root / "home"
        home.mkdir()
        (home / ".gitconfig").write_text(GIT_SANDBOX_CONFIG, encoding="utf-8")
        self.env = dict(os.environ, HOME=str(home), USERPROFILE=str(home), GIT_CONFIG_GLOBAL=str(home / ".gitconfig"),
                        GIT_CONFIG_NOSYSTEM="1", GIT_TERMINAL_PROMPT="0", GIT_EDITOR="true", GIT_MERGE_AUTOEDIT="no",
                        GIT_PAGER="cat", PAGER="cat", LC_ALL="C", LANG="C", GIT_CEILING_DIRECTORIES=str(self.root))

    def path(self, name):
        target = (self.cwd / name).resolve()
        if target != self.root and self.root not in target.parents:
            raise ValueError(f"{name}: only files inside the practice folder can be used")
        return target

    def git(self, *args, timeout=RUN_TIMEOUT):
        proc = subprocess.run([self.git_bin, *args], cwd=self.cwd, env=self.env, capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=timeout, **NO_WINDOW)
        return proc.returncode, proc.stdout, proc.stderr

    def run_line(self, line, timeout):
        """Run one command; return (output, failed)."""
        try:
            words = shlex.split(line, comments=True)
        except ValueError as exc:
            return f"Couldn't read this line: {exc}", True
        if not words:
            return "", False
        cmd, args = words[0], words[1:]
        if cmd == "git":
            rc, out, err = self.git(*args, timeout=timeout)
            return out + err, rc != 0
        if cmd not in GIT_FILE_COMMANDS:
            return (f"{cmd}: CodeQuest only runs git and these file commands here: "
                    + ", ".join(GIT_FILE_COMMANDS)), True
        try:
            if cmd == "echo":
                redirect = next((i for i, w in enumerate(args) if w in (">", ">>")), None)
                if redirect is None:
                    return " ".join(args) + "\n", False
                if redirect != len(args) - 2:
                    return "echo: put the file name right after > or >>", True
                text = " ".join(args[:redirect]) + "\n"
                with open(self.path(args[-1]), "a" if args[redirect] == ">>" else "w", encoding="utf-8", newline="\n") as f:
                    f.write(text)
                return "", False
            if cmd == "cat":
                return "".join(self.path(a).read_text(encoding="utf-8") for a in args), False
            if cmd == "ls":
                folder = self.path(args[0]) if args else self.cwd
                return "".join(p.name + ("/" if p.is_dir() else "") + "\n"
                               for p in sorted(folder.iterdir()) if p.name != ".git"), False
            if cmd == "mkdir":
                for a in args:
                    if a != "-p":
                        self.path(a).mkdir(parents=True, exist_ok=True)
                return "", False
            if cmd == "rm":
                for a in args:
                    if not a.startswith("-"):
                        target = self.path(a)
                        shutil.rmtree(target) if target.is_dir() else target.unlink()
                return "", False
            if cmd == "cd":
                target = self.path(args[0]) if args else self.root / "project"
                if not target.is_dir():
                    return f"cd: {args[0]}: no such folder", True
                self.cwd = target
                return "", False
            if cmd == "pwd":
                return "/" + self.cwd.relative_to(self.root).as_posix() + "\n", False
        except (OSError, ValueError, IndexError) as exc:
            return f"{cmd}: {exc.strerror if isinstance(exc, OSError) and exc.strerror else exc}", True
        return "", False

    def run_script(self, script, deadline, echo=True):
        """Run every line like a terminal would; return (transcript, error)."""
        transcript = []
        for raw in script.splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            left = deadline - time.monotonic()
            if left <= 0:
                raise subprocess.TimeoutExpired(line, RUN_TIMEOUT)
            out, failed = self.run_line(line, left)
            if failed and not line.startswith("git "):
                # A git command that fails is normal (a merge conflict, say), but anything else stops the run.
                transcript.append(f"$ {line}\n")
                return "".join(transcript), out.strip()
            if echo:
                transcript.append(f"$ {line}\n{out}")
        return "".join(transcript), ""


def run_git(lesson, code, mode, git):
    if not git:
        return {"ok": False, "output": "", "error":
                "Git isn't installed on the computer running CodeQuest. Install it from git-scm.com "
                "(on NixOS add pkgs.git to your packages), then restart CodeQuest."}
    with tempfile.TemporaryDirectory(prefix="codequest-git-") as tmp:
        box = GitSandbox(git, Path(tmp))
        deadline = time.monotonic() + RUN_TIMEOUT
        try:
            if lesson["setup"]:
                _, setup_error = box.run_script(lesson["setup"], deadline, echo=False)
                if setup_error:
                    return {"ok": False, "output": "", "error": "This lesson's setup failed: " + setup_error}
                box.cwd = box.root / "project"
            transcript, error = box.run_script(code, deadline)
        except subprocess.TimeoutExpired:
            return {"ok": False, "output": "", "error":
                    f"Your commands ran for more than {RUN_TIMEOUT} seconds and were stopped. Is one waiting for input?"}
        result = {"ok": not error, "output": clip(transcript.rstrip())}
        if error:
            result["error"] = error
        if mode != "submit":
            return result

        check_message = None
        if lesson["check"]:
            box.cwd = box.root / "project"

            def run_git_check(*args):
                return box.git(*args)[1].strip()  # stdout only, so failures read as ""

            def read(name):
                return box.path(name).read_text(encoding="utf-8")

            scope = {"git": run_git_check, "read": read, "exists": lambda name: box.path(name).exists(),
                     "output": transcript}
            try:
                exec(compile(lesson["check"], "check.py", "exec"), scope)
                check_message = {"passed": True, "message": ""}
            except AssertionError as exc:
                check_message = {"passed": False, "message": str(exc) or "Not quite yet."}
            except Exception as exc:  # a broken check, or the repo is in a state the check didn't expect
                check_message = {"passed": False, "message": f"The check couldn't read your repository ({exc})."}
        result.update(judge(lesson, transcript, check_message=check_message, has_check=bool(lesson["check"]),
                            runtime_error=error))
        return result


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
    nix = None
    git = None
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
                "nix": bool(self.nix),
                "git": bool(self.git),
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
            elif lang == "nix":
                result = run_nix(lesson, code, mode, self.nix)
            elif lang == "git":
                result = run_git(lesson, code, mode, self.git)
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

    def host_tool(self, lang):
        return {"gdscript": self.godot, "rust": self.rustc, "nix": self.nix, "git": self.git}.get(lang)

    def courses_payload(self):
        progress = progress_map()
        courses = []
        for course in load_courses().values():
            lang = course["lang"]
            info = LANGUAGES[lang]
            available = info["runs_on"] == "browser" or bool(self.host_tool(lang))
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
    Handler.nix = find_nix()
    Handler.git = find_git()
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
    print(f"  Nix:      {'found at ' + Handler.nix if Handler.nix else 'not found (install from nixos.org/download)'}")
    print(f"  Git:      {'found at ' + Handler.git if Handler.git else 'not found (install from git-scm.com)'}")
    print("\n  Press Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
