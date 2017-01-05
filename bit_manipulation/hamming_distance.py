"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers num1 and num2, calculate the Hamming distance.

https://leetcode.com/problems/hamming-distance/
"""

#@param num1 integer
#@param num2 integer
def hamming_distance(num1, num2):
    distance = 0
    while num1 > 0 and num2 > 0:
        xor = num1 ^ num2
        if xor % 2 == 1:
            distance = distance + 1

        num1 = num1 >> 1
        num2 = num2 >> 1

    while num1 > 0:
        xor = num1 ^ 0
        if xor % 2 == 1:
            distance = distance + 1

        num1 = num1 >> 1

    while num2 > 0:
        xor = num2 ^ 0
        if xor % 2 == 1:
            distance = distance + 1

        num2 = num2 >> 1

    return distance

if __name__ == '__main__':
    assert hamming_distance(1, 4) == 2
    assert hamming_distance(0, 0) == 0
    assert hamming_distance(8, 4) == 2
    assert hamming_distance(4, 8) == 2
    print "All test cases passed successfully."