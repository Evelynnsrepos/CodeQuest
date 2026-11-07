import numpy as np


def standardize(X):
    # means = X.mean(axis=0)
    # stds = X.std(axis=0)
    # return (X - means) / stds
    return X


def cosine_matrix(A):
    # lengths = np.linalg.norm(A, axis=1, keepdims=True)
    # B = A / lengths
    # return B @ B.T
    return A


def most_similar(A, i):
    # sims = cosine_matrix(A)[i].copy()
    # sims[i] = -np.inf
    # return int(sims.argmax())
    return 0


X = np.array([[1.0, 200.0], [2.0, 300.0], [3.0, 400.0]])
print(standardize(X))
A = np.array([[1.0, 0.0], [0.9, 0.1], [0.0, 1.0]])
print(cosine_matrix(A).round(3), most_similar(A, 0))
