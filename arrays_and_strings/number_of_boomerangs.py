"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the
distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range
[-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

https://leetcode.com/problems/number-of-boomerangs/
"""


# @param points list of pairwise distinct points
def number_of_boomerangs(points):
    result = 0
    for point in points:
        equidistant_points = {}
        for other_point in points:
            distance = get_distance(point, other_point)
            equidistant_points[distance] = equidistant_points.get(distance, 0) + 1

        for distance in equidistant_points:
            # The number of ways you can pick two items from a set of n items is n*(n-1)
            result = result + (equidistant_points[distance] * (equidistant_points[distance]-1))

    return result


def get_distance(point1, point2):
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]

    return dx*dx + dy*dy

if __name__ == '__main__':
    assert number_of_boomerangs([]) == 0
    assert number_of_boomerangs([[0,0],[1,0],[2,0]]) == 2
    assert number_of_boomerangs([[0,0],[1,0],[2,0],[0,2]]) == 4
    print "All test cases passed successfully."

