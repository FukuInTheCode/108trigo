def matrix_scalar(matrix: list[list[float]], x: float) -> list[list[float]]:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= x
    return matrix
