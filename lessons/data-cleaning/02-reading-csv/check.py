gd, rc = ns.get("guess_delimiter"), ns.get("read_csv")
assert gd and rc, "Keep guess_delimiter and read_csv."
assert gd("a;b;c\n1,5;2;3") == ";", "Only the first line counts: 'a;b;c' has two semicolons."
assert gd("a,b\n1,2") == ",", "Commas here."
assert gd("a\tb\tc\n1\t2\t3") == "\t", "Tabs here."
rows = rc("\ufeffName;Stadt\n\"Smith; John\";Köln\n")
assert rows == [{"Name": "Smith; John", "Stadt": "Köln"}], f"Strip the BOM and respect quotes. Got {rows!r}."
rows = rc('id,text\n1,"Hello, world"\n2,ok\n')
assert rows == [{"id": "1", "text": "Hello, world"}, {"id": "2", "text": "ok"}], f"Got {rows!r}."
