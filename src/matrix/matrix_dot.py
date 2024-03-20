def matrix_dot(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    if len(matrix1[0]) != len(matrix2):
        raise ValueError(
            "Number of columns in the first matrix must be equal to the number of rows in the second matrix."
        )

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0.0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)

    return result
