from fastapi.testclient import TestClient
app, get_llm, rt = ns.get("app"), ns.get("get_llm"), ns.get("run_tests")
assert app is not None and get_llm and rt, "Keep app, get_llm and run_tests."
c = TestClient(app)
app.dependency_overrides[get_llm] = lambda: (lambda text: text.upper())
r = c.post("/ask", json={"text": "abc"})
assert r.status_code == 200 and r.json() == {"answer": "ABC"}, f"/ask must use Depends(get_llm). Got {r.status_code} {r.text}."
app.dependency_overrides.clear()
r = c.post("/ask", json={"text": "abc"})
assert r.status_code == 503 and r.json() == {"detail": "model unavailable"}, f"A RuntimeError from the model → 503. Got {r.status_code} {r.text}."
assert rt() is True, "run_tests() should return True."
assert app.dependency_overrides == {}, "run_tests must clear the overrides when it's done."
