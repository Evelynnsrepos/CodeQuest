---
title: Merge conflicts
xp: 25
---
# When two branches change the same line

If `main` and a branch both changed the same line, git can't know which one you want. The merge stops with a **conflict** and writes both versions into the file:

```
<<<<<<< HEAD
Hello, world!
=======
Hi there!
>>>>>>> friendly
```

The part above `=======` is yours (`HEAD`, the branch you're on), the part below comes from the branch you're merging. To fix it:

1. Edit the file so it says what it should, without the `<<<<<<<`, `=======` and `>>>>>>>` lines
2. `git add` the file to mark it as solved
3. `git commit` to finish the merge (git already has a message ready, so `git commit --no-edit` uses it)

`git merge --abort` gives up and puts everything back as it was before the merge.

Your code here is a list of terminal commands, one per line. Each run starts over in a fresh practice folder, so you can run as often as you like. Besides `git` you can use `echo`, `cat`, `ls`, `mkdir`, `rm` and `cd`, and `echo "text" > file` writes a file (`>>` adds to the end).

## Your quest

Merge the `friendly` branch into `main`. It conflicts in `greeting.txt`. Solve it so the file contains just the line `Hello there, friend!`, then finish the merge.
