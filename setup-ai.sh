#!/usr/bin/env bash
# One command to set up the Python that the "AI engineer" courses use: ~/.codequest/ai-venv
# Linux: a virtual environment with CPU PyTorch. NixOS: a Nix-built Python with the same packages.
set -euo pipefail
cd "$(dirname "$0")"
target="$HOME/.codequest/ai-venv"
mkdir -p "$HOME/.codequest"

if [ -e /etc/NIXOS ] && command -v nix >/dev/null; then
  echo "NixOS found: building a Python with the AI packages (the first time takes a while)..."
  rm -rf "$target"
  nix --extra-experimental-features "nix-command flakes" build --impure -o "$target" --expr '
    (builtins.getFlake "nixpkgs").legacyPackages.${builtins.currentSystem}.python3.withPackages (ps: with ps; [
      torch numpy pandas scikit-learn fastapi httpx pydantic pytest uvicorn pyyaml ])'
else
  python=$(command -v python3.12 || command -v python3)
  echo "Making a virtual environment with $python ..."
  "$python" -m venv "$target"
  "$target/bin/python" -m pip install --upgrade pip
  "$target/bin/python" -m pip install torch --index-url https://download.pytorch.org/whl/cpu
  "$target/bin/python" -m pip install -r requirements-ai.txt
fi

"$target/bin/python" -c "import numpy, pandas, torch, sklearn, fastapi; print('All AI packages work. Press Run in AI engineer 1, lesson 01.')"
