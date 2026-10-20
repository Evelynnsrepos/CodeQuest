assert git("remote", "get-url", "origin") == "../server.git", "Add the remote: git remote add origin ../server.git"
head = git("rev-parse", "HEAD")
assert git("--git-dir=../server.git", "rev-parse", "--verify", "-q", "refs/heads/main") == head, "server.git doesn't have your main yet. git push -u origin main"
assert git("rev-parse", "--abbrev-ref", "main@{upstream}") == "origin/main", "Push with -u so main tracks origin/main."
assert exists("../laptop/.git"), "Clone it: git clone ../server.git ../laptop"
assert git("-C", "../laptop", "rev-parse", "HEAD") == head, "The laptop clone should have the same commits."
after_cd = output.split("$ cd ../laptop", 1)
assert len(after_cd) == 2 and "$ git log" in after_cd[1], "cd ../laptop and run git log --oneline there."
