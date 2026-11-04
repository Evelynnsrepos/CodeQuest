// Runs Python lessons with Pyodide, off the main thread so a stuck loop can be stopped.
import { loadPyodide } from "/vendor/pyodide/pyodide.mjs";

const HARNESS = `
import io, json, sys, traceback

def _cq_fmt(e):
    te = traceback.TracebackException.from_exception(e)
    te.stack = traceback.StackSummary.from_list([f for f in te.stack if f.filename == "main.py"])
    return "".join(te.format()).strip()

def _cq_no_input(prompt=""):
    raise RuntimeError("input() isn't available in lessons. Set the value in your code instead.")

def _cq_norm(s):
    return "\\n".join(line.rstrip() for line in s.strip().splitlines())

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


def _cq_run(code, check, expected, mode):
    out = io.StringIO()
    ns = {"__name__": "__main__", "input": _cq_no_input}
    old_out, old_err = sys.stdout, sys.stderr
    sys.stdout = sys.stderr = out
    error = None
    try:
        exec(compile(code, "main.py", "exec"), ns)
    except BaseException as e:
        error = _cq_fmt(e)
    finally:
        sys.stdout, sys.stderr = old_out, old_err
    output = out.getvalue()
    result = {"output": output, "error": error}
    if mode != "submit":
        return json.dumps(result)

    passed, message, want = True, "", None
    if error:
        passed, message = False, "Your program stopped with an error."
    elif expected is not None and _cq_norm(output) != _cq_norm(expected):
        passed, message, want = False, "The output doesn't match yet.", expected.strip()
    elif check:
        steps = _cq_steps(check, {"ns": ns, "output": output}, lambda e: "Your code raised an error while being checked:\\n" + "".join(
            traceback.format_exception_only(type(e), e)).strip())
        passed, message = steps["passed"], steps["message"]
        result.update(done=steps["done"], total=steps["total"])
    result.update(passed=passed, message=message)
    if want is not None:
        result["expected"] = want
    return json.dumps(result)
`;

const ready = (async () => {
  const py = await loadPyodide({ indexURL: "/vendor/pyodide/" });
  py.runPython(HARNESS);
  return py;
})();

ready.then(() => self.postMessage({ type: "ready" }),
  (err) => self.postMessage({ type: "failed", error: String(err) }));

self.onmessage = async (event) => {
  const { id, code, check, expected, mode } = event.data;
  try {
    const py = await ready;
    const run = py.globals.get("_cq_run");
    const json = run(code, check ?? undefined, expected ?? undefined, mode); // undefined becomes None; null would not
    run.destroy();
    self.postMessage({ type: "result", id, result: JSON.parse(json) });
  } catch (err) {
    self.postMessage({ type: "result", id, result: { output: "", error: String(err), passed: false } });
  }
};
