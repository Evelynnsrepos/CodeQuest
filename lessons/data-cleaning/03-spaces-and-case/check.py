t, k, d = ns.get("tidy"), ns.get("key"), ns.get("distinct")
assert t and k and d, "Keep tidy, key and distinct."
assert t("  Ber\u200blin \t\n ") == "Berlin", f"tidy: remove \\u200b, strip, collapse. Got {t('  Ber\u200blin ')!r}."
assert t("New   York\xa0City") == "New York City", "tidy: collapse inner spaces (including the non-breaking one)."
assert t(None) is None, "tidy(None) is None."
assert k("STRASSE") == k("Straße") == "strasse", "key: casefold, so ß matches SS."
assert d(["Berlin", "berlin ", " BERLIN", None, "Köln"]) == 2, "distinct: Berlin (3 spellings) and Köln."
