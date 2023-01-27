import numpy as np
def restore_matrix(triangle_matrix, n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = triangle_matrix[index]
            matrix[j][i] = triangle_matrix[index]
            index += 1
    return matrix

triangle_matrix = [1, 2, 3, 4, 5, 6]
n = 3
matrix = restore_matrix(triangle_matrix, n)
print(*[i for i in matrix], sep='\n')
matrix = np.array([i for i in matrix])
diag_arr = np.diag(matrix)

matrix_trace = np.trace(matrix)

for i in range(matrix.shape[0]):
    if i % 2 == 0:
        matrix[i] = matrix[i] / matrix_trace

print(matrix)
