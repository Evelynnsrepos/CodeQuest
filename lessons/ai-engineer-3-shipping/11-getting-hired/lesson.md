---
title: Ready for an AI engineer job
xp: 50
---
# What employers look for, and how to show it

> **Warm-up:** an employer has 5 minutes to look at your GitHub. What should they find?

Junior AI engineer job ads in 2026 usually ask for some mix of: **Python** (solid, with tests), **LLM APIs and prompting**, **RAG** (embeddings, vector databases), **evaluation**, **FastAPI or similar**, **Docker**, **git and CI**, some **PyTorch** and **classic ML** (scikit-learn), **SQL**, a cloud platform basics, and the judgement to know when *not* to use an LLM. You've now practised all of these except SQL and cloud.

**What gets you hired is proof, not certificates:**

1. **One or two real, finished projects** beat ten tutorials. "Finished" means: a README that explains the problem and how to run it, tests, a Dockerfile, CI that's green, and **numbers** (eval results).
2. **Show your evaluation.** "Hybrid search raised recall@3 from 0.71 to 0.92 on 60 hand-written questions" is the sentence that makes an interviewer lean in.
3. **Write about it.** A short blog post or a detailed README section on what failed and what you changed.
4. **Know the trade-offs** you'll be asked about: RAG vs fine-tuning, local vs API models, cost vs quality, how you'd monitor it in production, what you'd do about hallucinations and personal data.

**A README that works** has: a one-line description, a screenshot or example, how to run it (with Docker), how it works (a short diagram or list), evaluation results, limitations, and a license.

## Your quest

`readme_report(text)`: check a README (Markdown) and return a dict with a boolean for each of these keys:

- `"title"`: the first non-empty line starts with `# `;
- `"run"`: some heading (a line starting with `#`) contains "run", "install" or "usage" (any case);
- `"docker"`: the text mentions `docker run` or `docker compose`;
- `"eval"`: some heading contains "eval" or "results";
- `"numbers"`: the text contains at least one percentage or a decimal number like `0.92` (regex `\d+%|\d\.\d+`);
- `"license"`: some heading contains "license".

Then `score(text)`: how many of the six are `True`. Write your own capstone's README in `MY_README` and get a 6.

**Remember:** finished projects with numbers beat certificates.

## Review

<details><summary>What does the four-fifths rule check?</summary>Whether each group's selection rate is at least 80% of the highest group's rate.</details>
