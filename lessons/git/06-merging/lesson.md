---
title: Merging
xp: 20
---
# Bringing a branch back

When the work on a branch is done, you **merge** it into `main`. Switch to the branch you want to bring changes *into*, then merge the other one:

```sh
git switch main
git merge feature
```

If `main` hasn't changed since the branch was made, git simply moves `main` forward ("fast-forward"). Afterwards the branch isn't needed any more:

```sh
git branch -d feature
```

`-d` refuses to delete a branch that isn't merged yet, so it's a safe way to tidy up.

`git log --oneline --graph --all` draws every branch, which helps you see what's going on.

Your code here is a list of terminal commands, one per line. Each run starts over in a fresh practice folder, so you can run as often as you like. Besides `git` you can use `echo`, `cat`, `ls`, `mkdir`, `rm` and `cd`, and `echo "text" > file` writes a file (`>>` adds to the end).

## Your quest

This repository has a `login-page` branch with two commits. Merge it into `main`, then delete the `login-page` branch.
