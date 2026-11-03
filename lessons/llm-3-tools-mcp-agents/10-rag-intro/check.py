ch, rt = ns.get("chunk"), ns.get("retrieve")
assert ch and rt, "Keep chunk and retrieve."
text = "a b c d e f g h i j"
got = ch(text, 4, 1)
assert got == ["a b c d", "d e f g", "g h i j"], f"chunk('a b c d e f g h i j', 4, 1) returned {got!r}, expected ['a b c d', 'd e f g', 'g h i j']."
got = ch(text, 4, 0)
assert got == ["a b c d", "e f g h", "i j"], f"chunk(text, 4, 0) returned {got!r}, expected ['a b c d', 'e f g h', 'i j']."
got = ch("one two", 5, 2)
assert got == ["one two"], f"A text shorter than one chunk should give one chunk, got {got!r}."
chunks = ["cats purr softly", "dogs bark loudly", "cats and dogs play"]
got = rt("why do cats purr", chunks, 2)
assert got == ["cats purr softly", "cats and dogs play"], f"retrieve('why do cats purr', ...) returned {got!r}, expected the two cat chunks, best first."
assert len(rt("dogs", chunks, 1)) == 1, "retrieve should return exactly k chunks."
