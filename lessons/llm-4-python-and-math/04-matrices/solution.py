def shape(A):
    return (len(A), len(A[0]))


def transpose(A):
    result = []
    for j in range(len(A[0])):
        new_row = []
        for i in range(len(A)):
            new_row.append(A[i][j])
        result.append(new_row)
    return result


def matmul(A, B):
    if len(A[0]) != len(B):
        raise ValueError("shape mismatch")
    columns = transpose(B)
    C = []
    for row in A:
        new_row = []
        for col in columns:
            total = 0
            for k in range(len(row)):
                total = total + row[k] * col[k]
            new_row.append(total)
        C.append(new_row)
    return C


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
