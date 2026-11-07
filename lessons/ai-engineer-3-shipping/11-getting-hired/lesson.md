---
title: Ready for an AI engineer job
minutes: 40
xp: 50
hint: First find the first non-empty line (loop with break) and collect every line that starts with # (lower-cased) in heads
hint: report = {...} with title, docker and numbers already filled in, and run, eval and license as False for now
hint: Loop: for h in heads: and set report["run"], report["eval"] or report["license"] to True when its word is in h
hint: score: report = readme_report(text), then count the keys whose value is True
---
# What employers look for, and how to show it

⏱️ About 40 minutes

> **Warm-up:** an employer has 5 minutes to look at your GitHub. What should they find?

Junior AI engineer job ads in 2026 usually ask for some mix of: **Python** (solid, with tests), **LLM APIs and prompting**, **RAG** (embeddings, vector databases), **evaluation**, **FastAPI or similar**, **Docker**, **git and CI**, some **PyTorch** and **classic ML** (scikit-learn), **SQL**, a cloud platform basics, and the judgement to know when *not* to use an LLM. You've now practised all of these except SQL and cloud.

**What gets you hired is proof, not certificates:**

1. **One or two real, finished projects** beat ten tutorials. "Finished" means: a README that explains the problem and how to run it, tests, a Dockerfile, CI that's green, and **numbers** (eval results).
2. **Show your evaluation.** "Hybrid search raised recall@3 from 0.71 to 0.92 on 60 hand-written questions" is the sentence that makes an interviewer lean in.
3. **Write about it.** A short blog post or a detailed README section on what failed and what you changed.
4. **Know the trade-offs** you'll be asked about: RAG vs fine-tuning, local vs API models, cost vs quality, how you'd monitor it in production, what you'd do about hallucinations and personal data.

**A README that works** has: a one-line description, a screenshot or example, how to run it (with Docker), how it works (a short diagram or list), evaluation results, limitations, and a license.

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `for l in lines:` ... `break` | | stops at the first line that isn't empty |
| `l.startswith("#")` | | a Markdown heading: `# Title`, `## Run it` |
| `l.lower()` | | so `## Run It` and `## run it` both match |
| `"docker run" in low` | | is that text anywhere in the README? |
| `re.search(r"\d+%\|\d\.\d+", text)` | | searches for a pattern. `\d` means one digit, `\d+` one or more digits, `\|` means "or", `\.` a real dot. So it finds `97%` or `0.92`. |
| `... is not None` | | `re.search` gives `None` when nothing was found, so this is `True` when something was |
| `report["run"] = True` | | changes one value in the dictionary |
| `if report[key]:` | | true when that check passed |

### 👀 Worked example: a tiny README

```
# Todo app

## Usage
python app.py
```

1. **title**: the first non-empty line is `# Todo app` → starts with `# ` → True.
2. Headings: `# todo app`, `## usage`. `usage` is in `## usage` → **run** True.
3. No `docker run` → **docker** False. No eval/results heading → **eval** False.
4. No number like `97%` or `0.92` → **numbers** False. No license heading → **license** False.
5. `score` counts the True values: **2**.

## 🎯 Your quest

`readme_report(text)`: check a README (Markdown) and return a dict with a boolean for each of these keys:

- `"title"`: the first non-empty line starts with `# `;
- `"run"`: some heading (a line starting with `#`) contains "run", "install" or "usage" (any case);
- `"docker"`: the text mentions `docker run` or `docker compose`;
- `"eval"`: some heading contains "eval" or "results";
- `"numbers"`: the text contains at least one percentage or a decimal number like `0.92` (regex `\d+%|\d\.\d+`);
- `"license"`: some heading contains "license".

Then `score(text)`: how many of the six are `True`. Write your own capstone's README in `MY_README` and get a 6.

**Part 1:** `readme_report`. Replace `return {}` with:

1. `lines = text.splitlines()`
2. `first = ""`
3. `for l in lines:`
4. `    if l.strip() != "":`
5. `        first = l`
6. `        break`
7. `heads = []`
8. `for l in lines:`
9. `    if l.startswith("#"):`
10. `        heads.append(l.lower())`
11. `low = text.lower()`
12. `report = {`
13. `    "title": first.startswith("# "),`
14. `    "run": False,`
15. `    "docker": "docker run" in low or "docker compose" in low,`
16. `    "eval": False,`
17. `    "numbers": re.search(r"\d+%|\d\.\d+", text) is not None,`
18. `    "license": False,`
19. `}`
20. `for h in heads:`
21. `    if "run" in h or "install" in h or "usage" in h:`
22. `        report["run"] = True`
23. `    if "eval" in h or "results" in h:`
24. `        report["eval"] = True`
25. `    if "license" in h:`
26. `        report["license"] = True`
27. `return report`

**Part 2:** `score`. Replace `return 0` with:

1. `report = readme_report(text)`
2. `total = 0`
3. `for key in report:`
4. `    if report[key]:`
5. `        total = total + 1`
6. `return total`

**Part 3:** replace the starter's `MY_README` with your own. This one gets a 6, so you can start from it and change the words:

```
MY_README = """# Notes RAG

Ask questions about my Linux and AI notes, with sources.

## Run it

    docker compose up
    # or: docker run -p 8000:8000 --env-file .env notes-rag

## How it works

Chunking, hybrid search (BM25 + nomic-embed-text, fused with RRF), answers with citations.

## Evaluation results

60 hand-written questions: recall@3 0.92 (BM25 alone: 0.71), 97% of answers with valid citations.

## Limitations

English and German notes only; no images.

## License

MIT
"""
```

**Remember:** finished projects with numbers beat certificates.

## Review

<details><summary>What does the four-fifths rule check?</summary>Whether each group's selection rate is at least 80% of the highest group's rate.</details>
