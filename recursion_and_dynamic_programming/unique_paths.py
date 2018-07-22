"""
A robot is located at the top-left corner of a m x n grid (marked "Start" in the diagram below). The robot can only
move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid
(marked "Finish" in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be? An obstacle and empty space
is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:
Input:
[
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

Output: 2

Explanation:
There is one obstacle in the middle of the 3x3 grid above. There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

https://leetcode.com/problems/unique-paths-ii/description/
"""


def unique_paths_with_obstacles(obstacle_grid):
    if obstacle_grid[0][0] == 1:
        return 0

    solutions = [[0 for _ in range(len(obstacle_grid[0]))] for _ in range(len(obstacle_grid))]
    solutions[0][0] = 1
    for i in range(len(obstacle_grid)):
        for j in range(len(obstacle_grid[0])):
            if obstacle_grid[i][j] != 1:
                if i-1 >= 0:
                    solutions[i][j] += solutions[i-1][j]

                if j-1 >= 0:
                    solutions[i][j] += solutions[i][j-1]

    return solutions[len(obstacle_grid)-1][len(obstacle_grid[0])-1]


obstacle_grid_1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
assert unique_paths_with_obstacles(obstacle_grid_1) == 2
obstacle_grid_2 = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
assert unique_paths_with_obstacles(obstacle_grid_2) == 0
print("All test cases passed successfully.")
