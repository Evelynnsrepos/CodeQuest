---
title: Your first commit
xp: 15
---
# Saving a snapshot

Git keeps the history of a folder. Every **commit** is a snapshot of your files with a message saying what changed, so you can always look back or undo.

Your code here is a list of terminal commands, one per line. Each run starts over in a fresh practice folder, so you can run as often as you like. Besides `git` you can use `echo`, `cat`, `ls`, `mkdir`, `rm` and `cd`, and `echo "text" > file` writes a file (`>>` adds to the end).

Before your first commit, git needs to know who you are. On your own computer you do this once:

```sh
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

(Here it only changes CodeQuest's practice settings.)

Then a commit takes three steps:

```sh
git init                        # make this folder a repository (once)
git add README.md               # stage: choose what goes in the next commit
git commit -m "First commit"    # save the snapshot with a message
```

`git log --oneline` lists the commits.

## Your quest

1. Set your `user.name` and `user.email` with `git config --global`
2. Turn the folder into a repository
3. Commit `README.md` with the message `First commit`
