#!/bin/sh
# Installs CodeQuest for your user: the codequest command and an app-launcher entry.
# Run it again to update; your progress is kept. Remove with: ./install.sh --uninstall
set -e

SRC="$(cd "$(dirname "$0")" && pwd)"
DATA_HOME="${XDG_DATA_HOME:-$HOME/.local/share}"
DEST="$DATA_HOME/codequest"
BIN="$HOME/.local/bin"
DESKTOP="$DATA_HOME/applications/codequest.desktop"

if [ "$1" = "--uninstall" ]; then
    "$DEST/codequest" autostart off >/dev/null 2>&1 || true
    "$DEST/codequest" stop >/dev/null 2>&1 || true
    rm -f "$BIN/codequest" "$DESKTOP"
    echo "Removed the codequest command and launcher entry."
    echo "Your progress is still in $DEST/data. Delete $DEST to remove everything."
    exit 0
fi

if ! command -v python3 >/dev/null 2>&1; then
    echo "CodeQuest needs Python 3. Install it with your package manager first."
    exit 1
fi

# Stop an old copy so the update takes effect.
[ -x "$DEST/codequest" ] && "$DEST/codequest" stop >/dev/null 2>&1 || true

mkdir -p "$DEST" "$BIN"
if [ "$SRC" != "$DEST" ]; then
    # Copy everything except progress data, so updating never loses your XP.
    (cd "$SRC" && tar --exclude=./data --exclude=__pycache__ -cf - .) | (cd "$DEST" && tar -xf -)
fi
chmod +x "$DEST/codequest" "$DEST/start.sh"
ln -sf "$DEST/codequest" "$BIN/codequest"

if [ "$(uname)" = "Linux" ]; then
    mkdir -p "$(dirname "$DESKTOP")"
    cat > "$DESKTOP" <<DESKTOP_ENTRY
[Desktop Entry]
Type=Application
Name=CodeQuest
Comment=Learn Python, GDScript, Lua, Rust, Nix and Git
Exec=$DEST/codequest open
Icon=$DEST/static/icon-512.png
Terminal=false
Categories=Education;Development;
DESKTOP_ENTRY
    command -v update-desktop-database >/dev/null 2>&1 && update-desktop-database "$(dirname "$DESKTOP")" >/dev/null 2>&1 || true
fi

echo
echo "CodeQuest is installed."
echo
echo "  Open it:              codequest     (or 'CodeQuest' in your app launcher)"
echo "  Phone or tablet:      codequest phone"
echo "  Stop it:              codequest stop"
echo "  Start at every login: codequest autostart on"
echo "  All commands:         codequest help"
echo
case ":$PATH:" in
    *":$BIN:"*) ;;
    *) echo "Note: $BIN isn't on your PATH yet, so 'codequest' won't be found."
       echo "Add this line to your shell config (~/.bashrc, ~/.zshrc, ...):"
       echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
       echo ;;
esac
command -v godot >/dev/null 2>&1 || command -v godot4 >/dev/null 2>&1 || \
    echo "Godot wasn't found, so GDScript lessons won't run yet. Install Godot 4, then: codequest godot /path/to/godot"
command -v rustc >/dev/null 2>&1 || [ -x "$HOME/.cargo/bin/rustc" ] || \
    echo "Rust wasn't found, so Rust lessons won't run yet. Install it from https://rustup.rs"
command -v nix-instantiate >/dev/null 2>&1 || \
    echo "Nix wasn't found, so Nix lessons won't run. Install it from https://nixos.org/download"
command -v git >/dev/null 2>&1 || \
    echo "Git wasn't found, so Git lessons won't run. Install it with your package manager."
