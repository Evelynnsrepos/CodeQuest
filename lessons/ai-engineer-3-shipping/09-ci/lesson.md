---
title: CI: tests on every push
minutes: 45
xp: 55
hint: data = yaml.safe_load(text) (use {} if it's None), trigger = data.get("on", data.get(True)), and a single word becomes a list: if isinstance(trigger, str): trigger = [trigger]
hint: Collect two lists: for name in jobs: for step in jobs[name].get("steps", []): uses.append(step.get("uses", "")) and runs.append(step.get("run", ""))
hint: Three flags: checkout and python from the uses list (startswith), tests from the runs list ("pytest" in r)
hint: Then one if per problem, in the order trigger, checkout, python, tests, secret ("sk-" in text)
hint: WORKFLOW: copy the YAML example at the top of the lesson (without the # notes)
---
# A robot that runs your tests

⏱️ About 45 minutes

> **Warm-up:** you fixed a bug at midnight and pushed. Did you run all the tests first?

**Continuous integration (CI)** runs your tests automatically on every push and pull request, on a clean machine. On GitHub it's **GitHub Actions**: a YAML file in `.github/workflows/`. The pull request then shows a green ✓ or a red ✗, and you never merge a red one.

```yaml
name: tests
on:
  push:
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4            # get the code
      - uses: actions/setup-python@v5        # install Python
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pytest -q                       # app tests (with fakes, lesson 03) and retrieval evals
```

**YAML** is indentation-based, like Python: two spaces per level, `key: value`, and `- ` for list items.

What to run in CI for an AI app: unit tests with fakes (fast, free, every push), the retrieval eval suite (fast, deterministic), and the LLM-judged evals only on a schedule or by hand (they cost money and need an API key stored as a **repository secret**, used as `${{ secrets.OPENAI_API_KEY }}`, never written in the file).

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `yaml.safe_load(text)` | | reads YAML text into Python dictionaries and lists |
| `data.get("on", data.get(True))` | | YAML reads the word `on` as `True` (yes/no), so look under both |
| `isinstance(trigger, str)` | | true if `trigger` is text, like `on: push` (one word instead of a list) |
| `trigger = [trigger]` | | `"push"` → `["push"]`, so the next check works the same for both |
| `jobs[name].get("steps", [])` | | the job's steps, or an empty list |
| `step.get("uses", "")` | | each step either **uses** an action or **runs** a command; the other one is `""` |
| `u.startswith("actions/checkout")` | | matches `actions/checkout@v4` and any other version |
| `not trigger` | | true when `trigger` is missing (`None`) or empty |

### 👀 Worked example: the starter's workflow

```yaml
on: push
jobs:
  test:
    steps:
      - run: echo hi
```

1. `trigger` = `"push"` → a list `["push"]`. `"pull_request"` isn't in it → **trigger**.
2. The only step: `uses` = `""`, `run` = `"echo hi"`. So `uses` = `[""]`, `runs` = `["echo hi"]`.
3. No use starts with `actions/checkout` → **checkout**. None with `actions/setup-python` → **python**.
4. No run contains `pytest` → **tests**.
5. No `sk-` in the text → no secret problem.

Result: `["trigger", "checkout", "python", "tests"]`.

## 🎯 Your quest

1. `check_workflow(text)`: parse with `yaml.safe_load` and return a list of problems, in this order: `"trigger"` (not triggered on both `push` and `pull_request`), `"checkout"` (no step uses `actions/checkout`), `"python"` (no step uses `actions/setup-python`), `"tests"` (no `run` step contains `pytest`), `"secret"` (the raw text contains `sk-`, a key pasted into the file). Note: YAML reads the key `on` as the boolean `True`, so look up `data.get("on", data.get(True))`.
2. Write `WORKFLOW` that passes.

Replace `return []` in `check_workflow` with:

**Part 1:** read the YAML:

1. `data = yaml.safe_load(text)`
2. `if data is None:`
3. `    data = {}`
4. `trigger = data.get("on", data.get(True))`
5. `if isinstance(trigger, str):`
6. `    trigger = [trigger]`
7. `jobs = data.get("jobs")`
8. `if jobs is None:`
9. `    jobs = {}`

**Part 2:** collect what every step uses and runs:

10. `uses = []`
11. `runs = []`
12. `for name in jobs:`
13. `    for step in jobs[name].get("steps", []):`
14. `        uses.append(step.get("uses", ""))`
15. `        runs.append(step.get("run", ""))`

**Part 3:** three yes/no flags:

16. `checkout = False`
17. `python = False`
18. `tests = False`
19. `for u in uses:`
20. `    if u.startswith("actions/checkout"):`
21. `        checkout = True`
22. `    if u.startswith("actions/setup-python"):`
23. `        python = True`
24. `for r in runs:`
25. `    if "pytest" in r:`
26. `        tests = True`

**Part 4:** the problem list:

27. `problems = []`
28. `if not trigger or "push" not in trigger or "pull_request" not in trigger:`
29. `    problems.append("trigger")`
30. `if not checkout:`
31. `    problems.append("checkout")`
32. `if not python:`
33. `    problems.append("python")`
34. `if not tests:`
35. `    problems.append("tests")`
36. `if "sk-" in text:`
37. `    problems.append("secret")`
38. `return problems`

**Part 5:** replace the starter's `WORKFLOW` text with the YAML example at the top of this lesson (leave out the `# ...` notes).

**Remember:** green before merge; secrets in repository settings, never in the file.

## Review

<details><summary>Why copy requirements.txt before the rest of the code in a Dockerfile?</summary>So the dependency layer stays cached when only your code changes.</details>
