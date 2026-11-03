def shape(A):
    return (0, 0)


def transpose(A):
    return []


def matmul(A, B):
    return []


A = [[1, 2, 3],
     [4, 5, 6]]
B = [[1, 0],
     [0, 1],
     [2, 2]]
print(shape(A), "@", shape(B))
print(transpose(A))
print(matmul(A, B))
try:
    matmul(A, A)
except ValueError as e:
    print("A @ A:", e)
