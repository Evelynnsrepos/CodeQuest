---
title: Reverting a commit
xp: 20
---
# Undoing a commit that's already shared

`git revert <commit>` makes a **new commit** that does the opposite of an old one. History stays intact, which is what you want once others have your commits. (Rewriting history with `git reset` is fine only for commits nobody else has yet.)

You can name commits in several ways:

- the short hash that `git log --oneline` shows, like `a1b2c3d`
- `HEAD` for the latest commit, `HEAD~1` for the one before it, `HEAD~2` for the one before that

`git show HEAD` shows what a commit changed, and `git revert --no-edit` keeps git's ready-made message.

Your code here is a list of terminal commands, one per line. Each run starts over in a fresh practice folder, so you can run as often as you like. Besides `git` you can use `echo`, `cat`, `ls`, `mkdir`, `rm` and `cd`, and `echo "text" > file` writes a file (`>>` adds to the end).

## Your quest

Someone committed `Set speed to 9000` (in `game.txt`), which broke the game, and then a good commit changed `player.txt`. Revert **only** the broken commit and keep the good one.
