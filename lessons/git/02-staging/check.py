assert git("rev-list", "--count", "HEAD") == "2", "Make one new commit."
assert git("log", "-1", "--format=%s") == "Add notes", 'The new commit message should be "Add notes".'
changed = git("show", "--name-only", "--format=", "HEAD").split()
assert changed == ["notes.txt"], "The commit should contain only notes.txt. Stage just that file: git add notes.txt"
assert "Remember to drink water" in git("show", "HEAD:notes.txt"), "Commit the new line in notes.txt."
assert git("status", "--porcelain") == "M todo.txt", "todo.txt should still be changed but not committed."
