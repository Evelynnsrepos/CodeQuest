def hsa_override(gfx):
    return None


for card, gfx in [("RX 6700 XT", "gfx1031"), ("RX 6800", "gfx1030"), ("RX 7700 XT", "gfx1101"), ("RX 580", "gfx803")]:
    print(f"{card:11} {gfx:8} → {hsa_override(gfx)}")
