---
title: Checkpoint: the whole map
minutes: 45
xp: 120
hint: scores: accuracy = (tp + tn) / (tp + fp + fn + tn). Then precision and recall with an if/else each, so you never divide by 0
hint: weights: dense = (h * w) ** 2 and conv = k * k, then return (dense, conv)
hint: q_new: return q + alpha * (r + gamma * best_next - q)
hint: Part 2: think about why each wrong option is wrong. Look back at lessons 01, 07, 10, 09, 12 and 13.
---
# Pick the right tool

⏱️ About 45 minutes

> **Warm-up:** for each of these, which kind of model would you reach for first: predicting house prices from a spreadsheet, transcribing a podcast, generating a poster image, sorting photos by what's in them without labels?

(Gradient-boosted trees; Whisper; a diffusion model; CLIP embeddings plus clustering.)

## Your quest

### Part 1: the numbers

1. `scores(tp, fp, fn, tn)`: return `(accuracy, precision, recall)` (lesson 06). A fraud model with tp=2, fp=3, fn=98, tn=19897 has 99.5% accuracy, but what is its recall?
2. `weights(h, w, k)`: return `(dense, conv)`: the weights to map an h×w grayscale image to an h×w output with a fully connected layer (`(h·w)²`, ignore biases) and with one k×k convolution kernel (`k·k`).
3. `q_new(q, r, best_next, alpha, gamma)`: one Q-learning update, `q + α · (r + γ · best_next − q)` (lesson 13).

### How to answer Part 1

These are your formulas from lessons 06, 08 and 13. `**` is "to the power", so `** 2` is squared.

`scores`: replace `return (0, 0, 0)` with:

1. `accuracy = (tp + tn) / (tp + fp + fn + tn)`
2. `if tp + fp == 0:`
3. `    precision = 0.0`
4. `else:`
5. `    precision = tp / (tp + fp)`
6. `if tp + fn == 0:`
7. `    recall = 0.0`
8. `else:`
9. `    recall = tp / (tp + fn)`
10. `return (accuracy, precision, recall)`

`weights`: replace `return (0, 0)` with:

1. `dense = (h * w) ** 2`
2. `conv = k * k`
3. `return (dense, conv)`

For a 28 × 28 image: 28 · 28 = 784 pixels, and a dense layer connects every pixel to every output: 784 · 784 = 614,656 weights. A 3 × 3 kernel has 9.

`q_new`: replace `return q` with:

1. `return q + alpha * (r + gamma * best_next - q)`

### Part 2: why questions

Fill `ANSWERS` with the letter of the **best** answer. Every option sounds reasonable on purpose: think about *why* each wrong one is wrong.

1. A bank wants to predict loan default from 30 columns of customer data. Best first try?
   - **a)** A small neural network, because it can learn any function.
   - **b)** Gradient-boosted trees: they usually win on tabular data, train fast and are easier to explain.
   - **c)** Fine-tune an LLM on the rows written as text.
   - **d)** k-means with 2 clusters, one for default and one for no default.

2. Why did transformers replace RNNs for language?
   - **a)** RNNs can't be trained with backpropagation.
   - **b)** RNNs need more parameters for the same vocabulary.
   - **c)** Attention handles all positions in parallel and links far-apart tokens directly, while an RNN must pass everything step by step, which is slow and loses distant information.
   - **d)** Transformers don't need a tokenizer.

3. What does a DDPM diffusion network learn to predict during training?
   - **a)** The noise that was added to the image.
   - **b)** The clean image directly, in one step.
   - **c)** The next pixel, left to right.
   - **d)** The caption of the image.

4. How can CLIP sort images into categories it was never trained on?
   - **a)** It retrains its last layer for each new category at query time.
   - **b)** It looks the category up in its training captions.
   - **c)** It runs k-means on the image and names each cluster.
   - **d)** It compares the image's embedding with the embeddings of text like “a photo of a ___” and picks the closest.

5. How does a vision-language model feed an image to the LLM?
   - **a)** It writes a caption first and feeds the caption as text.
   - **b)** It turns image patches into embeddings with a vision encoder, and a projector maps them into the LLM's token-embedding space.
   - **c)** It converts the pixels into extra vocabulary tokens with BPE.
   - **d)** It sends the image to a separate model and merges the two answers.

6. In Q-learning, how does a reward at the end of an episode reach the first states?
   - **a)** Through the γ · max Q(s′, a′) term: each update copies some of the next state's value backward, one step at a time.
   - **b)** The final reward is added to every state visited in the episode.
   - **c)** Only through the learning rate α.
   - **d)** It doesn't; only the last state learns.

## Review

<details><summary>Write the Q-learning update.</summary>Q(s, a) += α · (r + γ·max_a' Q(s', a') − Q(s, a)).</details>
<details><summary>What is a mel scale for?</summary>Spacing frequency bands like human hearing does, finer at low frequencies.</details>
<details><summary>Formula for F1?</summary>2·P·R / (P + R).</details>

## What's next

Free, university-level follow-ups: Andrew Ng's *Machine Learning Specialization* (classic ML), Stanford **CS231n** (vision), **CS224n** (NLP), **CS234** or David Silver's RL lectures, and the *Hugging Face Diffusion Models* course. Sutton & Barto's *Reinforcement Learning: An Introduction* is free online. For hands-on tabular ML, try scikit-learn and XGBoost on a Kaggle dataset.
