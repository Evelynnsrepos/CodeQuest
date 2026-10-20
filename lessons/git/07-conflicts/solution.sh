git merge friendly
cat greeting.txt

# Fix greeting.txt, mark it solved and finish the merge
echo "Hello there, friend!" > greeting.txt
git add greeting.txt
git commit --no-edit

git log --oneline --graph
