from fastapi.testclient import TestClient
app, FEEDBACK = ns.get("app"), ns.get("FEEDBACK")
assert app is not None and FEEDBACK is not None, "Keep app and FEEDBACK."
c = TestClient(app)
r = c.get("/health")
assert r.status_code == 200 and r.json() == {"status": "ok"}, "GET /health → {'status': 'ok'}."
r = c.post("/ask", json={"text": "hi"})
assert r.status_code == 200 and r.json()["sources"] == ["note-0", "note-1", "note-2"], f"/ask with default k = 3. Got {r.status_code} {r.text}."
assert c.post("/ask", json={"text": "hi", "k": 1}).json()["sources"] == ["note-0"], "Pass k through."
for bad in ({"text": ""}, {"text": "hi", "k": 0}, {"text": "hi", "k": 11}, {"k": 2}, {"text": "x" * 2001}):
    assert c.post("/ask", json=bad).status_code == 422, f"{bad} must be rejected with 422."
n = len(FEEDBACK)
r = c.post("/feedback", json={"question": "q", "rating": 5})
assert r.status_code == 200 and r.json() == {"saved": n + 1} and FEEDBACK[-1] == {"question": "q", "rating": 5}, f"/feedback stores and counts. Got {r.text}."
assert c.post("/feedback", json={"question": "q", "rating": 6}).status_code == 422, "rating must be 1 to 5."
