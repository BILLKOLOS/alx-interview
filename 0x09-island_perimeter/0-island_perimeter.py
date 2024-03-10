#!/usr/bin/python3
"""This module contain a function that returns the perimeter of an
   islan described in a grid
"""


def island_perimeter(grid):
    """Function returns the perimeter of the island
    described in grid"""
    perimeter = 0
    connection = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                perimeter += 4
                if row != 0 and grid[row - 1][col] == 1:
                    connection += 1
                if col != 0 and grid[row][col - 1] == 1:
                    connection += 1
    return perimeter - (connection * 2)
