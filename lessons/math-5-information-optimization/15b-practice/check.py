import math
bi, tl, pp, kl, we = (ns.get(n) for n in ("bits", "token_loss", "perplexity", "kl", "worst_error"))
assert all((bi, tl, pp, kl, we)), "Keep all five functions."
assert abs(bi(1 / 8) - 3) < 1e-12 and abs(bi(1)) < 1e-12, "1. bits: −log₂ p."
assert abs(tl(0.25) - 1.3863) < 1e-4, "2. token_loss: −ln p."
assert abs(pp(math.log(4)) - 4) < 1e-9, "3. perplexity: e^loss."
assert abs(kl([0.5, 0.5], [0.9, 0.1]) - 0.5108) < 1e-4 and kl([1, 0], [0.5, 0.5]) > 0 and abs(kl([0.3, 0.7], [0.3, 0.7])) < 1e-12, "4. kl: Σ p · ln(p / q), skipping p = 0."
assert abs(we(4, 1) - 1 / 15) < 1e-12 and abs(we(8, 2) - 2 / 255) < 1e-12, "5. worst_error: half of 2m / (2ᵇ − 1)."
