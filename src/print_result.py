def print_result(A: list[list[float]]) -> int:
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f"{A[i][j]:.2f}", end="")
            if j != len(A[i]) - 1:
                print("\t", end="")
        print()
    return 0
