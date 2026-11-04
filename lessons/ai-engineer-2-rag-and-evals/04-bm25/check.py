import math
B = ns.get("BM25")
assert B, "Keep BM25."
docs = ["run nix-collect-garbage -d to free space", "nix flakes pin inputs", "hyprland binds and nix", "nix nix nix nix nix"]
bm = B(docs)
assert abs(bm.idf("nix") - math.log((4 - 3 + 0.5) / 3.5 + 1)) < 1e-9, "idf: ln((N − n + 0.5) / (n + 0.5) + 1). 'nix' is in 3 of 4 docs."
assert bm.idf("flakes") > bm.idf("nix"), "Rare words get a higher idf."
r = bm.search("nix-collect-garbage")
assert [i for i, _ in r] == [0], f"Only doc 0 contains nix-collect-garbage (one token, keep the hyphens). Got {r!r}."
s3, s1 = bm.score("nix", 3), bm.score("nix", 1)
assert s3 > s1 and s3 < 5 * s1, "Saturation: 5× 'nix' scores higher, but much less than 5×."
assert bm.search("rust cargo") == [], "No matching words → []."
r = bm.search("nix flakes", k=2)
assert r[0][0] == 1 and len(r) == 2, f"'nix flakes' → doc 1 first. Got {r!r}."
