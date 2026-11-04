import re


def readme_report(text):
    lines = text.splitlines()
    first = next((l for l in lines if l.strip()), "")
    heads = [l.lower() for l in lines if l.startswith("#")]
    low = text.lower()
    return {
        "title": first.startswith("# "),
        "run": any(w in h for h in heads for w in ("run", "install", "usage")),
        "docker": "docker run" in low or "docker compose" in low,
        "eval": any("eval" in h or "results" in h for h in heads),
        "numbers": re.search(r"\d+%|\d\.\d+", text) is not None,
        "license": any("license" in h for h in heads),
    }


def score(text):
    return sum(readme_report(text).values())


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
