---
title: Checkpoint: train a character-level model
minutes: 60
xp: 80
hint: Part 1: vocab = sorted(set(TEXT)), V = len(vocab), and stoi maps each character to its position in vocab
hint: pairs: for i in range(len(TEXT) - 1): pairs.append((stoi[TEXT[i]], stoi[TEXT[i + 1]])). Then cut = int(len(pairs) * 0.9)
hint: Training is lesson 11's loss_and_grad written out, inside for epoch in range(40):, plus train_losses.append(loss / len(train))
hint: generate: i = stoi[start], out = "", then length times: i = rng.choices(range(V), weights=softmax(W[i]))[0] and out = out + vocab[i]
hint: Every line is in the starter as a comment. Delete the # and the one space after it, and keep the indentation.
---
# Checkpoint

⏱️ About 60 minutes

The Module 5 checkpoint, from your plan: *train a tiny character-level model on a text and watch its loss go down.* It puts lessons 8–11 together in one program. Try writing it yourself first; every line is also given below and in the starter.

## 🐍 Python you need

Almost everything here is from lessons 10 and 11. New:

| You write | Say it | What it does |
|---|---|---|
| `set(TEXT)` | | every **different** character in the text, once each |
| `sorted(...)` | | puts them in order, as a list: `[' ', ',', '.', 'a', 'b', …]` |
| `stoi[vocab[i]] = i` | | a dictionary "character → its position", like `STOI` in lesson 10 |
| `TEXT[i]`, `TEXT[i + 1]` | | a character and the next one: one training pair |
| `def loss_on(data):` | | a helper you write yourself, used twice (before and after training) |
| `train_losses.append(...)` | | one loss per epoch, so the check can see the curve |
| `train_losses[-1]` | "the last one" | `[-1]` counts from the end |
| `rng.choices(range(V), weights=probs)[0]` | | picks one position, each with its probability (LLMs 4, lesson 9) |

### 👀 Worked example: the vocabulary of "baba ."

```python
text = "baba ."
vocab = sorted(set(text))        # [' ', '.', 'a', 'b']
stoi = {}
for i in range(len(vocab)):
    stoi[vocab[i]] = i            # {' ': 0, '.': 1, 'a': 2, 'b': 3}
pairs = []
for i in range(len(text) - 1):
    pairs.append((stoi[text[i]], stoi[text[i + 1]]))
print(pairs)                      # [(3, 2), (2, 3), (3, 2), (2, 0), (0, 1)]
```

Five pairs from six characters: b→a, a→b, b→a, a→space, space→. Part 1 below is this, plus a 90/10 split and a table of zeros.

## 🎯 Your quest

Train a neural **bigram** model on `TEXT`, with a validation split. Every line is in the starter as a comment: remove the `# ` in front (keep the indentation behind it). Here is what each part does.

**Part 1: data.** The vocabulary, the pairs, the split (first 90% train, last 10% validation), all logits at 0, and a helper that measures the loss on any list of pairs:

```python
vocab = sorted(set(TEXT))
V = len(vocab)
stoi = {}
for i in range(V):
    stoi[vocab[i]] = i
pairs = []
for i in range(len(TEXT) - 1):
    pairs.append((stoi[TEXT[i]], stoi[TEXT[i + 1]]))
cut = int(len(pairs) * 0.9)
train = pairs[:cut]
val = pairs[cut:]
W = []
for i in range(V):
    W.append([0.0] * V)


def loss_on(data):
    probs = []
    for row in W:
        probs.append(softmax(row))
    total = 0.0
    for a, b in data:
        total = total - math.log(probs[a][b])
    return total / len(data)


def loss_on(data):
    probs = []
    for row in W:
        probs.append(softmax(row))
    total = 0.0
    for a, b in data:
        total = total - math.log(probs[a][b])
    return total / len(data)
```

**Part 2: training.** The validation loss before training, then 40 epochs of lesson 11's gradient (softmax − onehot, averaged) with learning rate 30, and the validation loss after:

```python
val_loss_start = loss_on(val)
for epoch in range(40):
    probs = []
    for row in W:
        probs.append(softmax(row))
    grad = []
    for i in range(V):
        grad.append([0.0] * V)
    loss = 0.0
    for a, b in train:
        loss = loss - math.log(probs[a][b])
        for j in range(V):
            grad[a][j] = grad[a][j] + probs[a][j]
        grad[a][b] = grad[a][b] - 1
    train_losses.append(loss / len(train))
    for i in range(V):
        for j in range(V):
            W[i][j] = W[i][j] - 30 * grad[i][j] / len(train)
    if epoch % 5 == 0:
        print("epoch", epoch, "train loss", round(train_losses[-1], 3))
val_loss_end = loss_on(val)
print("validation loss:", round(val_loss_start, 3), "->", round(val_loss_end, 3))
```

**Part 3: generate.** Start at a character and sample `length` more:

```python
def generate(start, length, rng):
    i = stoi[start]
    out = ""
    for step in range(length):
        i = rng.choices(range(V), weights=softmax(W[i]))[0]
        out = out + vocab[i]
    return out
```

The check verifies that the first loss is about log V ≈ 3.30, that training loss falls clearly (to about 2.1), and that validation loss falls too (to about 2.8).

Then answer for yourself: why does the generated text look like English letter soup but not like English words? (Hint: how many characters of context does the model see?) What would you change first to make it better?

## On your machine (the real checkpoint)

Copy your code to `~/llm-course/charmodel.py`, swap `TEXT` for a text file you like (`TEXT = open("book.txt").read()`), and run it. Then go further, in order:

1. Use **two** previous characters as context (a trigram table): how much does the validation loss improve?
2. Follow Karpathy's makemore part 3 (MLP) with PyTorch.
3. Train `nanoGPT`'s Shakespeare character model on your GPU (needs PyTorch with ROCm; Module 6 covers the setup).

## What's next

LLMs 6: the training options for real models. LoRA, QLoRA, DPO, datasets, Hugging Face tools, and when to use RAG instead.
