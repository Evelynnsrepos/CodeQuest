import re


def readme_report(text):
    lines = text.splitlines()
    first = ""
    for l in lines:
        if l.strip() != "":
            first = l
            break
    heads = []
    for l in lines:
        if l.startswith("#"):
            heads.append(l.lower())
    low = text.lower()
    report = {
        "title": first.startswith("# "),
        "run": False,
        "docker": "docker run" in low or "docker compose" in low,
        "eval": False,
        "numbers": re.search(r"\d+%|\d\.\d+", text) is not None,
        "license": False,
    }
    for h in heads:
        if "run" in h or "install" in h or "usage" in h:
            report["run"] = True
        if "eval" in h or "results" in h:
            report["eval"] = True
        if "license" in h:
            report["license"] = True
    return report


def score(text):
    report = readme_report(text)
    total = 0
    for key in report:
        if report[key]:
            total = total + 1
    return total


MY_README = """# Notes RAG

Ask questions about my Linux and AI notes, with sources.

## Run it

    docker compose up
    # or: docker run -p 8000:8000 --env-file .env notes-rag

## How it works

Chunking, hybrid search (BM25 + nomic-embed-text, fused with RRF), answers with citations.

## Evaluation results

60 hand-written questions: recall@3 0.92 (BM25 alone: 0.71), 97% of answers with valid citations.

## Limitations

English and German notes only; no images.

## License

MIT
"""
print(readme_report(MY_README), score(MY_README))
