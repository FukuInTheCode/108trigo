from src.matrix.matrix_sum import matrix_sum
from src.matrix.matrix_pow import matrix_pow
from math import factorial
from src.print_result import print_result


def compute_matrix_exp(A: list[list[float]]) -> int:
    result = [[0.0] * len(A[0]) for _ in range(len(A))]

    for it in range(100):
        tmp = matrix_pow(A, it)
        coef = factorial(it)
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] *= 1.0 / coef
        result = matrix_sum(result, tmp)
    return print_result(result)


def compute_matrix_sinh(A: list[list[float]]) -> int:
    result = [[0.0] * len(A[0]) for _ in range(len(A))]

    for it in range(1, 100, 2):
        tmp = matrix_pow(A, it)
        coef = factorial(it)
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] *= 1.0 / coef
        result = matrix_sum(result, tmp)
    return print_result(result)


def compute_matrix_cosh(A: list[list[float]]) -> int:
    result = [[0.0] * len(A[0]) for _ in range(len(A))]

    for it in range(0, 100, 2):
        tmp = matrix_pow(A, it)
        coef = factorial(it)
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] *= 1.0 / coef
        result = matrix_sum(result, tmp)
    return print_result(result)


def compute_matrix_cos(A: list[list[float]]) -> int:
    result = [[0.0] * len(A[0]) for _ in range(len(A))]
    coef2 = -1.0

    for it in range(0, 100, 2):
        tmp = matrix_pow(A, it)
        coef = factorial(it)
        coef2 *= -1.0
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] *= coef2 / coef
        result = matrix_sum(result, tmp)
    return print_result(result)


def compute_matrix_sin(A: list[list[float]]) -> int:
    result = [[0.0] * len(A[0]) for _ in range(len(A))]
    coef2 = -1.0

    for it in range(1, 100, 2):
        tmp = matrix_pow(A, it)
        coef = factorial(it)
        coef2 *= -1.0
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] *= coef2 / coef
        result = matrix_sum(result, tmp)
    return print_result(result)
