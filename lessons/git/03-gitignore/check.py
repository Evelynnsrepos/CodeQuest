files = git("ls-tree", "-r", "--name-only", "HEAD").splitlines() if git("rev-parse", "--verify", "-q", "HEAD") else []
assert files, 'Make a commit with the message "Add app".'
assert "secret.env" not in files, "secret.env was committed! Add secret.env to .gitignore before git add ."
assert not any(f.startswith("build/") for f in files), "The build folder was committed. Add build/ to .gitignore."
assert "debug.log" not in files, "debug.log was committed. Add *.log to .gitignore."
assert ".gitignore" in files, "Commit the .gitignore file too."
assert "app.py" in files, "app.py should be in the commit."
assert git("log", "-1", "--format=%s") == "Add app", 'The commit message should be "Add app".'
