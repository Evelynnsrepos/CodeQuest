import json
import httpx
import numpy as np
no, oe, LE = ns.get("normalize"), ns.get("ollama_embed"), ns.get("LocalEmbedder")
assert no and oe and LE, "Keep normalize, ollama_embed and LocalEmbedder."
M = no(np.array([[3.0, 4.0], [0.0, 0.0]]))
assert np.allclose(M, [[0.6, 0.8], [0, 0]]), "normalize: rows of length 1; zero rows stay zero (no division by zero)."
seen = {}
def handler(request):
    seen["url"] = str(request.url); seen["body"] = json.loads(request.content)
    return httpx.Response(200, json={"embeddings": [[3, 4], [1, 0]]})
client = httpx.Client(transport=httpx.MockTransport(handler))
E = oe(["a", "b"], model="bge-m3", client=client)
assert seen["url"] == "http://localhost:11434/api/embed", f"POST to {{url}}/api/embed, got {seen.get('url')}."
assert seen["body"] == {"model": "bge-m3", "input": ["a", "b"]}, f"Send model and input. Got {seen['body']!r}."
assert np.allclose(E, [[0.6, 0.8], [1, 0]]), "Return the normalized embeddings."
bad = httpx.Client(transport=httpx.MockTransport(lambda r: httpx.Response(404, json={"error": "model not found"})))
try:
    oe(["a"], client=bad)
    raise AssertionError("A 404 should raise (use raise_for_status()).")
except httpx.HTTPStatusError:
    pass
emb = LE(["nix garbage collection", "hyprland keybinding"])
E = emb.embed(["nix garbage collect", "nix garbage collection", "hyprland bind"])
assert np.allclose(np.linalg.norm(E, axis=1), 1), "LocalEmbedder.embed: normalized rows."
assert E[0] @ E[1] > E[0] @ E[2], "Similar texts must score higher than unrelated ones."
