---
title: Undoing changes
xp: 20
---
# git restore

Made a mess? Two commands get you back:

- `git restore file` throws away the changes to a file and brings back the last committed version. Careful: those changes are gone for good.
- `git restore --staged file` takes a file **out of the staging area** but keeps your changes in the file.

`git status` tells you which one you need: it even prints the command.

Your code here is a list of terminal commands, one per line. Each run starts over in a fresh practice folder, so you can run as often as you like. Besides `git` you can use `echo`, `cat`, `ls`, `mkdir`, `rm` and `cd`, and `echo "text" > file` writes a file (`>>` adds to the end).

## Your quest

The starter breaks `config.txt` and stages a scratch file by mistake.

1. Bring back the committed version of `config.txt`
2. Unstage `scratch.txt`, but keep the file

At the end, `git status` should show only `scratch.txt` as untracked.
