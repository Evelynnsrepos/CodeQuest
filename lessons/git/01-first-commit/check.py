assert exists(".git"), "This folder isn't a repository yet. Run git init."
assert git("config", "user.name") not in ("", "CodeQuest Learner"), 'Set your name: git config --global user.name "Your Name"'
assert git("config", "user.email") not in ("", "learner@codequest.local"), 'Set your email: git config --global user.email "you@example.com"'
assert git("rev-list", "--count", "--all") == "1", "There should be exactly one commit. Did you run git commit?"
assert git("log", "-1", "--format=%s") == "First commit", 'The commit message should be "First commit".'
assert "README.md" in git("ls-tree", "--name-only", "HEAD").splitlines(), "README.md should be in the commit. Stage it with git add."
