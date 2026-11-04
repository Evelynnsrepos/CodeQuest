# CodeQuest

A self-hosted, game-style coding course in the spirit of Boot.dev. It teaches **Python**, **GDScript** (Godot), **Lua**, **TypeScript**, **Rust**, **Nix** (with flakes) and **Git** with hands-on lessons, XP, levels and daily streaks. You run it on your computer and open it in any browser, including your phone or tablet on the same Wi-Fi.

## Install on Windows

1. Get the code with Git (from [git-scm.com](https://git-scm.com)): `git clone https://github.com/Evelynnsrepos/CodeQuest.git`
2. Open the `CodeQuest` folder and double-click **install.bat**. If Windows shows "Windows protected your PC", click **More info**, then **Run anyway**.
3. If Python isn't installed, it offers to install it. Say yes, then double-click `install.bat` again.
4. Answer the two questions (start automatically at login, open now).

Afterwards, open **CodeQuest** from the Start menu or the desktop icon. It runs quietly in the background, with no window to keep open. To stop it, use **Start menu > CodeQuest > Stop CodeQuest**. To remove it, use **Uninstall CodeQuest** in the same place. Running `install.bat` again updates CodeQuest and keeps your progress (see [Update](#update)).

For your phone or tablet: when Windows asks whether Python may use the network, tick **Private networks** and click **Allow**. Your Wi-Fi also has to be set to Private (Settings > Network & internet > Wi-Fi > your network). Then click **Open on phone** on the CodeQuest home page.

## Install (Linux and Mac)

Clone CodeQuest anywhere, then run the installer once:

```
git clone https://github.com/Evelynnsrepos/CodeQuest.git
cd CodeQuest
./install.sh
```

It copies CodeQuest to `~/.local/share/codequest`, adds a `codequest` command, and on Linux adds **CodeQuest** to your app launcher (wofi, rofi, hyprlauncher, ...). Running it again updates CodeQuest and keeps your progress. `./install.sh --uninstall` removes the command and launcher entry.

## Update

Pull the latest version in your clone, then run the installer again. Your progress is kept.

```
git pull
./install.sh        # Linux and Mac
install.bat         # Windows (or double-click it)
```

## Use it (Linux and Mac)

| Command | What it does |
| --- | --- |
| `codequest` | Starts CodeQuest in the background (if it isn't running) and opens it in your browser |
| `codequest phone` | Shows the address for your phone or tablet, with a QR code if `qrencode` is installed |
| `codequest stop` | Stops it |
| `codequest status` | Shows whether it's running, its addresses, and whether Godot, Rust, Nix and Git were found |
| `codequest autostart on` | Starts it every time you log in (systemd), so your phone can always connect |
| `codequest pin 4821` | Asks for a PIN before anyone can run code (`codequest pin off` removes it) |
| `codequest godot /path/to/godot` | Tells CodeQuest where Godot is |
| `codequest port 9000` | Uses another port |
| `codequest logs` | Shows the server log, useful if something goes wrong |
| `codequest run` | Runs it in the terminal instead (Ctrl+C stops it) |

Settings are saved in `~/.config/codequest/config.json`.

On Hyprland you can also give it a key, for example in `hyprland.lua`:

```lua
hl.bind(mainMod .. " + F1", hl.dsp.exec_cmd("codequest"))
```

### On your phone or tablet

1. Run `codequest phone` (or click **Open on phone** on the CodeQuest home page on your computer).
2. On the phone, connect to the same Wi-Fi and open the address, or scan the QR code.
3. In the phone's browser menu, choose **Add to Home Screen**. CodeQuest now has its own app icon and opens full screen.

The computer has to be on with CodeQuest running. `codequest autostart on` takes care of the running part.

Your progress (XP, streak, saved code) is stored on the computer, so it's the same on every device.

## Without installing

Double-click `start.bat` on Windows (it keeps a window open while it runs), or run `python3 server.py --open` from the `CodeQuest` folder on any system. It needs Python 3.9 or newer. Server options: `--pin 4821`, `--port 9000`, `--local-only` (only this computer can connect), `--godot PATH`, `--open`.

## GDScript, Rust, Nix and Git

Python, Lua and TypeScript run inside the browser. GDScript, Rust, Nix and Git lessons are sent to the host computer, which runs them, so it needs:

- **Godot 4** from [godotengine.org](https://godotengine.org/download) (tested with 4.5). Put it on your PATH as `godot`, copy the program into CodeQuest's `tools` folder (on Windows: `%LOCALAPPDATA%\CodeQuest\tools`), or use `codequest godot /path/to/Godot`. On a Mac that path is usually `/Applications/Godot.app/Contents/MacOS/Godot`. On Windows, point it at the `_console.exe` file that comes in the Godot download, because the other one doesn't report output.
- **Rust** from [rustup.rs](https://rustup.rs).
- **Nix** for the Nix courses. NixOS has it; elsewhere get it from [nixos.org/download](https://nixos.org/download). Lessons are only evaluated with `nix-instantiate --eval`, never built. There's no Nix for Windows itself, so on Windows these two courses only work inside WSL.
- **Git** from [git-scm.com](https://git-scm.com) (on NixOS: `pkgs.git`).

The home page tells you if either is missing. Each run has a 10-second limit so an endless loop can't hang the computer.

## Courses

| Course | Language | Runs in |
| --- | --- | --- |
| Python | Python | browser |
| GDScript | GDScript | host computer (Godot) |
| GDScript for game dev | GDScript | host computer (Godot) |
| Lua | Lua | browser |
| Lua for Hyprland | Lua | browser |
| TypeScript | TypeScript | browser |
| Rust | Rust | host computer |
| Git | Git commands | host computer |
| Nix | Nix | host computer (Nix) |
| Nix flakes | Nix | host computer (Nix) |
| LLMs 1: How an LLM works | Python | browser |
| LLMs 2: Running models locally | Python | browser |
| LLMs 3: Tools, MCP and agents | Python | browser |
| LLMs 4: Python and math for AI | Python | browser |
| LLMs 5: How training works | Python | browser |
| LLMs 6: Fine-tuning and its alternatives | Python | browser |
| LLMs 7: Capstone, your own model | Python | browser |
| LLMs 8: Build a GPT, scale it, make it reason | Python | browser |
| LLMs 9: Working with AI tools | Python | browser |
| AI beyond LLMs | Python | browser |
| Math 1: Reading math | Python | browser |
| Math 2: Linear algebra | Python | browser |
| Math 3: Calculus | Python | browser |
| Math 4: Probability and statistics | Python | browser |
| Math 5: Information theory and optimization | Python | browser |
| Math 6: Data geometry and testing | Python | browser |
| AI crash course | Python | browser |
| Data cleaning with Python | Python | browser |
| AI engineer 1: Real tools | Python (numpy, pandas, PyTorch) | host computer |
| AI engineer 2: Real RAG and evals | Python | host computer |
| AI engineer 3: Shipping AI apps | Python (FastAPI) | host computer |

**Lua for Hyprland** teaches the Lua config that Hyprland uses since version 0.55 (`~/.config/hypr/hyprland.lua`). Lessons run against a practice copy of Hyprland's `hl` API (`lessons/lua-hyprland/prelude.lua`) that records what your code sets and shows a summary, so nothing on your real desktop changes. If `hyprctl version` shows something older than 0.55, your Hyprland still uses `hyprland.conf`, which has a different syntax.

**LLMs 1: How an LLM works** is the first module of a local-AI course: tokens and BPE, weights, softmax, perplexity, the generation loop, temperature and top-p, chat templates, embeddings, attention and the context window. Each idea is built in a few lines of plain Python, and each lesson ends with review questions from earlier lessons. It needs only the Python basics. **LLMs 2** continues with safetensors and GGUF files, quantization, VRAM, KV cache and speed math, Mixture of Experts, AMD ROCm vs Vulkan, and LM Studio's OpenAI-compatible server. **LLMs 3** covers tool calling, the agent loop, MCP (JSON-RPC, stdio vs HTTP, writing a server), LM Studio's `mcp.json`, MCP security and a first RAG pipeline. **LLMs 4** is the math gate: classes, vectors, matrices, FLOPs, derivatives, gradients, the chain rule (including the softmax + cross-entropy gradient), probability, information theory and statistics for evaluations, ending with a script that calls LM Studio. **LLMs 5** builds training from scratch in the style of Karpathy's *Zero to Hero*: an autograd engine (micrograd), a neural network, batches and epochs, overfitting, AdamW and LR schedules, makemore-style character models, a causal attention head, training memory, and Hinton's Forward-Forward algorithm as a comparison. **LLMs 6** covers the training options: RAG vs fine-tuning, JSONL datasets and loss masking, LoRA and QLoRA math, hyperparameters, the Hugging Face stack, DPO, merging and GGUF conversion, and training on AMD or a rented GPU. **LLMs 7** is the capstone: plan a fine-tune, clean and split a dataset, budget tokens, read training logs, run a blind A/B evaluation with confidence intervals, check tool calling did not regress, and publish a model card, ending with a quiz on the reason behind every step. **LLMs 8** goes to university depth: every part of a GPT (multi-head attention, LayerNorm and RMSNorm, the MLP and residuals, RoPE, a full forward pass), parameter counts, the training recipe, Chinchilla scaling laws, pretraining data, multi-GPU training with ZeRO, and RLHF, PPO, GRPO and test-time compute. **AI beyond LLMs** covers the rest of the field: linear and logistic regression, decision trees, k-means, honest evaluation, RNNs, CNNs, vision transformers and CLIP, diffusion, speech and Whisper, multimodal LLMs and Q-learning. **LLMs 9** turns Evelynn's guide *AI on your computer* into practice: the four layers, context budgets and prompt caching, how Claude Code remembers (CLAUDE.md, auto memory), settings layers and permission rules, hooks, skills, prompt engineering, validated JSON output, prompt injection, headless automation with cron, and the math of speculative decoding, MoE routers and Mamba.

The **Math for AI** track (Math 1–6) assumes no math at all. Every lesson explains one idea in plain words and real numbers first, introduces each sign with how to say it and its Python equivalent, then takes the full formula apart with colour-coded pieces and shows what goes wrong if the formula were different. Math 1 covers arithmetic up to Σ, logs and e; Math 2 linear algebra up to attention and LoRA; Math 3 calculus up to backprop by hand; Math 4 probability and statistics up to Bayes, maximum likelihood and p-values; Math 5 entropy, cross-entropy, KL, log-sum-exp, Adam, floating point, quantization, contrastive loss and distillation; Math 6 covariance, PCA, SVD, Jacobians and t-tests. Math 1–5 each have a mixed practice set, and key lessons have drawings.

On the home page the AI and Math courses are grouped into **levels**. New to AI? Start with the **AI crash course** (11 short lessons, the whole picture in one evening), then Level 1 (LLMs 1–3), Level 2 (LLMs 4–7, AI beyond LLMs) and Level 3 (LLMs 8–9, AI engineer 1–3). **Data cleaning with Python** is its own course because it is useful far beyond training data.

The **AI engineer** courses use real packages (numpy, pandas, PyTorch, scikit-learn, FastAPI, pytest), so they run on your computer, not in the browser. Set them up once:

```
python3 -m venv ~/.codequest/ai-venv
~/.codequest/ai-venv/bin/pip install torch -r requirements-ai.txt
```

On Windows use `%USERPROFILE%\.codequest\ai-venv\Scripts\pip`. CodeQuest finds that venv by itself (or set `CODEQUEST_AI_PYTHON` to another Python). Lessons that talk to a model use Ollama or LM Studio when running and a built-in fake otherwise.

**Nix** and **Nix flakes** evaluate your code with `nix-instantiate`. The flakes course passes your `outputs` a practice nixpkgs (`lessons/nix-flakes/prelude.nix`), so nothing is downloaded or built, and Run shows the outputs your flake produces. The last lessons of both courses are about your own NixOS configuration.

**Git** lessons are a list of commands, one per line, run in a fresh practice repository every time. Only `git` plus `echo`, `cat`, `ls`, `mkdir`, `rm` and `cd` are allowed, and git uses a private practice config, so your real repositories and `~/.gitconfig` are never touched. A lesson can have a hidden `setup.sh` (same commands) that prepares the repository, for example with branches that conflict.

**TypeScript** lessons are checked by the real TypeScript compiler (5.9, `strict` mode) running in your browser, then the compiled JavaScript runs there too. A type error stops the run and shows the compiler's message, just like `tsc` would. Lessons have plain JavaScript plus `console`, but no browser page APIs such as `document`.

**GDScript for game dev** runs your script as a real node in a headless Godot scene: `_ready()` runs, and the checks call `_process(delta)`, press input actions and listen to your signals.

## Write your own lessons

Each folder in `lessons/` is a course, and each folder inside it is a lesson. Folders are shown in name order, so number them.

```
lessons/python/05-conditionals/
  lesson.md            # front matter (title, xp) + the lesson text in Markdown
  starter.py           # code the learner starts with
  solution.py          # optional; shown after the lesson is cleared
  expected_output.txt  # optional; the exact output the program must print
  check.py             # optional; extra checks (see below)
```

A course can have a `course.json`:

```json
{"lang": "lua", "name": "Lua for Hyprland", "icon": "🪟", "order": 35,
 "blurb": "Shown on the course card", "prelude": "prelude.lua"}
```

`lang` defaults to the folder name. `prelude` (Python and Lua courses) is hidden code that runs before the learner's code, for example a practice API. In Lua, a prelude can define `_cq_after()` to print a summary after the learner's code runs.

`lesson.md` starts like this:

```
---
title: Conditionals
xp: 15
---
# Lesson heading
...
```

Checks per language:

- **Python** `check.py`: plain `assert` statements. `ns` is a dict of the learner's variables and functions, and `output` is what they printed. The assert message is shown to the learner.
- **Lua** `check.lua`: `assert(condition, "message")` lines. The learner's global variables and functions are available directly, and `output` is what they printed. Ask learners to keep checked functions global (no `local`).
- **TypeScript** `check.js`: plain JavaScript with `assert(condition, "message")` lines. It runs in the same scope as the learner's code, so their top-level functions, classes, `const` and `let` are available directly. `output` is what they printed and `code` is their source text, for checking things that only exist in types (for example `/interface\s+Hero/.test(code)`). Starter and solution files end in `.ts`.
- **GDScript** `check.gd`: a script with `func check(player) -> String`. `player` is the learner's script object after `run()` was called. Return `""` to pass or a message to fail. The learner's code goes in `func run():`.
- **Rust** `tests.rs`: normal `#[test]` functions. They are placed in a test module next to the learner's code, so they can call its functions directly.
- **Nix** `check.nix`: a function `{ result, prelude, expect }: [ (expect condition "message") ... ]`. `result` is the learner's value and `prelude` the course prelude, if any. Checks run in order and the first failing message is shown. Starter, solution and check files end in `.nix`.
- **Git** `check.py`: Python `assert` statements, run after the learner's commands. `git("log", "-1", "--format=%s")` returns git's output, `read(path)` a file's text, `exists(path)` whether it exists, and `output` the whole transcript. Starter and solution files end in `.sh`; `setup.sh` is optional.

## Troubleshooting

- **Phone can't connect:** make sure both devices are on the same Wi-Fi (not a guest network), and allow Python through your computer's firewall when asked. On Windows choose "Private networks".
- **Python lesson is slow the first time:** the browser downloads Python once (about 13 MB), then caches it. Lua is much smaller (under 1 MB), and TypeScript is about 4 MB.
- **Start over:** run `codequest stop`, then delete `~/.local/share/codequest/data/progress.db` (or `data/progress.db` in the folder you run it from).

## What's inside

- `codequest`: the command that starts, stops and opens CodeQuest. `install.sh` installs it.
- `server.py`: the web server, progress database and GDScript, Rust, Nix and Git runners (Python standard library only).
- `static/`: the web page.
- `runners/runner.gd`: loads the learner's GDScript inside headless Godot.
- `vendor/`: Pyodide, wasmoon (Lua), the TypeScript compiler, CodeMirror, marked and a QR code library, bundled so the app works without internet. See `vendor/LICENSES.md`.
