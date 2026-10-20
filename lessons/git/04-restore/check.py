assert read("config.txt").strip() == "volume = 7", "config.txt still has your change. Use git restore config.txt"
assert exists("scratch.txt"), "scratch.txt is gone. Unstage it with git restore --staged so the file stays."
status = git("status", "--porcelain")
assert "A  scratch.txt" not in status, "scratch.txt is still staged. Use git restore --staged scratch.txt"
assert status == "?? scratch.txt", "Only scratch.txt should show in git status, as untracked."
assert git("rev-list", "--count", "HEAD") == "1", "No new commits are needed in this lesson."
