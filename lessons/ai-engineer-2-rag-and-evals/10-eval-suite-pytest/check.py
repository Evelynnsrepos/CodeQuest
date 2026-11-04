import os, sys, tempfile
ws, rs = ns.get("write_suite"), ns.get("run_suite")
assert ws and rs, "Keep write_suite and run_suite."
good = [("delete old generations", "nix-gc"), ("where are flake inputs pinned", "nix-flakes")]
with tempfile.TemporaryDirectory() as d:
    ws(d, good, 0.8)
    assert sorted(os.listdir(d)) >= ["retriever.py", "test_rag.py"], "Write retriever.py and test_rag.py."
    src = open(os.path.join(d, "test_rag.py"), encoding="utf-8").read()
    assert "parametrize" in src and "def test_right_chunk_in_top3" in src and "def test_overall_recall" in src, "test_rag.py needs the parametrized test and the recall test."
    assert rs(d) == 0, "With a good golden set, pytest should pass (exit code 0)."
with tempfile.TemporaryDirectory() as d:
    ws(d, good + [("what is the meaning of life", "nonexistent-note")], 0.6)
    assert rs(d) == 1, "With an item the retriever can't find, the parametrized test must fail (exit code 1)."
