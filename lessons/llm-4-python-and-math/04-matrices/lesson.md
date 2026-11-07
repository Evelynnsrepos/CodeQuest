---
title: Matrices and matrix multiplication
minutes: 60
xp: 40
hint: shape: return (len(A), len(A[0])): rows, then the length of the first row
hint: transpose: result = [], for j in range(len(A[0])): new_row = [], for i in range(len(A)): new_row.append(A[i][j]). Then result.append(new_row), return result
hint: matmul starts with: if len(A[0]) != len(B): raise ValueError("shape mismatch")
hint: matmul: columns = transpose(B), C = [], for row in A: new_row = [], for col in columns: total = 0 and for k in range(len(row)): total = total + row[k] * col[k]
hint: Then new_row.append(total) (inside 'for col'), C.append(new_row) (inside 'for row'), and at the end return C
---
# The operation LLMs are made of

⏱️ About 60 minutes

> **Warm-up:** in the last lesson's `Linear` class, each output was a dot product of one weight row with the input. What do you get if you stack all those rows into one grid?

A **matrix** is a grid of numbers: `m` rows by `n` columns, written `m × n`. In Python, a list of rows:

```python
W = [[1, 2, 3],
     [4, 5, 6]]      # 2 × 3
```

**Matrix × vector** is exactly your `Linear` layer without the bias: each output is a row of `W` dotted with `x`. A 2 × 3 matrix turns a 3-vector into a 2-vector. Geometrically, a matrix is a *transformation* of space: it can rotate, stretch, squash and project (3Blue1Brown's *Essence of Linear Algebra*, chapter 3, shows this beautifully).

**Matrix × matrix**: `C = A @ B` where entry `C[i][j]` is row `i` of `A` dotted with column `j` of `B`:

```
A: m × k      B: k × n      C: m × n
          ↑ the inner sizes must match
```

That shape rule is the single most common source of errors in ML code ("mat1 and mat2 shapes cannot be multiplied (4x3 and 4x2)"). Read every error like that as: the inner numbers didn't match.

Why it's everywhere: a whole **batch** of token vectors stacked as rows, `X` (tokens × d), goes through a layer as `X @ Wᵀ`: one big matrix multiplication, which is exactly what GPUs are built to do fast. Q, K and V for all tokens are three matmuls; the attention scores are `Q @ Kᵀ`; the MLP is two or three more.

The **transpose** `Aᵀ` swaps rows and columns: `Aᵀ[j][i] = A[i][j]`.

## 🔬 Take the formulas apart

**Size `m × n`.** Say "m by n". The first number is always **rows** (going down), the second **columns** (going across). `[[1, 2, 3], [4, 5, 6]]` is 2 × 3: 2 rows, 3 columns.

**One entry `A[i][j]`.** Row `i`, then column `j`. In the 2 × 3 matrix above, `A[1][0]` is row 1 (the second row), column 0 (the first column): **4**.

**Transpose** <div class="formula"><span class="k1">Aᵀ</span>[j][i] = <span class="k2">A</span>[i][j]</div>
The little `ᵀ` means "transposed". Rows become columns: the first row `[1, 2, 3]` becomes the first column.
```
A  = [[1, 2, 3],        Aᵀ = [[1, 4],
      [4, 5, 6]]              [2, 5],
                              [3, 6]]
```

**Matrix × matrix** <div class="formula"><span class="k1">C[i][j]</span> = <span class="k2">(row i of A)</span> · <span class="k3">(column j of B)</span></div>
Every entry of the result is one dot product (lesson 3). Take A = `[[1, 2], [3, 4]]` and B = `[[5, 6], [7, 8]]`:

1. C[0][0] = row 0 of A · column 0 of B = [1, 2] · [5, 7] = 1×5 + 2×7 = **19**
2. C[0][1] = [1, 2] · [6, 8] = 6 + 16 = **22**
3. C[1][0] = [3, 4] · [5, 7] = 15 + 28 = **43**
4. C[1][1] = [3, 4] · [6, 8] = 18 + 32 = **50**

So C = `[[19, 22], [43, 50]]`.

**The shape rule.** A row of A and a column of B must have the **same length**, or the dot product makes no sense. So:
<div class="formula"><span class="k1">(m × k)</span> @ <span class="k2">(k × n)</span> → <span class="k3">(m × n)</span></div>

The two inner numbers (both `k`) must match. The outer ones give the result's size.

<div class="wrong">❌ (1 × 2) @ (1 × 2): a row has 2 numbers, a column has 1. Error.</div>
<div class="right">✅ (1 × 2) @ (2 × 1): 2 and 2 match, and the result is 1 × 1.</div>

The trick in code: the columns of B are the rows of `transpose(B)`. So you transpose B once and then only work with rows.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `A[0]` | | the first row |
| `len(A)`, `len(A[0])` | | the number of rows, and the number of columns (the length of a row) |
| `A[i][j]` | "A at i, at j" | row `i`, then column `j` inside it |
| `return (2, 3)` | | gives back two numbers together, a **tuple** |
| `!=` | "is not equal to" | true when the two sides differ |
| `raise ValueError("…")` | | stops with an error message |
| a loop inside a loop | | for every round of the outer loop, the inner loop runs all the way through |

### 👀 Worked example: flipping a seating chart

```python
seats = [["Ann", "Bo", "Cy"],
         ["Di", "Ed", "Fay"]]
result = []
for j in range(len(seats[0])):      # j = 0, 1, 2: each column
    new_row = []
    for i in range(len(seats)):     # i = 0, 1: each row
        new_row.append(seats[i][j])
    result.append(new_row)
print(result)
```

1. `j` = 0: take column 0 from every row: `seats[0][0]` = Ann, `seats[1][0]` = Di → `["Ann", "Di"]`.
2. `j` = 1: `["Bo", "Ed"]`. `j` = 2: `["Cy", "Fay"]`.
3. `result` = `[["Ann", "Di"], ["Bo", "Ed"], ["Cy", "Fay"]]`: 3 × 2. That's the transpose.

## 🎯 Your quest

`shape(A)`: replace `return (0, 0)` with `    return (len(A), len(A[0]))`

`transpose(A)`: replace `return []` with the worked example as a function:

1. `    result = []`
2. `    for j in range(len(A[0])):`
3. `        new_row = []`
4. `        for i in range(len(A)):`
5. `            new_row.append(A[i][j])`
6. `        result.append(new_row)`
7. `    return result`

`matmul(A, B)`: replace `return []` with:

1. `    if len(A[0]) != len(B):`
2. `        raise ValueError("shape mismatch")`
3. `    columns = transpose(B)`
4. `    C = []`
5. `    for row in A:`
6. `        new_row = []`
7. `        for col in columns:`
8. `            total = 0`
9. `            for k in range(len(row)):`
10. `                total = total + row[k] * col[k]`
11. `            new_row.append(total)`
12. `        C.append(new_row)`
13. `    return C`

Lines 8 to 10 are the dot product from lesson 3. The program prints `[[7, 8], [16, 17]]` for A @ B.

## Review

<details><summary>What does RMSNorm do to a vector?</summary>Divides it by its root mean square (then scales by learned weights), keeping vector sizes stable through the layers.</details>
<details><summary>What does the dot product measure, geometrically?</summary>|a|·|b|·cos(angle): how strongly the vectors point the same way.</details>
<details><summary>Can a 4 × 3 matrix be multiplied by a 4 × 2 matrix?</summary>No: the inner numbers are 3 and 4, and they must match.</details>
