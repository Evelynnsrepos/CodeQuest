---
title: Ignoring files
xp: 15
---
# .gitignore

Some files should never be committed: passwords and keys, build output, editor junk. List them in a file called `.gitignore` and git acts as if they aren't there:

```
secret.env
build/
*.log
```

- a name ignores that file
- a name ending in `/` ignores a whole folder
- `*` matches anything, so `*.log` ignores every log file

Commit the `.gitignore` itself so everyone working on the project ignores the same things. `git add .` stages everything in the folder, except what's ignored.

Your code here is a list of terminal commands, one per line. Each run starts over in a fresh practice folder, so you can run as often as you like. Besides `git` you can use `echo`, `cat`, `ls`, `mkdir`, `rm` and `cd`, and `echo "text" > file` writes a file (`>>` adds to the end).

## Your quest

This repository has `app.py`, a `secret.env` with a password, a `build/` folder and a `debug.log`. Write a `.gitignore` that ignores `secret.env`, `build/` and every `.log` file, then stage everything with `git add .` and commit with the message `Add app`.
