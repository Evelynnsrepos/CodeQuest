---
title: The RAG prompt and citations
minutes: 40
xp: 55
hint: build_prompt: for c in chunks: line = "[" + str(len(lines) + 1) + "] (" + c["id"] + ") " + c["text"], and break if total + tokens(line) > budget
hint: After the loop: prompt = HEADER + "\n\n" + "\n".join(lines) + "\n\nQuestion: " + question, then return prompt, used
hint: citations: for n in re.findall(r"\[(\d+)\]", answer): add int(n) to found if it's not there yet, then return sorted(found)
hint: check_answer: no citations → "ok" only if "i don't know" is in answer.lower(). Then any n < 1 or n > n_sources → "bad citation"
---
# Make the model show its sources

⏱️ About 40 minutes

> **Warm-up:** a RAG answer says "Run nix-collect-garbage -d". How can the user check that it didn't make that up?

The retrieved chunks go into the prompt **numbered**, and the model is told to answer **only** from them and cite them like `[2]`. Then your code can **verify** the citations:

```
Answer the question using only the sources below. Cite sources like [1].
If the sources don't contain the answer, say "I don't know".

[1] (nix-gc) Old generations fill the disk. Run nix-collect-garbage -d ...
[2] (nix-flakes) A flake is a Nix project ...

Question: how do I free disk space on NixOS?
```

Three rules that make RAG trustworthy:

1. **"I don't know" is allowed.** Without it, the model invents an answer when retrieval failed.
2. **Budget the context** (LLMs 9 lesson 02): add chunks best-first until the token budget is used up, never cut one in the middle.
3. **Check citations in code:** every `[n]` must refer to a source that was actually given. An answer with no citations, or with a made-up `[7]`, gets flagged.

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `"[" + str(len(lines) + 1) + "] ("` | | builds `[1] (`, `[2] (`, ...: the next number is one more than the lines so far |
| `tokens(line)` | | the given estimate: characters // 4 |
| `"\n\n"` | | two line breaks: an empty line |
| `re.findall(r"\[(\d+)\]", answer)` | | every number inside square brackets. `\[` is a real `[`, `\d+` is "one or more digits", and the round brackets say "give me this part". `"see [1] and [3]"` → `["1", "3"]`. |
| `int(n)` | | the text `"3"` → the number 3 |
| `sorted(found)` | | smallest first |
| `answer.lower()` | | so "I don't know" and "i don't know" both match |

### 👀 Worked example: the budget

Budget 40 tokens. Chunk 1's line is `[1] (nix-gc) Run nix-collect-garbage -d to delete old generations.`: 66 characters → 66 // 4 = 16 tokens. 0 + 16 ≤ 40 → keep it, total 16. Chunk 2's line is 55 characters → 13 tokens. 16 + 13 = 29 ≤ 40 → keep it too. A third chunk of 15 tokens would make 44 > 40 → stop.

## 🎯 Your quest

Tokens are estimated as `len(text) // 4` (the starter's `tokens`).

1. `build_prompt(question, chunks, budget)`: `chunks` are dicts with `"id"` and `"text"`, best first. Add sources `[1]`, `[2]`, … as lines `"[n] (id) text"` while the total `tokens` of the source lines stays ≤ `budget`; stop at the first one that doesn't fit. Return `(prompt, used_ids)`. The prompt is the `HEADER`, a blank line, the source lines, a blank line, then `"Question: " + question`.
2. `citations(answer)`: the sorted list of distinct numbers cited as `[n]`.
3. `check_answer(answer, n_sources)`: `"ok"`, `"no citations"` (unless the answer contains "I don't know", which is fine without citations), or `"bad citation"` if any number is outside 1..n_sources.

**Part 1:** `build_prompt`. Replace `return "", []` with:

1. `lines = []`
2. `used = []`
3. `total = 0`
4. `for c in chunks:`
5. `    line = "[" + str(len(lines) + 1) + "] (" + c["id"] + ") " + c["text"]`
6. `    if total + tokens(line) > budget:`
7. `        break`
8. `    lines.append(line)`
9. `    used.append(c["id"])`
10. `    total = total + tokens(line)`
11. `prompt = HEADER + "\n\n" + "\n".join(lines) + "\n\nQuestion: " + question`
12. `return prompt, used`

**Part 2:** `citations`. Replace `return []` with:

1. `found = []`
2. `for n in re.findall(r"\[(\d+)\]", answer):`
3. `    if int(n) not in found:`
4. `        found.append(int(n))`
5. `return sorted(found)`

**Part 3:** `check_answer`. Above its `return "ok"` line, type:

1. `cited = citations(answer)`
2. `if len(cited) == 0:`
3. `    if "i don't know" in answer.lower():`
4. `        return "ok"`
5. `    return "no citations"`
6. `for n in cited:`
7. `    if n < 1 or n > n_sources:`
8. `        return "bad citation"`

**Remember:** numbered sources in, verified citations out.

## Review

<details><summary>What does recall@3 measure?</summary>The share of questions whose right chunk is among the top 3 results.</details>
