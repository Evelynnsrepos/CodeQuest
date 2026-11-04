---
title: Checkpoint: train a character-level model
xp: 80
---
# Checkpoint

The Module 5 checkpoint, from your plan: *train a tiny character-level model on a text and watch its loss go down.* This time nothing is scaffolded except `softmax` and the text. Everything else you write yourself, using what you built in lessons 8–11.

## Your quest

Train a neural **bigram** model (a `V × V` table of logits) on `TEXT`, with a validation split.

1. `vocab`: the sorted list of the unique characters in `TEXT`. `V = len(vocab)`.
2. Turn the text into a list of index pairs `(current, next)` for every neighbouring pair of characters.
3. Split the pairs: the first 90% for training, the last 10% for validation.
4. Start all logits at 0. Set `val_loss_start` to the validation loss before training.
5. Train for **40 epochs** with full-batch gradient descent (`softmax − onehot`, averaged, LLMs 5 lesson 11) and a learning rate you choose. Append the training loss of each epoch to `train_losses`.
6. Set `val_loss_end` to the validation loss after training.
7. Write `generate(start, length, rng)`: starting from the character `start`, repeatedly sample the next character from the model (`rng.choices(range(V), weights=probs)[0]`) and return the generated string of `length` characters (not counting `start`).

Print the losses as you go. The check verifies that the first loss is about `log V`, that training loss falls clearly, and that validation loss falls too.

Then answer for yourself: why does the generated text look like English letter soup but not like English words? What would you change first to make it better?

## On your machine (the real checkpoint)

Copy your code to `~/llm-course/charmodel.py`, swap `TEXT` for a text file you like (`TEXT = open("book.txt").read()`), and run it. Then go further, in order:

1. Use **two** previous characters as context (a trigram table): how much does the validation loss improve?
2. Follow Karpathy's makemore part 3 (MLP) with PyTorch.
3. Train `nanoGPT`'s Shakespeare character model on your GPU (needs PyTorch with ROCm; Module 6 covers the setup).

## What's next

LLMs 6: the training options for real models. LoRA, QLoRA, DPO, datasets, Hugging Face tools, and when to use RAG instead.
