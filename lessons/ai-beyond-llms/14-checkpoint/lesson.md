---
title: Checkpoint: the whole map
xp: 120
---
# Pick the right tool

> **Warm-up:** for each of these, which kind of model would you reach for first: predicting house prices from a spreadsheet, transcribing a podcast, generating a poster image, sorting photos by what's in them without labels?

(Gradient-boosted trees; Whisper; a diffusion model; CLIP embeddings plus clustering.)

## Your quest

### Part 1: the numbers

1. `scores(tp, fp, fn, tn)`: return `(accuracy, precision, recall)` (lesson 06). A fraud model with tp=2, fp=3, fn=98, tn=19897 has 99.5% accuracy, but what is its recall?
2. `weights(h, w, k)`: return `(dense, conv)`: the weights to map an h×w grayscale image to an h×w output with a fully connected layer (`(h·w)²`, ignore biases) and with one k×k convolution kernel (`k·k`).
3. `q_new(q, r, best_next, alpha, gamma)`: one Q-learning update, `q + α · (r + γ · best_next − q)` (lesson 13).

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
