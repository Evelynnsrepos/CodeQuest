---
title: Attention in one picture
xp: 30
---
# Each word looks at the others

> **Warm-up:** in "The cat didn't eat because **it** was full", what does "it" refer to? How did you decide?

**Attention** is how a transformer (the T in GPT) lets each token gather information from the earlier tokens. For the token "it":

1. It gives every earlier token a **relevance score** (how useful is "cat"? "eat"? "The"?).
2. **Softmax** turns the scores into weights that add up to 1 (lesson 03).
3. Its new meaning is the **weighted average** of the earlier tokens' vectors: mostly "cat", a little of the rest.

<svg viewBox="0 0 520 150" width="100%" style="max-width:520px" role="img" aria-label="The token 'it' with arrows to earlier tokens; the arrow to 'cat' is thickest, weight 0.7">
  <g font-size="14" fill="currentColor" text-anchor="middle">
    <text x="50" y="30">The</text><text x="140" y="30">cat</text><text x="240" y="30">didn't</text><text x="340" y="30">eat</text><text x="440" y="130">it</text>
    <text x="70" y="80" font-size="12">0.05</text><text x="175" y="75" font-size="12">0.70</text><text x="265" y="80" font-size="12">0.05</text><text x="360" y="80" font-size="12">0.20</text>
  </g>
  <g stroke="#6c4cf5" fill="none" stroke-linecap="round">
    <line x1="430" y1="115" x2="55" y2="38" stroke-width="1"/>
    <line x1="430" y1="115" x2="145" y2="38" stroke-width="8"/>
    <line x1="430" y1="115" x2="245" y2="38" stroke-width="1"/>
    <line x1="430" y1="115" x2="345" y2="38" stroke-width="3"/>
  </g>
</svg>

The scores come from learned vectors called **queries** and **keys**, and the averaged vectors are **values**; that's the full version in LLMs 8 and AI engineer 1 lesson 03. A model stacks dozens of these layers, each with many attention "heads" looking for different relationships.

**Go deeper:** LLMs 1 lesson 12, LLMs 8 lesson 01, Math 2 lesson 11.

## Your quest

1. `weights(scores)`: softmax of the scores (no temperature).
2. `attend(scores, values)`: `values` is a list of vectors (one per earlier token). Return the weighted average vector: Σ weightᵢ · valueᵢ.

**Remember:** score, softmax, weighted average.
