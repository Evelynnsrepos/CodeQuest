import re

HEADER = ("Answer the question using only the sources below. Cite sources like [1]. "
          "If the sources don't contain the answer, say \"I don't know\".")


def tokens(text):
    return len(text) // 4


def build_prompt(question, chunks, budget):
    lines = []
    used = []
    total = 0
    for c in chunks:
        line = "[" + str(len(lines) + 1) + "] (" + c["id"] + ") " + c["text"]
        if total + tokens(line) > budget:
            break
        lines.append(line)
        used.append(c["id"])
        total = total + tokens(line)
    prompt = HEADER + "\n\n" + "\n".join(lines) + "\n\nQuestion: " + question
    return prompt, used


def citations(answer):
    found = []
    for n in re.findall(r"\[(\d+)\]", answer):
        if int(n) not in found:
            found.append(int(n))
    return sorted(found)


def check_answer(answer, n_sources):
    cited = citations(answer)
    if len(cited) == 0:
        if "i don't know" in answer.lower():
            return "ok"
        return "no citations"
    for n in cited:
        if n < 1 or n > n_sources:
            return "bad citation"
    return "ok"


chunks = [{"id": "nix-gc", "text": "Run nix-collect-garbage -d to delete old generations."},
          {"id": "nix-flakes", "text": "A flake pins its inputs in flake.lock."}]
prompt, used = build_prompt("how do I free disk space?", chunks, budget=40)
print(prompt, used)
print(check_answer("Use nix-collect-garbage -d [1].", 2), check_answer("Do it [3].", 2), check_answer("Easy!", 2))
