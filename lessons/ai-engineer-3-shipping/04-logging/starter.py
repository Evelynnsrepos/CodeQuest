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
        return ""


app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    return await call_next(request)


@app.get("/hello")
def hello():
    return {"hi": True}


handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
log.addHandler(handler)
r = TestClient(app).get("/hello")
print(r.headers.get("X-Request-ID"))
