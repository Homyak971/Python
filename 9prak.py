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


with open('ЖиляковаАннаСергеевна_ЗИТ-22м_vvod.txt', 'r') as file:
    triangle_matrix = file.read()
    triangle_matrix = map(lambda x: int(x.strip()), triangle_matrix.split(','))
    triangle_matrix = list(triangle_matrix)

n = 3
matrix = restore_matrix(triangle_matrix, n)

matrix = np.array([i for i in matrix])
diag_arr = np.diag(matrix)

# Нахождение следа матрицы
matrix_trace = np.trace(matrix)

# Преобразование исходной матрицы
for i in range(matrix.shape[0]):
    if i % 2 == 0:
        matrix[i] = matrix[i] / matrix_trace



with open('ЖиляковаАннаСергеевна_ЗИТ-22м_vivod.txt', 'w') as file:
    file.write('\n'.join([''.join(str(i)) for i in matrix]))
