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
    nbr = next_perfect_square(len(abrs[1:]))
    num_sublist = int(math.sqrt(nbr))
    nbr_nul = nbr - len(abrs[1:])
    inside_list.extend(float(num_str) for num_str in abrs[1:])
    inside_list.extend([0.0] * nbr_nul)
    sublists = [inside_list[i:i + num_sublist] for i in
                range(0, len(inside_list), num_sublist)]
    return sublists
