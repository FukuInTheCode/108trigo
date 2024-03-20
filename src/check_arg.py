#!/usr/bin/python3


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
    return 0
