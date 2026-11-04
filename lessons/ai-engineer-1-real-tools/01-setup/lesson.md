---
title: Set up your AI Python
xp: 40
---
# Real libraries, on your computer

> **Warm-up:** why can't the browser Python in the other courses run PyTorch?

Until now every Python lesson ran **inside your browser** (Pyodide). That's great for learning, but real AI work uses big compiled libraries: **NumPy** (fast arrays), **pandas** (tables), **PyTorch** (neural networks on CPU or GPU), **scikit-learn** (classic machine learning) and **FastAPI** (web APIs). They can't run in the browser.

So the AI engineer courses run your code with **Python on the computer where CodeQuest runs**. CodeQuest looks for it in this order:

1. the path in the environment variable `CODEQUEST_AI_PYTHON`, if you set one;
2. a **virtual environment** at `~/.codequest/ai-venv` (on Windows `C:\Users\<you>\.codequest\ai-venv`);
3. otherwise the Python that runs CodeQuest itself.

A **virtual environment** ("venv") is a private folder of packages for one project, so different projects can't break each other. Real AI engineers make one per project. Let's make yours.

## The quick way: one command

In your CodeQuest folder:

- **Windows:** double-click `setup-ai.bat` (needs Python 3.12 from python.org).
- **Linux and NixOS:** run `./setup-ai.sh` in a terminal. On NixOS it builds the packages with Nix instead of pip.

It takes a few minutes (PyTorch is big) and ends with "All AI packages work." Then go straight to **Your quest**. If it fails, the step-by-step version below shows what the script does, so you can find the step that broke.

## Make the venv by hand

**Windows** (PowerShell), with Python 3.12 from python.org:

```
py -3.12 -m venv $HOME\.codequest\ai-venv
$HOME\.codequest\ai-venv\Scripts\python -m pip install --upgrade pip
$HOME\.codequest\ai-venv\Scripts\python -m pip install torch
$HOME\.codequest\ai-venv\Scripts\python -m pip install -r requirements-ai.txt
```

Run the last line inside your CodeQuest folder (the file `requirements-ai.txt` is there).

**Linux** (most distributions):

```
python3 -m venv ~/.codequest/ai-venv
~/.codequest/ai-venv/bin/pip install --upgrade pip
~/.codequest/ai-venv/bin/pip install torch --index-url https://download.pytorch.org/whl/cpu
~/.codequest/ai-venv/bin/pip install -r requirements-ai.txt
```

The `--index-url …/cpu` line gets the small CPU-only PyTorch (about 200 MB instead of several GB with CUDA). Every lesson here runs fine on a CPU. For an AMD GPU later, PyTorch's website lists a ROCm command.

**NixOS:** pip's prebuilt packages often can't find system libraries. Easiest: make a shell with the packages from nixpkgs (`nix-shell -p "python3.withPackages (ps: with ps; [ torch numpy pandas scikit-learn fastapi httpx pydantic pytest uvicorn pyyaml ])"`), run `which python3` inside it, and start CodeQuest with `CODEQUEST_AI_PYTHON` set to that path.

No restart needed: CodeQuest looks for the venv every time you press Run.

## Your quest

Write `versions()` returning a dict with the version strings of `numpy`, `pandas`, `torch`, `sklearn` and `fastapi` (each module has `__version__`). Press **Run**: if one is missing you'll see `ModuleNotFoundError`, so go back to the commands above.

**Remember:** one venv per project; never `pip install` into your system Python.

## Review

<details><summary>Why do these courses run on your computer instead of the browser?</summary>PyTorch, NumPy and friends are large compiled libraries that the browser Python can't load.</details>
