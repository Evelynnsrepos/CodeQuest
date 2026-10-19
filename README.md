# CodeQuest

A self-hosted, game-style coding course in the spirit of Boot.dev. It teaches **Python**, **GDScript** (Godot), **Lua** and **Rust** with hands-on lessons, XP, levels and daily streaks. You run it on your computer and open it in any browser, including your phone or tablet on the same Wi-Fi.

## Install on Windows

1. Right-click `codequest.zip` and choose **Extract All**. (Don't run it from inside the zip.)
2. Open the extracted `codequest` folder and double-click **install.bat**. If Windows shows "Windows protected your PC", click **More info**, then **Run anyway**.
3. If Python isn't installed, it offers to install it. Say yes, then double-click `install.bat` again.
4. Answer the two questions (start automatically at login, open now).

Afterwards, open **CodeQuest** from the Start menu or the desktop icon. It runs quietly in the background, with no window to keep open. To stop it, use **Start menu > CodeQuest > Stop CodeQuest**. To remove it, use **Uninstall CodeQuest** in the same place. Running `install.bat` again updates CodeQuest and keeps your progress.

For your phone or tablet: when Windows asks whether Python may use the network, tick **Private networks** and click **Allow**. Your Wi-Fi also has to be set to Private (Settings > Network & internet > Wi-Fi > your network). Then click **Open on phone** on the CodeQuest home page.

## Install (Linux and Mac)

Unzip CodeQuest anywhere, then run the installer once:

```
cd codequest
./install.sh
```

It copies CodeQuest to `~/.local/share/codequest`, adds a `codequest` command, and on Linux adds **CodeQuest** to your app launcher (wofi, rofi, hyprlauncher, ...). Running it again updates CodeQuest and keeps your progress. `./install.sh --uninstall` removes the command and launcher entry.

## Use it (Linux and Mac)

| Command | What it does |
| --- | --- |
| `codequest` | Starts CodeQuest in the background (if it isn't running) and opens it in your browser |
| `codequest phone` | Shows the address for your phone or tablet, with a QR code if `qrencode` is installed |
| `codequest stop` | Stops it |
| `codequest status` | Shows whether it's running, its addresses, and whether Godot and Rust were found |
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

Double-click `start.bat` on Windows (it keeps a window open while it runs), or run `python3 server.py --open` from the `codequest` folder on any system. It needs Python 3.9 or newer. Server options: `--pin 4821`, `--port 9000`, `--local-only` (only this computer can connect), `--godot PATH`, `--open`.

## GDScript and Rust

Python and Lua run inside the browser. GDScript and Rust lessons are sent to the host computer, which compiles and runs them, so it needs:

- **Godot 4** from [godotengine.org](https://godotengine.org/download) (tested with 4.5). Put it on your PATH as `godot`, copy the program into CodeQuest's `tools` folder (on Windows: `%LOCALAPPDATA%\CodeQuest\tools`), or use `codequest godot /path/to/Godot`. On a Mac that path is usually `/Applications/Godot.app/Contents/MacOS/Godot`. On Windows, point it at the `_console.exe` file that comes in the Godot download, because the other one doesn't report output.
- **Rust** from [rustup.rs](https://rustup.rs).

The home page tells you if either is missing. Each run has a 10-second limit so an endless loop can't hang the computer.

## Courses

| Course | Language | Runs in |
| --- | --- | --- |
| Python | Python | browser |
| GDScript | GDScript | host computer (Godot) |
| GDScript for game dev | GDScript | host computer (Godot) |
| Lua | Lua | browser |
| Lua for Hyprland | Lua | browser |
| Rust | Rust | host computer |

**Lua for Hyprland** teaches the Lua config that Hyprland uses since version 0.55 (`~/.config/hypr/hyprland.lua`). Lessons run against a practice copy of Hyprland's `hl` API (`lessons/lua-hyprland/prelude.lua`) that records what your code sets and shows a summary, so nothing on your real desktop changes. If `hyprctl version` shows something older than 0.55, your Hyprland still uses `hyprland.conf`, which has a different syntax.

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
- **GDScript** `check.gd`: a script with `func check(player) -> String`. `player` is the learner's script object after `run()` was called. Return `""` to pass or a message to fail. The learner's code goes in `func run():`.
- **Rust** `tests.rs`: normal `#[test]` functions. They are placed in a test module next to the learner's code, so they can call its functions directly.

## Troubleshooting

- **Phone can't connect:** make sure both devices are on the same Wi-Fi (not a guest network), and allow Python through your computer's firewall when asked. On Windows choose "Private networks".
- **Python lesson is slow the first time:** the browser downloads Python once (about 13 MB), then caches it. Lua is much smaller (under 1 MB).
- **Start over:** run `codequest stop`, then delete `~/.local/share/codequest/data/progress.db` (or `data/progress.db` in the folder you run it from).

## What's inside

- `codequest`: the command that starts, stops and opens CodeQuest. `install.sh` installs it.
- `server.py`: the web server, progress database and GDScript/Rust runners (Python standard library only).
- `static/`: the web page.
- `runners/runner.gd`: loads the learner's GDScript inside headless Godot.
- `vendor/`: Pyodide, wasmoon (Lua), CodeMirror, marked and a QR code library, bundled so the app works without internet. See `vendor/LICENSES.md`.
