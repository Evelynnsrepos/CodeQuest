---
title: Checkpoint: the whole map
xp: 100
---
# Pick the right tool

> **Warm-up:** for each of these, which kind of model would you reach for first: predicting house prices from a spreadsheet, transcribing a podcast, generating a poster image, sorting photos by what's in them without labels?

(Gradient-boosted trees; Whisper; a diffusion model; CLIP embeddings plus clustering.)

## Your quest

Fill `ANSWERS` with the best letter.

1. A bank wants to predict loan default from 30 columns of customer data. Best first try?
   a) Fine-tune an LLM  b) Gradient-boosted trees  c) A diffusion model
2. Why did transformers replace RNNs for language?
   a) RNNs can't use GPUs at all  b) Attention processes all positions in parallel and links distant tokens directly, avoiding vanishing gradients through time  c) Transformers have no parameters
3. Why does a CNN need far fewer weights than a fully connected network on images?
   a) It shares the same small kernel across all positions  b) It uses fewer pixels  c) It skips training
4. What does a diffusion model's network predict in DDPM training?
   a) The caption  b) The noise added to the image  c) The next pixel
5. How can CLIP classify images into categories it was never trained on?
   a) By comparing the image embedding with embeddings of text descriptions  b) By retraining at query time  c) It can't
6. A fraud model has 99.5% accuracy but recall 0.02. What does that mean?
   a) It's excellent  b) It catches only 2% of actual fraud; accuracy is high because fraud is rare  c) It has too many false alarms
7. How does a vision-language model feed an image to the LLM?
   a) As a file path  b) As patch embeddings mapped by a projector into the LLM's token space  c) As a text description written by a human
8. In Q-learning, how does a reward at the end of an episode reach earlier states?
   a) Through the γ·max Q(s', a') term in each update, step by step backwards  b) It doesn't  c) Through the learning rate only

## Review

<details><summary>Write the Q-learning update.</summary>Q(s, a) += α · (r + γ·max_a' Q(s', a') − Q(s, a)).</details>
<details><summary>What is a mel scale for?</summary>Spacing frequency bands like human hearing does, finer at low frequencies.</details>
<details><summary>Formula for F1?</summary>2·P·R / (P + R).</details>

## What's next

Free, university-level follow-ups: Andrew Ng's *Machine Learning Specialization* (classic ML), Stanford **CS231n** (vision), **CS224n** (NLP), **CS234** or David Silver's RL lectures, and the *Hugging Face Diffusion Models* course. Sutton & Barto's *Reinforcement Learning: An Introduction* is free online. For hands-on tabular ML, try scikit-learn and XGBoost on a Kaggle dataset.
