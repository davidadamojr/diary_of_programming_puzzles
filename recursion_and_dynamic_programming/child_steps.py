"""
A child is running up a staircase with n steps, and can hope either 1 step,
2 steps, or 3 steps at a time. Implement a method to count how many possible
ways the child can run up the stairs.
"""

def count_ways(number_of_steps):
    """
    The total number of ways of reaching the last step is therefore the
    sum of the number of ways of reaching the last three steps
    This solution is O(3^N) since there are three recursive calls at each level
    """
    if number_of_steps < 0:
        return 0

    if number_of_steps == 0:
        return 1

    return count_ways(number_of_steps-1) + count_ways(number_of_steps-2) + \
        count_ways(number_of_steps-3)





