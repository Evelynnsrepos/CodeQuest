cw, cs, wm = ns.get("chunk_words"), ns.get("chunk_sentences"), ns.get("with_meta")
assert cw and cs and wm, "Keep chunk_words, chunk_sentences and with_meta."
text = "One two three four five six seven eight nine ten"
assert cw(text, 4, 1) == ["One two three four", "four five six seven", "seven eight nine ten"], f"Got {cw(text, 4, 1)!r}."
assert cw(text, 4, 0) == ["One two three four", "five six seven eight", "nine ten"], "No overlap: plain windows, the last one shorter."
assert cw("a b", 5, 2) == ["a b"], "Short text: one chunk."
try:
    cw(text, 3, 3)
    raise AssertionError("overlap >= size should raise ValueError.")
except ValueError:
    pass
got = cs("Short one. This is the second sentence here. Third! And a fourth?", 6)
assert got == ["Short one.", "This is the second sentence here.", "Third! And a fourth?"], f"Got {got!r}."
assert cs("A very long sentence that has more than five words.", 5) == ["A very long sentence that has more than five words."], "An over-long sentence is its own chunk."
assert wm("notes", ["a", "b"]) == [{"id": "notes#0", "doc": "notes", "text": "a"}, {"id": "notes#1", "doc": "notes", "text": "b"}], "with_meta: id is doc#index."
