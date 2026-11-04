"""Runs a learner's Python file with the computer's own Python, then (optionally) the lesson's check.

Usage: python pyhost_runner.py main.py [check.py]
The check gets `ns` (the learner's globals) and `output` (what they printed), like browser Python lessons.
"""
import contextlib
import io
import json
import sys
import traceback

MARK = "\x1eCODEQUEST-CHECK "


class Tee(io.TextIOBase):
    def __init__(self, buf):
        self.buf = buf

    def write(self, s):
        self.buf.write(s)
        sys.__stdout__.write(s)
        return len(s)

    def flush(self):
        sys.__stdout__.flush()


def _cq_steps(check, scope, crash):
    """Run a check one top-level statement at a time. Each statement holding an assert is one "part";
    a failing part is noted and the rest still run, so the learner sees how many parts already pass."""
    import ast
    tree = ast.parse(check, "check.py")
    parts = [any(isinstance(n, ast.Assert) for n in ast.walk(node)) for node in tree.body]
    done, message = 0, None
    for node, is_part in zip(tree.body, parts):
        try:
            exec(compile(ast.Module([node], []), "check.py", "exec"), scope)
            done += is_part
        except AssertionError as e:
            message = message or str(e) or "Not quite yet."
        except Exception as e:
            message = message or crash(e)
            if not is_part:
                break  # setup for later parts failed, so they can't run
    return {"passed": message is None, "message": message or "", "done": done, "total": sum(parts)}


def short_traceback(exc):
    frames = [f for f in traceback.extract_tb(exc.__traceback__) if f.filename == "main.py"]
    text = "Traceback (most recent call last):\n" + "".join(traceback.format_list(frames)) if frames else ""
    text += "".join(traceback.format_exception_only(type(exc), exc))
    if isinstance(exc, ModuleNotFoundError):
        text += ("\nThis lesson needs a package that isn't installed in CodeQuest's AI Python yet. "
                 "Run setup-ai.bat (Windows) or ./setup-ai.sh (Linux, NixOS) in your CodeQuest folder, "
                 "see AI engineer 1, lesson 01, and run this again.\n")
    return text


def main():
    user_path = sys.argv[1]
    check_path = sys.argv[2] if len(sys.argv) > 2 else None
    with open(user_path, encoding="utf-8") as f:
        code = f.read()
    ns = {"__name__": "__main__"}
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(Tee(buf)):
            exec(compile(code, "main.py", "exec"), ns)
    except SystemExit:
        pass
    except BaseException as exc:  # show the learner their own error, not this runner's frames
        sys.stderr.write(short_traceback(exc))
        sys.exit(1)
    if not check_path:
        return
    with open(check_path, encoding="utf-8") as f:
        check = f.read()
    result = _cq_steps(check, {"ns": ns, "output": buf.getvalue()},
                       lambda exc: f"The check hit an error while using your code: {type(exc).__name__}: {exc}")
    sys.__stdout__.write("\n" + MARK + json.dumps(result) + "\n")


if __name__ == "__main__":
    main()
