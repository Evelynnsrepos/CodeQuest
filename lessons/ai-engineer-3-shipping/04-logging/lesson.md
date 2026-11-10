---
title: Logs you can search
minutes: 40
xp: 55
hint: format: data = {"level": record.levelname, "msg": record.getMessage()}, extra = getattr(record, "extra_fields", {}), copy every key of extra into data
hint: format: return json.dumps(data)
hint: middleware: request_id = uuid.uuid4().hex and start = time.perf_counter(), then response = await call_next(request)
hint: middleware: ms = round((time.perf_counter() - start) * 1000, 1), build fields, log.info("request", extra={"extra_fields": fields}), set the header, return response
---
# One JSON line per request

⏱️ About 40 minutes

> **Warm-up:** a user says "it gave me a weird answer yesterday around 3". How would you find that request?

With **structured logs**: one JSON object per line, with the same fields every time, so tools (Grafana Loki, Datadog, or just `grep` and `jq`) can filter them. For an AI service, log per request:

- `request_id`: a unique id, also sent back to the client in a header (`X-Request-ID`), so a user can quote it;
- `method`, `path`, `status`, `ms` (how long it took);
- for model calls: model name, token counts, cost (lesson 06).

**Don't log:** secrets, and usually not full prompts/answers with personal data (GDPR, lesson 10). If you must keep them for debugging, keep them short-term and protected.

FastAPI **middleware** runs around every request, which is the right place for this:

```python
@app.middleware("http")
async def log_requests(request, call_next):
    start = time.perf_counter()
    response = await call_next(request)          # run the endpoint
    ...                                          # log, add headers
    return response
```

Python's `logging` module sends messages to handlers; a **formatter** decides what a line looks like.

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `record.levelname`, `record.getMessage()` | | the level (`"INFO"`) and the message of one log entry |
| `getattr(record, "extra_fields", {})` | | the record's `extra_fields`, or `{}` if it has none |
| `data[key] = extra[key]` | | copies one field into the dictionary |
| `json.dumps(data)` | | the dictionary as one line of JSON text |
| `uuid.uuid4().hex` | | a random id like `"1bee6a31..."`, different every time |
| `await call_next(request)` | | runs the actual endpoint and waits for its response. `async`/`await` is how FastAPI waits without blocking; just keep the words where they are. |
| `round(x, 1)` | | one decimal place |
| `request.method`, `request.url.path` | | `"GET"`, `"/hello"` |
| `response.headers["X-Request-ID"] = request_id` | | adds a header the caller can see |

### 👀 What one log line looks like

A `GET /hello` that takes 0.7 ms becomes:

```
{"level": "INFO", "msg": "request", "request_id": "1bee6a31...", "method": "GET", "path": "/hello", "status": 200, "ms": 0.7}
```

One JSON object per line is easy for log tools to search: "show me every request with status 500 today".

## 🎯 Your quest

1. `JsonFormatter.format(record)`: return `json.dumps` of a dict with `"level"` (`record.levelname`), `"msg"` (`record.getMessage()`), plus every key of `record.extra_fields` if the record has that attribute.
2. The middleware: make a request id with `uuid.uuid4().hex`, run the request, then `log.info("request", extra={"extra_fields": {...}})` with `request_id`, `method`, `path`, `status` and `ms` (rounded to 1 decimal), and set the response header `X-Request-ID`.

**Part 1:** `JsonFormatter.format`. Replace `return ""` with (8 spaces, it's inside a class):

1. `data = {"level": record.levelname, "msg": record.getMessage()}`
2. `extra = getattr(record, "extra_fields", {})`
3. `for key in extra:`
4. `    data[key] = extra[key]`
5. `return json.dumps(data)`

**Part 2:** the middleware `log_requests`. Replace `return await call_next(request)` with:

1. `request_id = uuid.uuid4().hex`
2. `start = time.perf_counter()`
3. `response = await call_next(request)`
4. `ms = round((time.perf_counter() - start) * 1000, 1)`
5. `fields = {"request_id": request_id, "method": request.method, "path": request.url.path, "status": response.status_code, "ms": ms}`
6. `log.info("request", extra={"extra_fields": fields})`
7. `response.headers["X-Request-ID"] = request_id`
8. `return response`

**Remember:** one JSON line per request, with an id the user can see.

## Review

<details><summary>How do you test an endpoint without calling the real model?</summary>Override its dependency with a fake via app.dependency_overrides.</details>
