---
title: Training: nudge, check, repeat
xp: 30
---
# How a model learns

> **Warm-up:** you're blindfolded on a hill and want to reach the bottom. What do you do?

You feel which way the ground slopes and take a small step downhill. Repeat. That's **gradient descent**, and it's how every neural network learns:

1. Make a prediction with the current weights.
2. Measure how wrong it is: the **loss** (e.g. the average squared error).
3. Compute the **gradient**: which direction each weight should move to make the loss smaller.
4. Move each weight a small step that way (the step size is the **learning rate**). Repeat thousands of times.

For a one-weight model `prediction = w · x` with squared-error loss, the gradient is the average of `2 · (w·x − y) · x`. An LLM does exactly this with billions of weights, and the "y" is the real next token.

**Learning rate too big** → the steps overshoot and the loss explodes. **Too small** → it takes forever.

**Go deeper:** LLMs 5 (How training works), Math 3 lessons 09–11, AI engineer 1 lesson 08.

<div class="quiz" data-answer="0" data-why="The steps overshoot the bottom. Smaller steps fix it. Try it in the drawing below with a learning rate above 1."><p><b>Predict first:</b> your loss gets bigger every step until it explodes. What do you change?</p><button>make the learning rate smaller</button><button>make the learning rate bigger</button><button>train for more steps</button></div>

<div class="explore" data-widget="gradient-descent"></div>

## Your quest

`train(xs, ys, steps, lr)`: start with `w = 0.0`, and each step set `w = w − lr · gradient`. Return `w`.

**Remember:** predict, measure the loss, step downhill.
