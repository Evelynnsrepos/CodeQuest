f = ns.get("setup_problems")
assert f, "Define a function called setup_problems."
good = {"base_url": "http://host.docker.internal:1234/v1", "n8n_in_docker": True, "use_responses_api": False, "model": "google/gemma-3-4b"}
assert f(good) == [], "A correct setup has no problems."
assert f({**good, "base_url": "http://host.docker.internal:1234/v1/"}) == [], "A trailing / is fine."
assert f({**good, "base_url": "http://host.docker.internal:1234/v1/chat/completions"}) == ["cut the URL at /v1"], "Rule 1."
assert f({**good, "base_url": "http://host.docker.internal:1234"}) == ["add /v1 to the URL"], "Rule 2."
assert f({**good, "base_url": "http://localhost:1234/v1"}) == ["use host.docker.internal"], "Rule 3."
assert f({**good, "base_url": "http://127.0.0.1:1234/v1"}) == ["use host.docker.internal"], "Rule 3 also covers 127.0.0.1."
assert f({**good, "base_url": "http://localhost:1234/v1", "n8n_in_docker": False}) == [], "localhost is fine when n8n isn't in Docker."
assert f({**good, "use_responses_api": True}) == ["turn off Use Responses API"], "Rule 4."
assert f({**good, "model": ""}) == ["set the model ID"], "Rule 5."
bad = {"base_url": "http://localhost:1234/v1/chat/completions", "n8n_in_docker": True, "use_responses_api": True, "model": ""}
assert f(bad) == ["cut the URL at /v1", "use host.docker.internal", "turn off Use Responses API", "set the model ID"], "Report every problem, in rule order."
