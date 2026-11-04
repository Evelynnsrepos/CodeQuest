import re
from fastapi.testclient import TestClient
app, get_llm, TRACKER, NOTES = ns.get("app"), ns.get("get_llm"), ns.get("TRACKER"), ns.get("NOTES")
assert app is not None and get_llm and TRACKER is not None and NOTES, "Keep app, get_llm, TRACKER and NOTES."
c = TestClient(app)
assert c.get("/health").json() == {"status": "ok", "notes": len(NOTES)}, "/health returns status and the number of notes."
r = c.post("/search", json={"q": "which port does the ollama api use"})
assert r.status_code == 200 and r.json()["results"][0] == "ollama-api" and len(r.json()["results"]) <= 3, f"/search. Got {r.text}."
assert len(c.post("/search", json={"q": "nix", "k": 1}).json()["results"]) == 1, "/search respects k."
assert c.post("/search", json={"q": "zzzz qqqq"}).json() == {"results": []}, "Only notes with a score above 0."
assert c.post("/search", json={"q": ""}).status_code == 422 and c.post("/search", json={"q": "x", "k": 11}).status_code == 422, "Validate /search."
seen = {}
def fake():
    def llm(prompt):
        seen["prompt"] = prompt
        return "Run nix-collect-garbage -d [1].", 120, 9
    return llm
app.dependency_overrides[get_llm] = fake
try:
    n = len(TRACKER)
    r = c.post("/ask", json={"question": "how do I delete old nix generations"})
    assert r.status_code == 200, f"/ask failed: {r.status_code} {r.text}"
    body = r.json()
    assert body["answer"] == "Run nix-collect-garbage -d [1]." and body["sources"][0] == "nix-gc", f"Got {body!r}."
    p = seen["prompt"]
    for k, sid in enumerate(body["sources"], 1):
        assert f"[{k}] ({sid}) " in p, f"The prompt should list source [{k}] ({sid})."
    assert all(1 <= int(x) <= len(body["sources"]) for x in re.findall(r"\[(\d+)\]", body["answer"])), "Citations must point to given sources."
    assert len(TRACKER) == n + 1 and TRACKER[-1]["tokens_in"] == 120 and TRACKER[-1]["tokens_out"] == 9, "Record tokens in TRACKER."
    seen.clear()
    r = c.post("/ask", json={"question": "zzzz qqqq"})
    assert r.json() == {"answer": "I don't know.", "sources": []} and not seen, "No sources → I don't know, without calling the model."
    def broken():
        def llm(prompt):
            raise RuntimeError("down")
        return llm
    app.dependency_overrides[get_llm] = broken
    assert c.post("/ask", json={"question": "nix"}).status_code == 503, "Model down → 503."
    assert c.post("/ask", json={"question": ""}).status_code == 422, "Validate /ask."
finally:
    app.dependency_overrides.clear()
ev = c.get("/eval").json()
assert ev["recall@3"] >= 0.9, f"recall@3 should be at least 0.9, got {ev!r}."
