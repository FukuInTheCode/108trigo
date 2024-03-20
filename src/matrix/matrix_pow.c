def matrix_pow(matrix: list[list[float]], power: int) -> list[list[float]]:
    if power == 0:
        # Identity matrix
        n = len(matrix)
        return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    elif power == 1:
        return matrix
    elif power % 2 == 0:
        # If power is even, M^power = (M^(power//2))^2
        half_power = matrix_pow(matrix, power // 2)
        return matrix_dot(half_power, half_power)
    else:
        # If power is odd, M^power = M * M^(power-1)
        return matrix_dot(matrix, matrix_pow(matrix, power - 1))

