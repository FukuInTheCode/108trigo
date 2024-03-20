def matrix_sum(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] += B[i][j]
    return A
