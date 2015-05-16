"""
A child is running up a staircase with n steps, and can hope either 1 step,
2 steps, or 3 steps at a time. Implement a method to count how many possible
ways the child can run up the stairs.
"""
map = {}

def count_ways_dp(number_of_steps):
    """
    Dynamic programming solution
    """
    if number_of_steps < 0:
        return 0

    if number_of_steps == 0:
        return 1

    if number_of_steps in map:
        return map[number_of_steps]
    else:
        map[number_of_steps] = count_ways_dp(number_of_steps-1) + count_ways_dp(number_of_steps-2) + count_ways_dp(number_of_steps-3)
        return map[number_of_steps];

