---
title: The RAG prompt and citations
xp: 55
---
# Make the model show its sources

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

## Your quest

Tokens are estimated as `len(text) // 4` (the starter's `tokens`).

1. `build_prompt(question, chunks, budget)`: `chunks` are dicts with `"id"` and `"text"`, best first. Add sources `[1]`, `[2]`, … as lines `"[n] (id) text"` while the total `tokens` of the source lines stays ≤ `budget`; stop at the first one that doesn't fit. Return `(prompt, used_ids)`. The prompt is the `HEADER`, a blank line, the source lines, a blank line, then `"Question: " + question`.
2. `citations(answer)`: the sorted list of distinct numbers cited as `[n]`.
3. `check_answer(answer, n_sources)`: `"ok"`, `"no citations"` (unless the answer contains "I don't know", which is fine without citations), or `"bad citation"` if any number is outside 1..n_sources.

**Remember:** numbered sources in, verified citations out.

## Review

<details><summary>What does recall@3 measure?</summary>The share of questions whose right chunk is among the top 3 results.</details>
