from src.matrix.matrix_sum import matrix_sum
from src.matrix.matrix_pow import matrix_pow
from math import factorial


def compute_matrix_exp(A: list[list[float]]) -> int:
    result = [[0.0] * len(A[0]) for _ in range(len(A))]

    for i in range(len(A)):
        A[i][i] = 1
    for i in range(100):
        tmp = matrix_pow(A, i)
        coef = factorial(i)
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] *= 1.0 / coef
        result = matrix_sum(result, tmp)
    return print_result(result)
