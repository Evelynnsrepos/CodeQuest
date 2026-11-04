lo, im, il = ns.get("load_order"), ns.get("imports"), ns.get("index_loaded")
assert lo and im and il, "Keep load_order, imports and index_loaded."
ex = {"/home/eve/.claude/CLAUDE.md", "/home/eve/CodeQuest/CLAUDE.md", "/home/eve/CodeQuest/CLAUDE.local.md",
      "/home/eve/CodeQuest/lessons/CLAUDE.md", "/home/eve/CodeQuest/lessons/sub/CLAUDE.md"}
want = ["/home/eve/.claude/CLAUDE.md", "/home/eve/CodeQuest/CLAUDE.md", "/home/eve/CodeQuest/CLAUDE.local.md", "/home/eve/CodeQuest/lessons/CLAUDE.md"]
got = lo("/home/eve/CodeQuest/lessons", ex, "/home/eve")
assert got == want, f"load_order wrong: {got!r}. Subfolders below cwd load later, not at launch."
ex2 = {"/home/eve/CodeQuest/.claude/CLAUDE.md", "/home/eve/CodeQuest/CLAUDE.md"}
assert lo("/home/eve/CodeQuest", ex2, "/home/eve") == ["/home/eve/CodeQuest/CLAUDE.md", "/home/eve/CodeQuest/.claude/CLAUDE.md"], "CLAUDE.md, then .claude/CLAUDE.md in the same folder."
ex3 = {"/home/eve/.claude/CLAUDE.md"}
assert lo("/home/eve", ex3, "/home/eve") == ["/home/eve/.claude/CLAUDE.md"], "Don't list the user file twice."
assert im("See @docs/testing.md and `@README` and @~/notes.md") == ["docs/testing.md", "~/notes.md"], f"imports wrong: {im('See @docs/testing.md and `@README` and @~/notes.md')!r}."
assert im("@AGENTS.md\nmail me at a@b.com") == ["AGENTS.md"], "An @ inside a word (an email) is not an import."
lines = ["- note %d" % i for i in range(300)]
assert il(lines) == lines[:200], "Only the first 200 lines load."
big = ["x" * 999] * 100
assert len(il(big)) == 25, "At most 25,000 characters (999 + 1 per line → 25 lines)."
