import math
sb, sn, js = ns.get("surprise_bits"), ns.get("surprise_nats"), ns.get("joint_surprise")
assert sb and sn and js, "Keep surprise_bits, surprise_nats and joint_surprise."
assert sb(0.5) == 1 and sb(1) == 0, f"surprise_bits(0.5) = 1, got {sb(0.5)!r}."
assert abs(sb(1 / 6) - 2.5849625007) < 1e-9 and abs(sb(0.001) - 9.9657842847) < 1e-9, "Die 2.58 bits, raffle 9.97 bits."
assert abs(sn(0.5) - math.log(2)) < 1e-12, "Coin in nats: 0.693."
assert abs(js([0.5, 0.5]) - 2) < 1e-12 and abs(js([0.5, 0.25, 1]) - 3) < 1e-12, "Independent surprises add."
assert js([]) == 0, "Nothing happened: no surprise."
