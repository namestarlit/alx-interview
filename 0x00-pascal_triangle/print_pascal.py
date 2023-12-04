#!/usr/bin/env python3
"""
Program to display Pascal's Triangle.

For details about what a Pascal's Triangle is visit
ref: https://en.wikipedia.org/wiki/Pascal%27s_triangle

"""
from sys import argv


def print_pascal(n: int):
    """Prints a Pascal's Triangle

    Args:
        n (int); The number of lines of a Pascal's triangle

    Returns:
        list vector: A list of lists representing a Pascal's Triangle
        list: An empty list if n is negative integer or zero

    """
    # Check if n is a negative integer or zero
    if n <= 0:
        return []

    for line in range(1, n + 1):
        c = 1  # used to represent c(line, 1)
        for i in range(1, line + 1):
            print(c, end=" ")
            c = int(c * (line - i) / i)
        print("")


if __name__ == '__main__':
    num = int(argv[1])
    print_pascal(num)
