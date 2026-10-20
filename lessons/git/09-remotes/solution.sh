git log --oneline

# 1. Add the remote
git remote add origin ../server.git

# 2. Push main
git push -u origin main

# 3. Clone it into ../laptop and look at the log
git clone ../server.git ../laptop
cd ../laptop
git log --oneline
