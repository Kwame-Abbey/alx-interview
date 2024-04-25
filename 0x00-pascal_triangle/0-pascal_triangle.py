#!/usr/bin/python3
"""Defines an algorithm for Pascal's Triangle"""


def pascal_triangle(n):
    """An algorithm for solving pascal's triangle
    Args:
        n (int): Number of rows to be generated
    Returns:
        a list of lists of integers
    """
    if n <= 0:
        return []

    rows = []
    for i in range(n):
        rows.append([])
        rows[i].append(1)
        if i > 0:
            for j in range(1, i):
                rows[i].append(rows[i - 1][j - 1] + rows[i - 1][j])
            rows[i].append(1)
    return rows
