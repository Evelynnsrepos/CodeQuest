def hsa_override(gfx):
    # if gfx.startswith("gfx103"):
    #     return "10.3.0"
    # if gfx.startswith("gfx110"):
    #     return "11.0.0"
    return None


cards = {"RX 6700 XT": "gfx1031", "RX 6800": "gfx1030", "RX 7700 XT": "gfx1101", "RX 580": "gfx803"}
for card in cards:
    print(card, cards[card], hsa_override(cards[card]))
