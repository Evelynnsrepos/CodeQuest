import unicodedata
ct, rd, pc = ns.get("clean_text"), ns.get("redact"), ns.get("pii_counts")
assert ct and rd and pc, "Keep clean_text, redact and pii_counts."
decomposed = "Cafe\u0301"
assert ct(decomposed) == "Café" and len(ct(decomposed)) == 4, "clean_text: NFC turns e + accent into one é."
assert ct("a\x00b\x1bc\nd\te") == "abc\nd\te", "clean_text: drop control characters, keep \\n and \\t."
msg = "Hi, I'm Ada (ada.l+news@mail.example.de, +49 170 1234567). Please refund to DE89 3704 0044 0532 0130 00."
out = rd(msg)
assert out == "Hi, I'm Ada ([EMAIL], [PHONE]). Please refund to [IBAN].", f"Got {out!r}."
assert rd("call 030/1234567 or 0170-1234567") == "call [PHONE] or [PHONE]", "Phones with / and - too."
assert rd("version 3.12 on 2026") == "version 3.12 on 2026", "Short numbers aren't phones."
assert pc(msg) == {"EMAIL": 1, "IBAN": 1, "PHONE": 1}, f"Got {pc(msg)!r}."
