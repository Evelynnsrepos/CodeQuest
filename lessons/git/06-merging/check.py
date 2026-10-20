assert git("branch", "--show-current") == "main", "Finish on main."
subjects = git("log", "--format=%s", "main").splitlines()
assert "Add login form" in subjects and "Add login button" in subjects, "main doesn't have the login-page commits yet. Run git merge login-page on main."
assert exists("login.html"), "login.html should be in the folder after the merge."
assert not git("rev-parse", "--verify", "-q", "refs/heads/login-page"), "Delete the branch afterwards: git branch -d login-page"
