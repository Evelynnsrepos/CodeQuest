---
title: An eval suite that runs itself
minutes: 40
xp: 60
hint: The TEST text is given. write_suite: with open(os.path.join(folder, "retriever.py"), "w", encoding="utf-8") as f: f.write(RETRIEVER)
hint: write_suite: the same for test_rag.py, with f.write(TEST.format(golden=repr(golden), threshold=threshold))
hint: run_suite: if folder not in sys.path: sys.path.insert(0, folder), then remove the two old modules, then return int(pytest.main([...]))
---
# Evals as tests

⏱️ About 40 minutes

> **Warm-up:** you tweak the system prompt. How do you know you didn't break something that used to work?

Turn your golden set into **tests** that run on every change, just like normal code tests. The tool is **pytest**: any function named `test_…` in a file named `test_….py` is a test; a failing `assert` fails it.

```python
# test_rag.py
import pytest
from app import retrieve

GOLDEN = [("how do I delete old nix generations", "nix-gc"), ...]

@pytest.mark.parametrize("question,right", GOLDEN)
def test_right_chunk_in_top3(question, right):
    assert right in retrieve(question, k=3)

def test_overall_recall():
    hits = 0
    for q, r in GOLDEN:
        if r in retrieve(q, k=3):
            hits = hits + 1
    assert hits / len(GOLDEN) >= 0.8
```

`parametrize` makes one test per golden item, so a failure tells you **which** question broke. The overall test sets a **threshold**: LLM output is noisy, so require "≥ 80%" rather than "all".

Run it with `pytest -q` in a terminal, or from Python with `pytest.main([...])`, which returns an exit code (0 = all passed, 1 = some failed). In AI engineer 3 you'll run it automatically on every push with GitHub Actions.

**Deterministic first:** test retrieval and output **format** (JSON valid? citations valid?) with exact asserts; those don't need an LLM. Use LLM-as-judge only for what truly needs judgement, and run those less often (they cost money).

## Python you need

`RETRIEVER` (a tiny search) and `TEST` (the test file) are **given** in the starter as long texts. You write the two functions that save them as files and run pytest.

| You write | Say it | What it does |
|---|---|---|
| `os.path.join(folder, "test_rag.py")` | | glues a folder and a file name with the right slash for your system |
| `with open(path, "w", encoding="utf-8") as f:` | | opens a file for writing (it's created if missing) |
| `f.write(text)` | | puts the text into the file |
| `TEST.format(golden=..., threshold=...)` | | fills `{golden}` and `{threshold}` in the text with these values |
| `repr(golden)` | | the list written the way Python would write it, with quotes, so it's valid code in the test file |
| `sys.path.insert(0, folder)` | | tells Python "look for modules in this folder first" |
| `sys.modules.pop(name, None)` | | forgets a module imported earlier, so the new file is read |
| `pytest.main([...])` | | runs pytest like the terminal command; returns 0 if all tests passed |

### 👀 Worked example: what `.format` does

`"x = {a}, limit {b}".format(a=repr(["hi"]), b=0.8)` gives `x = ['hi'], limit 0.8`. With the golden list, `GOLDEN = {golden}` in the test file becomes `GOLDEN = [('delete old generations', 'nix-gc')]`: real Python code.

## 🎯 Your quest

1. `write_suite(folder, golden, threshold)`: write two files into `folder`:
   - `retriever.py` containing exactly the `RETRIEVER` source given in the starter;
   - `test_rag.py`: imports `retrieve` from `retriever`, has `GOLDEN` (use `repr(golden)`), a parametrized `test_right_chunk_in_top3`, and `test_overall_recall` with your `threshold`.
2. `run_suite(folder)`: insert `folder` into `sys.path` (so the test can import `retriever`), remove `"retriever"` and `"test_rag"` from `sys.modules` (left over from an earlier run, they would hide the new files), then return `int(pytest.main(["-q", "-p", "no:cacheprovider", "--import-mode=importlib", "--rootdir", folder, folder]))`.

The check runs your suite twice: once with a good golden set (exit 0) and once with a broken item (exit 1).

**Part 1:** `write_suite`. Replace `pass` with:

1. `with open(os.path.join(folder, "retriever.py"), "w", encoding="utf-8") as f:`
2. `    f.write(RETRIEVER)`
3. `with open(os.path.join(folder, "test_rag.py"), "w", encoding="utf-8") as f:`
4. `    f.write(TEST.format(golden=repr(golden), threshold=threshold))`

**Part 2:** `run_suite`. Replace `return 1` with:

1. `if folder not in sys.path:`
2. `    sys.path.insert(0, folder)`
3. `for name in ["retriever", "test_rag"]:`
4. `    sys.modules.pop(name, None)`
5. `return int(pytest.main(["-q", "-p", "no:cacheprovider", "--import-mode=importlib", "--rootdir", folder, folder]))`

In line 5, `-q` means quiet output, `-p no:cacheprovider` stops pytest from writing a cache folder, and the last `folder` says which folder to test.

**Remember:** golden set → parametrized tests → a threshold → run on every change.

## Review

<details><summary>What does Cohen's κ correct for?</summary>Agreement that would happen by chance anyway.</details>
