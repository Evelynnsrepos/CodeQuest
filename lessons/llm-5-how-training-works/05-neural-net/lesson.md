---
title: A neural network from Values
xp: 45
---
# Neuron, Layer, MLP

> **Warm-up:** in LLMs 4 you wrote a `Linear` class with plain numbers. What changes if the weights are `Value`s instead?

Everything you compute with them becomes a graph, so one call to `loss.backward()` gives you the gradient for **every weight** at once. That's the whole trick of deep learning frameworks.

The building blocks (micrograd's names, which mirror PyTorch's):

- A **Neuron** has one weight per input and a bias. It computes `tanh(Σ wᵢ·xᵢ + b)`, or skips the tanh if it's in the output layer.
- A **Layer** is a list of neurons that all see the same inputs; it outputs one number per neuron.
- An **MLP** (multi-layer perceptron) is a list of layers; each layer's outputs are the next layer's inputs.

Each class has `parameters()`, returning every `Value` that training should adjust. In PyTorch that's `model.parameters()`, which you hand to the optimizer.

Weights start **random** (here uniform in −1…1). If they all started equal, every neuron in a layer would compute the same thing and get the same gradient forever: random initialization breaks that symmetry. Real models use carefully scaled random init (Kaiming, Xavier) so signals neither explode nor vanish through many layers.

Counting parameters: a layer from `n` inputs to `m` outputs has `n·m` weights + `m` biases. The program prints the count; check it by hand: 3→4→4→1.

## Your quest

Fill in:

1. `Neuron.__call__(x)`: start from `self.b`, add `wᵢ * xᵢ` for every weight and input, then apply `.tanh()` only if `self.activation`. `Neuron.parameters()`: the weights plus the bias, as one list.
2. `Layer.__call__(x)`: a list with each neuron's output. `Layer.parameters()`: all neurons' parameters in one list.
3. `MLP.__call__(x)`: feed `x` through the layers in order. `MLP.parameters()`: all layers' parameters.

## Review

<details><summary>What is the local derivative of tanh?</summary>1 − tanh(x)²</details>
<details><summary>Why do networks need non-linear activations?</summary>Without them, stacked linear layers collapse into one linear function.</details>
<details><summary>How do you sanity-check an autograd engine?</summary>Compare its gradients with numerical (central difference) derivatives.</details>
