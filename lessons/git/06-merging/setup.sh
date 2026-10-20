git init
echo "<h1>Home</h1>" > index.html
git add index.html
git commit -m "Add home page"
git switch -c login-page
echo "<form>login</form>" > login.html
git add login.html
git commit -m "Add login form"
echo "<button>Log in</button>" >> login.html
git commit -am "Add login button"
git switch main
