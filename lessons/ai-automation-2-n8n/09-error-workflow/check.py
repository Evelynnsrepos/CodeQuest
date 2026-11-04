f = ns.get("error_alert")
assert f, "Define a function called error_alert."
wf = {"id": "1", "name": "Morning summary"}
full = {"execution": {"id": "9", "url": "http://n8n/execution/9", "lastNodeExecuted": "Ollama", "error": {"message": "timeout"}}, "workflow": wf}
assert f(full) == "❌ Morning summary failed at Ollama: timeout\nhttp://n8n/execution/9", f"Got {f(full)!r}."
nourl = {"execution": {"lastNodeExecuted": "HTTP Request", "error": {"message": "404"}}, "workflow": wf}
assert f(nourl) == "❌ Morning summary failed at HTTP Request: 404", "No url (execution not saved): just the first line."
trig = {"trigger": {"error": {"message": "IMAP login failed"}}, "workflow": wf}
assert f(trig) == "❌ Morning summary failed at its trigger: IMAP login failed", "Trigger errors have 'trigger' instead of 'execution'."
