#!/usr/bin/python3

from src.pass_matrix import get_matrix
from src.compute_function import *


def get_rigth_calc(matrix, func):
    if func == "EXP":
        return compute_matrix_exp(matrix)
    if func == "COS":
        return compute_matrix_cos(matrix)
    if func == "SIN":
        return compute_matrix_sin(matrix)
    if func == "COSH":
        return compute_matrix_cosh(matrix)
    if func == "SINH":
        return compute_matrix_sinh(matrix)
    return 0


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def check_arg(abrs: list[str]) -> int:
    if len(abrs) < 2:
        exit(84)
    if abrs[0] not in {"EXP", "COS", "SIN", "COSH", "SINH"}:
        exit(84)
    for arg in abrs[1:]:
        try:
            float(arg)
        except ValueError:
            exit(84)
    matrix = get_matrix(abrs)
    get_rigth_calc(matrix, abrs[0])
    return 0
