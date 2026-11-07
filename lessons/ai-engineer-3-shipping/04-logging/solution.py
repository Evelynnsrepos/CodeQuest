import json
import logging
import time
import uuid
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient

log = logging.getLogger("app")
log.setLevel(logging.INFO)


class JsonFormatter(logging.Formatter):
    def format(self, record):
        data = {"level": record.levelname, "msg": record.getMessage()}
        extra = getattr(record, "extra_fields", {})
        for key in extra:
            data[key] = extra[key]
        return json.dumps(data)


app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = uuid.uuid4().hex
    start = time.perf_counter()
    response = await call_next(request)
    ms = round((time.perf_counter() - start) * 1000, 1)
    fields = {"request_id": request_id, "method": request.method, "path": request.url.path, "status": response.status_code, "ms": ms}
    log.info("request", extra={"extra_fields": fields})
    response.headers["X-Request-ID"] = request_id
    return response


@app.get("/hello")
def hello():
    return {"hi": True}


handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
log.addHandler(handler)
r = TestClient(app).get("/hello")
print(r.headers.get("X-Request-ID"))
