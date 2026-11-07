---
title: Tiny GPT 1: data and batches
minutes: 40
xp: 55
hint: build_vocab: chars = sorted(set(text)), then for i in range(len(chars)): stoi[chars[i]] = i and itos[i] = chars[i]
hint: encode: ids = [], for c in s: ids.append(stoi[c]). decode: out = "", for i in ids: out = out + itos[int(i)]
hint: get_batch: ix = torch.randint(...) as in the quest, then for i in ix: xs.append(data[i:i + block]) and ys.append(data[i + 1:i + block + 1])
hint: get_batch, last line: return torch.stack(xs), torch.stack(ys)
---
# From text to training examples

⏱️ About 40 minutes

> **Warm-up:** in LLMs 5 you trained a bigram model. What was one training example?

The next three lessons build and train a real (tiny) GPT in PyTorch, the same design as nanoGPT and as LLMs 8, small enough to train on a laptop CPU in under a minute.

Step 1 is the data:

1. **Tokenize** by character (the simplest tokenizer): every distinct character gets an id. `stoi` maps character → id, `itos` id → character.
2. **Encode** the whole text into one long tensor of ids.
3. **Batches:** pick random start positions; each example is `block` ids `x`, and the target `y` is the **same window shifted one to the right**. So for every position the model learns "given everything so far, predict the next character", `block` predictions per example.

```
text:  E i n _ M e n s c h
x:     E i n _ M e n s
y:       i n _ M e n s c
```

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `sorted(set(text))` | | every different character once, in sorted order |
| `stoi[chars[i]] = i` | | "**s**tring **to** **i**nteger": character → id |
| `itos[i] = chars[i]` | | "**i**nteger **to** **s**tring": id → character |
| `int(i)` | | a one-number tensor → a plain number, so it works as a dictionary key |
| `out = out + itos[...]` | | glues the characters back into a text |
| `torch.randint(high, (batch,), generator=gen)` | | `batch` random whole numbers from 0 up to (not including) `high` |
| `data[i:i + block]` | | a slice of `block` ids starting at i |
| `torch.stack(xs)` | | a list of equal-length tensors → one 2-D tensor, one row each |

### 👀 Worked example: a tiny vocabulary

`text = "abba"`:

1. `set` → {a, b}, `sorted` → `["a", "b"]`.
2. `stoi` = `{"a": 0, "b": 1}`, `itos` = `{0: "a", 1: "b"}`.
3. `encode("abba")` → `[0, 1, 1, 0]`. `decode([1, 0])` → `"ba"`.
4. With data `[0, 1, 1, 0]`, block = 2 and a start i = 1: x = `data[1:3]` = `[1, 1]`, y = `data[2:4]` = `[1, 0]`. y is x moved one to the right: after "b" comes "b", after "bb" comes "a".

## 🎯 Your quest

1. `build_vocab(text)`: `(stoi, itos)` with the **sorted** distinct characters.
2. `encode(s, stoi)` → list of ids; `decode(ids, itos)` → string.
3. `get_batch(data, block, batch, gen)`: `data` is a 1-D `long` tensor. Draw `batch` start indexes with `torch.randint(len(data) - block, (batch,), generator=gen)`, and return `(x, y)`, both of shape `(batch, block)`, `y` shifted by one.

**Part 1:** `build_vocab`. Replace `return {}, {}` with:

1. `chars = sorted(set(text))`
2. `stoi = {}`
3. `itos = {}`
4. `for i in range(len(chars)):`
5. `    stoi[chars[i]] = i`
6. `    itos[i] = chars[i]`
7. `return stoi, itos`

**Part 2:** `encode`. Replace `return []` with:

1. `ids = []`
2. `for c in s:`
3. `    ids.append(stoi[c])`
4. `return ids`

`decode`: replace `return ""` with:

1. `out = ""`
2. `for i in ids:`
3. `    out = out + itos[int(i)]`
4. `return out`

**Part 3:** `get_batch`. Replace `return None, None` with:

1. `ix = torch.randint(len(data) - block, (batch,), generator=gen)`
2. `xs = []`
3. `ys = []`
4. `for i in ix:`
5. `    xs.append(data[i:i + block])`
6. `    ys.append(data[i + 1:i + block + 1])`
7. `return torch.stack(xs), torch.stack(ys)`

**Remember:** the target is the input shifted by one.

## Review

<details><summary>Why do the ReLUs matter in an MLP?</summary>Without a nonlinearity, stacked linear layers collapse into one linear map and can't bend.</details>
