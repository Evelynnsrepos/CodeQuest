import os, tempfile
import numpy as np
VS = ns.get("VectorStore")
assert VS, "Keep VectorStore."
s = VS(2)
s.add([{"id": "a", "tag": "nix"}, {"id": "b", "tag": "git"}], np.array([[1.0, 0.0], [0.0, 1.0]]))
s.add([{"id": "c", "tag": "nix"}], np.array([[0.6, 0.8]]))
r = s.search(np.array([1.0, 0.0]), k=2)
assert [it["id"] for it, _ in r] == ["a", "c"] and abs(r[1][1] - 0.6) < 1e-9, f"search: best first with scores. Got {r!r}."
r = s.search(np.array([0.0, 1.0]), k=1, where={"tag": "nix"})
assert [it["id"] for it, _ in r] == ["c"], "where={'tag': 'nix'} must skip b even though it scores higher."
assert s.search(np.array([1.0, 0.0]), where={"tag": "rust"}) == [], "No match → []."
assert len(s.search(np.array([1.0, 0.0]), k=10)) == 3, "k larger than the store: return everything."
with tempfile.TemporaryDirectory() as d:
    p = os.path.join(d, "store")
    s.save(p)
    t = VS.load(p)
    assert t.items == s.items and np.allclose(t.vectors, s.vectors), "save/load should round-trip items and vectors."
