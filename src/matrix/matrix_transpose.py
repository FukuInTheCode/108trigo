def matrix_transpose(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    transposed_matrix = [[0] * num_rows for _ in range(num_cols)]
    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix
