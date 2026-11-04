import json, logging
from fastapi.testclient import TestClient
app, JF, log = ns.get("app"), ns.get("JsonFormatter"), ns.get("log")
assert app is not None and JF and log, "Keep app, JsonFormatter and log."
rec = logging.LogRecord("x", logging.WARNING, "f", 1, "hello %s", ("you",), None)
assert json.loads(JF().format(rec)) == {"level": "WARNING", "msg": "hello you"}, "format: level and msg (use getMessage())."
rec.extra_fields = {"a": 1}
assert json.loads(JF().format(rec)) == {"level": "WARNING", "msg": "hello you", "a": 1}, "Include extra_fields."
lines = []
class Grab(logging.Handler):
    def emit(self, record):
        lines.append(JF().format(record))
g = Grab(); log.addHandler(g)
try:
    r = TestClient(app).get("/hello?x=1")
    r404 = TestClient(app).get("/nope")
finally:
    log.removeHandler(g)
rid = r.headers.get("X-Request-ID")
assert rid and len(rid) == 32, "Send the request id back in the X-Request-ID header (uuid4().hex)."
entries = [json.loads(l) for l in lines]
assert len(entries) == 2, f"One log line per request, got {len(entries)}."
e = entries[0]
assert e["msg"] == "request" and e["request_id"] == rid and e["method"] == "GET" and e["path"] == "/hello" and e["status"] == 200, f"Got {e!r}."
assert isinstance(e["ms"], float) and e["ms"] >= 0, "ms: a float, rounded to 1 decimal."
assert entries[1]["status"] == 404 and entries[1]["path"] == "/nope", "Log failures too."
