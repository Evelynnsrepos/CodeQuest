def shape(A):
    return (len(A), len(A[0]))


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def matmul(A, B):
    if len(A[0]) != len(B):
        raise ValueError("shape mismatch")
    columns = transpose(B)
    return [[sum(a * b for a, b in zip(row, col)) for col in columns] for row in A]


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
