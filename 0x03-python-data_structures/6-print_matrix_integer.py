#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for items in matrix:
        for row in items:
            print("{:d}".format(row), end="")
        print()
