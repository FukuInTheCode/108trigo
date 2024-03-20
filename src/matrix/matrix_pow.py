from src.matrix.matrix_dot import matrix_dot


def matrix_pow(matrix: list[list[float]], power: int) -> list[list[float]]:
    if power == 0:
        n = len(matrix)
        return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    elif power == 1:
        return matrix
    elif power % 2 == 0:
        half_power = matrix_pow(matrix, power // 2)
        return matrix_dot(half_power, half_power)
    else:
        return matrix_dot(matrix, matrix_pow(matrix, power - 1))
