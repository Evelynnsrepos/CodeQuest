---
title: An eval suite that runs itself
xp: 60
---
# Evals as tests

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
    hits = sum(r in retrieve(q, k=3) for q, r in GOLDEN)
    assert hits / len(GOLDEN) >= 0.8
```

`parametrize` makes one test per golden item, so a failure tells you **which** question broke. The overall test sets a **threshold**: LLM output is noisy, so require "≥ 80%" rather than "all".

Run it with `pytest -q` in a terminal, or from Python with `pytest.main([...])`, which returns an exit code (0 = all passed, 1 = some failed). In AI engineer 3 you'll run it automatically on every push with GitHub Actions.

**Deterministic first:** test retrieval and output **format** (JSON valid? citations valid?) with exact asserts; those don't need an LLM. Use LLM-as-judge only for what truly needs judgement, and run those less often (they cost money).

## Your quest

1. `write_suite(folder, golden, threshold)`: write two files into `folder`:
   - `retriever.py` containing exactly the `RETRIEVER` source given in the starter;
   - `test_rag.py`: imports `retrieve` from `retriever`, has `GOLDEN` (use `repr(golden)`), a parametrized `test_right_chunk_in_top3`, and `test_overall_recall` with your `threshold`.
2. `run_suite(folder)`: insert `folder` into `sys.path` (so the test can import `retriever`), remove `"retriever"` and `"test_rag"` from `sys.modules` (left over from an earlier run, they would hide the new files), then return `int(pytest.main(["-q", "-p", "no:cacheprovider", "--import-mode=importlib", "--rootdir", folder, folder]))`.

The check runs your suite twice: once with a good golden set (exit 0) and once with a broken item (exit 1).

**Remember:** golden set → parametrized tests → a threshold → run on every change.

## Review

<details><summary>What does Cohen's κ correct for?</summary>Agreement that would happen by chance anyway.</details>
