ps, pk = ns.get("parse_skill"), ns.get("pick_skill")
assert ps and pk, "Keep parse_skill and pick_skill."
doc = "---\nname: new-lesson\ndescription: Add a lesson: lesson.md and check.py\n---\n1. Copy a folder\n2. Test"
r = ps(doc)
assert r.get("name") == "new-lesson" and r.get("description") == "Add a lesson: lesson.md and check.py", f"Frontmatter parsed wrong: {r!r} (split on the FIRST colon only)."
assert r.get("body") == "1. Copy a folder\n2. Test", f"body should be everything after the closing ---, got {r.get('body')!r}."
assert ps("\n---\nname: x\n---\nhi") == {"body": "\n---\nname: x\n---\nhi"}, "Frontmatter must start on the first line."
sk = {"deploy": "Deploy the server to production", "new-lesson": "Add a CodeQuest lesson folder", "nix": "Edit the NixOS flake"}
assert pk(sk, "add a lesson about entropy") == "new-lesson", "Most shared words wins."
assert pk(sk, "update my NixOS flake please") == "nix"
assert pk(sk, "bake cookies") is None, "No shared word → None."
