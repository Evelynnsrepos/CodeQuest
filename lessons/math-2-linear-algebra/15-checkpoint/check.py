mb, mf, sh = ns.get("mlp_batch"), ns.get("mlp_flops"), ns.get("shapes")
assert mb and mf and sh, "Keep mlp_batch, mlp_flops and shapes."
X = [[1, 0, 2], [0, 1, -1]]
W1 = [[1, 1, 0], [0, -1, 1], [2, 0, 0]]
b1 = [0, 0, -1]
W2 = [[1, 0, 1], [0, 1, -1]]
b2 = [0.5, 0]
# H row1: [1, 2, 2-1=1] ; row2: [1, -2->0, -1->0]... computed by hand below
got = mb(X, W1, b1, W2, b2)
assert got == [[2.5, 1], [1.5, 0]], f"Expected [[2.5, 1], [1.5, 0]], got {got!r}. H = ReLU(X W1ᵀ + b1), then H W2ᵀ + b2."
assert mf(1, 2, 3, 4) == 2 * 2 * 3 + 2 * 3 * 4, "Two products: 2·batch·d_in·d_hidden + 2·batch·d_hidden·d_out."
assert tuple(sh(4, 3, 5, 2)) == ((4, 3), (5, 3), (4, 5), (2, 5), (4, 2)), f"shapes(4, 3, 5, 2) is wrong: {sh(4, 3, 5, 2)!r}."
