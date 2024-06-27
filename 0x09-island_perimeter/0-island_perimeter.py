#!/usr/bin/python3
""" Module 5-island_perimeter contains function island_perimeter """


def island_perimeter(grid):
    """
    Finds perimeter of island described in grid

    Args:
        grid - list of list on integers

    Returns:
        Perimeter of island
   """
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    count += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    count += 1
                if j == 0 or grid[i][j - 1] == 0:
                    count += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    count += 1
    return count
