---
title: A neural network from Values
minutes: 60
xp: 45
hint: Neuron.__call__: total = self.b, then for i in range(len(self.w)): total = total + self.w[i] * x[i]
hint: Neuron.__call__ ends: if self.activation: return total.tanh(). After the if: return total
hint: Neuron.parameters: return self.w + [self.b]
hint: Layer.__call__: outputs = [], for n in self.neurons: outputs.append(n(x)), return outputs
hint: parameters in Layer and MLP: params = [], loop, params = params + n.parameters() (or layer.parameters()), return params
hint: MLP.__call__: for layer in self.layers: x = layer(x), then return x
---
# Neuron, Layer, MLP

⏱️ About 60 minutes

> **Warm-up:** in LLMs 4 you wrote a `Linear` class with plain numbers. What changes if the weights are `Value`s instead?

Everything you compute with them becomes a graph, so one call to `loss.backward()` gives you the gradient for **every weight** at once. That's the whole trick of deep learning frameworks.

The building blocks (micrograd's names, which mirror PyTorch's):

- A **Neuron** has one weight per input and a bias. It computes `tanh(Σ wᵢ·xᵢ + b)`, or skips the tanh if it's in the output layer.
- A **Layer** is a list of neurons that all see the same inputs; it outputs one number per neuron.
- An **MLP** (multi-layer perceptron) is a list of layers; each layer's outputs are the next layer's inputs.

Each class has `parameters()`, returning every `Value` that training should adjust. In PyTorch that's `model.parameters()`, which you hand to the optimizer.

Weights start **random** (here uniform in −1…1). If they all started equal, every neuron in a layer would compute the same thing and get the same gradient forever: random initialization breaks that symmetry. Real models use carefully scaled random init (Kaiming, Xavier) so signals neither explode nor vanish through many layers.

Counting parameters: a layer from `n` inputs to `m` outputs has `n·m` weights + `m` biases. The program prints the count; check it by hand: 3→4→4→1.

## 🔬 Take the formula apart

<div class="formula">output = <span class="k1">tanh</span>( <span class="k2">Σ wᵢ·xᵢ</span> <span class="k3">+ b</span> )</div>

1. <span class="k2">Σ wᵢ·xᵢ</span>: multiply each input by its own weight and add them up (a dot product, LLMs 4 lesson 3).
2. <span class="k3">+ b</span>: add the bias.
3. <span class="k1">tanh</span>: squash into −1…1 (lesson 4). Skipped in the last layer.

Numbers: w = [0.5, −1], b = 0.2, x = [2, 1]: 0.5·2 + (−1)·1 + 0.2 = 1 − 1 + 0.2 = 0.2. tanh(0.2) ≈ **0.197**.

**Counting parameters** for 3 → 4 → 4 → 1:
1. 3 → 4: 3·4 = 12 weights + 4 biases = 16
2. 4 → 4: 16 weights + 4 biases = 20
3. 4 → 1: 4 weights + 1 bias = 5
4. Total: 16 + 20 + 5 = **41**.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `total = self.b` | | start the sum at the bias (a `Value`, so the graph is built) |
| `self.w[i] * x[i]` | | weight number i times input number i |
| `if self.activation:` … `return total.tanh()` | | the hidden layers squash; a `return` ends the function |
| `return total` (after the `if`) | | only reached when there's no activation |
| `self.w + [self.b]` | | `+` on two lists glues them: `[w0, w1, w2] + [b]` = `[w0, w1, w2, b]` |
| `params = params + n.parameters()` | | adds one neuron's list to the end of the big list |
| `outputs.append(n(x))` | | `n(x)` runs that neuron's `__call__` |

### 👀 Worked example: a team of counters

```python
class Counter:
    def __init__(self, items):
        self.items = items

    def parameters(self):
        return self.items + ["lid"]

class Shelf:
    def __init__(self):
        self.counters = [Counter(["a", "b"]), Counter(["c"])]

    def parameters(self):
        params = []
        for c in self.counters:
            params = params + c.parameters()
        return params

print(Shelf().parameters())   # ['a', 'b', 'lid', 'c', 'lid']
```

1. First counter gives `["a", "b", "lid"]`. params = [] + that.
2. Second gives `["c", "lid"]`. params = `["a", "b", "lid", "c", "lid"]`.

Layer and MLP collect their parameters exactly like `Shelf`.

## 🎯 Your quest

**Neuron.** In `__call__`, replace `return None` with:

1. `        total = self.b`
2. `        for i in range(len(self.w)):`
3. `            total = total + self.w[i] * x[i]`
4. `        if self.activation:`
5. `            return total.tanh()`
6. `        return total`

In `parameters`, replace `return []` with `        return self.w + [self.b]`

**Layer.** In `__call__`, replace `return []` with:

1. `        outputs = []`
2. `        for n in self.neurons:`
3. `            outputs.append(n(x))`
4. `        return outputs`

In `parameters`:

1. `        params = []`
2. `        for n in self.neurons:`
3. `            params = params + n.parameters()`
4. `        return params`

**MLP.** In `__call__`, replace `return x` with:

1. `        for layer in self.layers:`
2. `            x = layer(x)`
3. `        return x`

In `parameters`: the same four lines as Layer's, with `layer` instead of `n`:

1. `        params = []`
2. `        for layer in self.layers:`
3. `            params = params + layer.parameters()`
4. `        return params`

It prints `41 parameters` and one output `Value`.

## Review

<details><summary>What is the local derivative of tanh?</summary>1 − tanh(x)²</details>
<details><summary>Why do networks need non-linear activations?</summary>Without them, stacked linear layers collapse into one linear function.</details>
<details><summary>How do you sanity-check an autograd engine?</summary>Compare its gradients with numerical (central difference) derivatives.</details>
