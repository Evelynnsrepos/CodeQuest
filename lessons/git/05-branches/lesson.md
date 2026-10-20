---
title: Branches
xp: 20
---
# Working on a branch

A **branch** is a separate line of commits. You make one to try something without touching `main`, and switch between them whenever you like. Git swaps the files in the folder to match.

```sh
git switch -c feature   # create a branch called feature and switch to it
git branch              # list branches; * marks the one you're on
git switch main         # go back to main
```

Commits you make go on the branch you're on.

Your code here is a list of terminal commands, one per line. Each run starts over in a fresh practice folder, so you can run as often as you like. Besides `git` you can use `echo`, `cat`, `ls`, `mkdir`, `rm` and `cd`, and `echo "text" > file` writes a file (`>>` adds to the end).

## Your quest

1. Create a branch called `dark-mode` and switch to it
2. Write `theme = dark` into `theme.txt` and commit it with the message `Add dark mode`
3. Switch back to `main`

`main` should not have the new commit, and `theme.txt` disappears from the folder when you switch back. That's expected: it lives on `dark-mode`.
