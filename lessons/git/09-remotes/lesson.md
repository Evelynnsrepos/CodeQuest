---
title: Pushing and cloning
xp: 25
---
# Sharing your repository

A **remote** is another copy of the repository, usually on a server like GitHub. You give it a name (by convention `origin`), then **push** your commits to it:

```sh
git remote add origin https://github.com/you/project.git
git push -u origin main   # -u remembers origin/main, so next time plain git push works
```

Someone else (or you, on another computer) gets a copy with `git clone`, and later fetches new commits with `git pull`.

Here, a practice "server" repository sits next to your project at `../server.git`, so you can use that path instead of a GitHub URL.

Your code here is a list of terminal commands, one per line. Each run starts over in a fresh practice folder, so you can run as often as you like. Besides `git` you can use `echo`, `cat`, `ls`, `mkdir`, `rm` and `cd`, and `echo "text" > file` writes a file (`>>` adds to the end).

## Your quest

1. Add `../server.git` as the remote `origin`
2. Push `main` to it with `-u`
3. Clone it into `../laptop`, `cd` into it and run `git log --oneline` to see your commits arrived
