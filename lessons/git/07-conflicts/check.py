text = read("greeting.txt")
assert "<<<<<<<" not in text and ">>>>>>>" not in text and "=======" not in text, "greeting.txt still has conflict markers. Write the solved text into it."
assert text.strip() == "Hello there, friend!", "greeting.txt should contain just: Hello there, friend!"
assert not exists(".git/MERGE_HEAD"), "The merge isn't finished yet. git add greeting.txt, then git commit --no-edit"
parents = git("log", "-1", "--format=%P").split()
assert len(parents) == 2, "Finish with a merge commit: git merge friendly, solve, git add, git commit."
assert git("show", "HEAD:greeting.txt").strip() == "Hello there, friend!", "Commit the solved greeting.txt."
assert git("status", "--porcelain") == "", "Everything should be committed at the end."
