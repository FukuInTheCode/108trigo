from src.matrix.matrix_sum import matrix_sum
from src.matrix.matrix_pow import matrix_pow
from math import factorial
from src.print_result import print_result


def compute_matrix_exp(A: list[list[float]]) -> int:
    result = [[0.0] * len(A[0]) for _ in range(len(A))]

    for it in range(20):
        tmp = matrix_pow(A, it)
        coef = factorial(it)
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] *= 1.0 / coef
        result = matrix_sum(result, tmp)
    return print_result(result)


def compute_matrix_sinh(A: list[list[float]]) -> int:
    result = [[0.0] * len(A[0]) for _ in range(len(A))]

    for it in range(20):
        tmp = matrix_pow(A, 2 * it + 1)
        coef = factorial(2 * it + 1)
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] *= 1.0 / coef
        result = matrix_sum(result, tmp)
    return print_result(result)


def compute_matrix_cosh(A: list[list[float]]) -> int:
    result = [[0.0] * len(A[0]) for _ in range(len(A))]

    for it in range(20):
        tmp = matrix_pow(A, 2 * it)
        coef = factorial(2 * it)
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] *= 1.0 / coef
        result = matrix_sum(result, tmp)
    return print_result(result)


def compute_matrix_cos(A: list[list[float]]) -> int:
    result = [[0.0] * len(A[0]) for _ in range(len(A))]

    for it in range(20):
        tmp = matrix_pow(A, 2 * it)
        coef = factorial(2 * it)
        coef2 = pow(-1.0, it)
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] *= coef2 / coef
        result = matrix_sum(result, tmp)
    return print_result(result)


def compute_matrix_sin(A: list[list[float]]) -> int:
    result = [[0.0] * len(A[0]) for _ in range(len(A))]

    for it in range(20):
        tmp = matrix_pow(A, 2 * it + 1)
        coef = factorial(2 * it + 1)
        coef2 = pow(-1.0, it)
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] *= coef2 / coef
        result = matrix_sum(result, tmp)
    return print_result(result)
