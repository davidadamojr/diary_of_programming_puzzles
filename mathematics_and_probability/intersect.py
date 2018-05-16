"""
Given two lines on a Cartesian plane, determine whether the two lines would 
intersect.
"""


class Line:
    def __init__(self, slope, yIntercept):
        self.slope = slope
        self.yIntercept = yIntercept


def intersect(line1, line2):
    """
    If two different lines are not parallel, then they intersect.
    To check if two lines intersect, we just need to check if the slopes are 
    different (or if the lines are identical)
    
    Note: Due to the limitations of floating point representations, never check 
    for equality with ==. Instead, check if the difference is less than an 
    epsilon value.
    """
    epsilon = 0.000001  # used for floating point comparisons
    return abs(line1.slope - line2.slope) > epsilon \
           or abs(line1.yIntercept - line2.yIntercept) < epsilon;


if __name__ == '__main__':
    line1 = Line(0.5, 1)
    line2 = Line(0.5, 2)
    print(intersect(line1, line2))
