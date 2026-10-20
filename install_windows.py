"""Installs CodeQuest on Windows. install.bat runs this; you don't need to run it yourself.

It copies CodeQuest to %LOCALAPPDATA%\\CodeQuest, adds Start menu and desktop shortcuts,
and can start CodeQuest when you log in. Run install.bat again to update (your progress
is kept). Uninstall from the Start menu: CodeQuest > Uninstall CodeQuest.
"""

import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEST = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local")) / "CodeQuest"
NO_WINDOW = 0x08000000


def ps(script):
    """Run a short PowerShell snippet and return its output."""
    result = subprocess.run(
        ["powershell", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-Command", script],
        capture_output=True, text=True, creationflags=NO_WINDOW,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "PowerShell failed")
    return result.stdout.strip()


def special_folder(name):
    """Desktop, Programs (Start menu) or Startup, following OneDrive redirection."""
    return Path(ps(f"[Environment]::GetFolderPath('{name}')"))


def quote_ps(text):
    return "'" + str(text).replace("'", "''") + "'"


def make_shortcut(path, target, arguments="", icon=None, workdir=None, description=""):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "$s = (New-Object -ComObject WScript.Shell).CreateShortcut(" + quote_ps(path) + ")",
        "$s.TargetPath = " + quote_ps(target),
        "$s.Arguments = " + quote_ps(arguments),
        "$s.WorkingDirectory = " + quote_ps(workdir or Path(target).parent),
        "$s.Description = " + quote_ps(description),
    ]
    if icon:
        lines.append("$s.IconLocation = " + quote_ps(f"{icon},0"))
    lines.append("$s.Save()")
    ps("; ".join(lines))


def pythonw():
    """pythonw.exe runs CodeQuest without a console window."""
    candidate = Path(sys.executable).with_name("pythonw.exe")
    return candidate if candidate.exists() else Path(sys.executable)


def launcher_args(command):
    return f'"{DEST / "codequest"}" {command}'


def startup_shortcut():
    return special_folder("Startup") / "CodeQuest.lnk"


def set_autostart(on):
    link = startup_shortcut()
    if on:
        make_shortcut(link, pythonw(), launcher_args("start"), icon=DEST / "static" / "icon.ico",
                      workdir=DEST, description="Start CodeQuest in the background")
    elif link.exists():
        link.unlink()


def ask(question, default=True):
    hint = "[Y/n]" if default else "[y/N]"
    try:
        answer = input(f"{question} {hint} ").strip().lower()
    except EOFError:
        return default
    return default if not answer else answer.startswith("y")


def run_launcher(command, wait=True):
    script = DEST / "codequest"
    if not script.exists():
        return
    if wait:
        subprocess.run([sys.executable, str(script), command], capture_output=True, creationflags=NO_WINDOW)
    else:
        subprocess.Popen([str(pythonw()), str(script), command], creationflags=NO_WINDOW, cwd=DEST)


def install():
    print("\nInstalling CodeQuest...\n")
    run_launcher("stop")  # an older copy may be running

    DEST.mkdir(parents=True, exist_ok=True)
    if HERE != DEST:
        shutil.copytree(HERE, DEST, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns("data", "__pycache__"))

    icon = DEST / "static" / "icon.ico"
    programs = special_folder("Programs") / "CodeQuest"
    make_shortcut(programs / "CodeQuest.lnk", pythonw(), launcher_args("open"), icon=icon, workdir=DEST,
                  description="Learn Python, GDScript, Lua and Rust")
    make_shortcut(programs / "Stop CodeQuest.lnk", pythonw(), launcher_args("stop"), icon=icon, workdir=DEST,
                  description="Stop CodeQuest")
    make_shortcut(programs / "Uninstall CodeQuest.lnk", Path(sys.executable),
                  f'"{DEST / "install_windows.py"}" --uninstall', workdir=DEST, description="Remove CodeQuest")
    make_shortcut(special_folder("Desktop") / "CodeQuest.lnk", pythonw(), launcher_args("open"), icon=icon,
                  workdir=DEST, description="Learn Python, GDScript, Lua and Rust")

    print("  Installed to       ", DEST)
    print("  Added shortcuts    Start menu > CodeQuest, and on your desktop\n")

    autostart = ask("Start CodeQuest automatically when you log in, so your phone can always connect?")
    set_autostart(autostart)
    print("  Autostart is", "on." if autostart else "off.", "\n")

    print("Using it on your phone or tablet:")
    print("  1. Open CodeQuest on this PC and click 'Open on phone' to see the address and a QR code.")
    print("  2. The first time, Windows asks whether Python may use the network.")
    print("     Tick 'Private networks' and click Allow.")
    print("  3. Your Wi-Fi must be set to Private: Settings > Network & internet > Wi-Fi >")
    print("     your network > Private network. On a Public network your phone can't connect.\n")

    tools = DEST / "tools"
    tools.mkdir(exist_ok=True)
    print("Optional, for the GDScript, Rust and Git lessons (Python and Lua work right away):")
    print("  Godot: download Godot 4 from https://godotengine.org/download, unzip it and copy the")
    print(f"         Godot_..._console.exe file into {tools}")
    if shutil.which("rustc") or (Path.home() / ".cargo" / "bin" / "rustc.exe").exists():
        print("  Rust:  found.")
    else:
        print("  Rust:  install it from https://rustup.rs (it also asks to install the Visual Studio")
        print("         C++ build tools, which Rust needs on Windows).")
    git_found = shutil.which("git") or (Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "Git" / "cmd" / "git.exe").exists()
    print("  Git:   found." if git_found else "  Git:   install it from https://git-scm.com/download/win")
    print("  (The Nix courses need Nix, which only runs on Linux and Mac, or in WSL.)")
    print("  Then restart CodeQuest: Start menu > CodeQuest > Stop CodeQuest, then open it again.\n")

    if ask("Open CodeQuest now?"):
        run_launcher("open", wait=False)
        time.sleep(1)
    print("Done. You can close this window.")


def uninstall():
    print("\nRemoving CodeQuest...\n")
    run_launcher("stop")
    for link in (special_folder("Desktop") / "CodeQuest.lnk", startup_shortcut()):
        if link.exists():
            link.unlink()
    shutil.rmtree(special_folder("Programs") / "CodeQuest", ignore_errors=True)
    print("Removed the shortcuts and autostart.")
    if ask("Also delete CodeQuest and your progress (XP, saved code)?", default=False):
        # This script lives inside DEST, so delete everything else and leave a tiny folder behind.
        for item in DEST.iterdir():
            if item.name == "install_windows.py":
                continue
            shutil.rmtree(item, ignore_errors=True) if item.is_dir() else item.unlink(missing_ok=True)
        print(f"Deleted. You can remove the empty folder {DEST} yourself.")
    else:
        print(f"Your progress is still in {DEST / 'data'}.")


def main():
    if os.name != "nt":
        print("This installer is for Windows. On Linux or Mac, run ./install.sh instead.")
        sys.exit(1)
    if "WindowsApps" in sys.executable:
        print("This is the Microsoft Store version of Python, which can't create CodeQuest's shortcuts.")
        print("Install Python from https://www.python.org/downloads/ and run install.bat again.")
        input("\nPress Enter to close.")
        sys.exit(1)
    try:
        uninstall() if "--uninstall" in sys.argv else install()
    except Exception as exc:  # show a readable message instead of a traceback
        print(f"\nSomething went wrong: {exc}")
        print("Please send a screenshot of this window.")
    if "--uninstall" in sys.argv:
        input("\nPress Enter to close.")


if __name__ == "__main__":
    main()
