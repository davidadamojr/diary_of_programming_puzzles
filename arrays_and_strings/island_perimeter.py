"""
You are given a map in the form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there
is exactly one island (i.e. one or more connected land cells). The island does not have "lakes" (water inside that is
not connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width
and height do not exceed 100. Determine the perimeter of the island.

Example:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

 Answer: 16
"""

# def island_perimeter(grid):
#
#     total_perimeter = 0
#
#     for i in range(0, len(grid)):
#         for j in range(0, len(grid[i])):
#             cell_perimeter = 4
#
#             if grid[i][j]
