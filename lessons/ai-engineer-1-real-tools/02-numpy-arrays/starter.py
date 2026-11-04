import numpy as np


def standardize(X):
    return X


def cosine_matrix(A):
    return A


def most_similar(A, i):
    return 0


X = np.array([[1.0, 200.0], [2.0, 300.0], [3.0, 400.0]])
print(standardize(X))
A = np.array([[1.0, 0.0], [0.9, 0.1], [0.0, 1.0]])
print(cosine_matrix(A).round(3), most_similar(A, 0))
