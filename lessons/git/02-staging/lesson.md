---
title: The staging area
xp: 15
---
# Choosing what goes in a commit

Between your files and a commit sits the **staging area**. `git add` puts a change there; `git commit` saves only what's staged. That lets you make several changes but commit them separately, each with its own message.

- `git status` shows what's changed, what's staged and what git doesn't track yet
- `git diff` shows changes you haven't staged
- `git diff --staged` shows what the next commit will contain

Your code here is a list of terminal commands, one per line. Each run starts over in a fresh practice folder, so you can run as often as you like. Besides `git` you can use `echo`, `cat`, `ls`, `mkdir`, `rm` and `cd`, and `echo "text" > file` writes a file (`>>` adds to the end).

This practice repository already has a commit with `notes.txt` and `todo.txt`.

## Your quest

The starter changes both files. Commit **only** `notes.txt`, with the message `Add notes`, and leave the change to `todo.txt` uncommitted. Look at `git status` before and after.
