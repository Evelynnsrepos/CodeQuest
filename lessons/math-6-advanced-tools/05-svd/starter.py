import math


def transpose(A):
    return A


def matmul(A, B):
    return A


def top_singular(A, steps=200):
    return 0.0, [], []


def rank1(A):
    return A


def frobenius(A):
    return 0.0


def lora_params(d, k, r):
    return 0


def full_params(d, k):
    return 0


A = [[3, 0], [4, 5]]
print(top_singular(A), rank1(A), lora_params(4096, 4096, 16), full_params(4096, 4096))
