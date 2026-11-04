---
title: Logs you can search
xp: 55
---
# One JSON line per request

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

## Your quest

1. `JsonFormatter.format(record)`: return `json.dumps` of a dict with `"level"` (`record.levelname`), `"msg"` (`record.getMessage()`), plus every key of `record.extra_fields` if the record has that attribute.
2. The middleware: make a request id with `uuid.uuid4().hex`, run the request, then `log.info("request", extra={"extra_fields": {...}})` with `request_id`, `method`, `path`, `status` and `ms` (rounded to 1 decimal), and set the response header `X-Request-ID`.

**Remember:** one JSON line per request, with an id the user can see.

## Review

<details><summary>How do you test an endpoint without calling the real model?</summary>Override its dependency with a fake via app.dependency_overrides.</details>
