def matches(rule, tool, command):
    return False


def decide(tool, command, rules):
    return "allow"


def effective(key, layers):
    return None


rules = {"deny": ["Bash(git push *)"], "allow": ["Bash(git *)"]}
print(decide("Bash", "git status", rules), decide("Bash", "git push origin main", rules), decide("Bash", "npm install", rules))
