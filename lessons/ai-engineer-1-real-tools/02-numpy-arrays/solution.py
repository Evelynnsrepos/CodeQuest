import numpy as np


def standardize(X):
    return (X - X.mean(axis=0)) / X.std(axis=0)


def cosine_matrix(A):
    B = A / np.linalg.norm(A, axis=1, keepdims=True)
    return B @ B.T


def most_similar(A, i):
    sims = cosine_matrix(A)[i].copy()
    sims[i] = -np.inf
    return int(sims.argmax())


X = np.array([[1.0, 200.0], [2.0, 300.0], [3.0, 400.0]])
print(standardize(X))
A = np.array([[1.0, 0.0], [0.9, 0.1], [0.0, 1.0]])
print(cosine_matrix(A).round(3), most_similar(A, 0))
