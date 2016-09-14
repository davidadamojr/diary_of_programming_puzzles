"""
Given an integer, write a function to determine if it is a power of three.

https://leetcode.com/problems/power-of-three/
"""

def is_power_of_three(number):
    while number >= 3:
        number = number / 3.0

    return number % 1 == 0

if __name__ == "__main__":
    assert is_power_of_three(20) is False
    assert is_power_of_three(15) is False
    assert is_power_of_three(81) is True
    print "All test cases passed successfully."
