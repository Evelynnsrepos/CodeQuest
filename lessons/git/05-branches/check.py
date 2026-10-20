assert git("rev-parse", "--verify", "-q", "refs/heads/dark-mode"), "There's no dark-mode branch yet. Use git switch -c dark-mode"
assert git("log", "-1", "--format=%s", "dark-mode") == "Add dark mode", 'dark-mode should have a commit "Add dark mode".'
assert git("show", "dark-mode:theme.txt").strip() == "theme = dark", "theme.txt on dark-mode should say: theme = dark"
assert git("branch", "--show-current") == "main", "Switch back to main at the end: git switch main"
assert git("rev-list", "--count", "main") == "1", "main shouldn't have the new commit. Make it while you're on dark-mode."
