#!/usr/bin/python3

import math


def next_perfect_square(x) -> int:
    square_root = math.isqrt(x)
    if square_root ** 2 == x:
        return x
    next_square = (square_root + 1) ** 2
    return next_square


def get_matrix(abrs: list[str]) -> list[list[float]]:
    inside_list = []
    list_str = abrs[1:]
    nbr = next_perfect_square(len(abrs[1:]))
    if len(abrs[1:]) != nbr:
        exit(84)
    for i in range(0, len(list_str), int(math.isqrt(nbr))):
        inside_list.append([float(abr) for abr in list_str[i:i + int(math.isqrt(nbr))]])
    return inside_list
