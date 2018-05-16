"""
Given a non-negative integer number "num". For every numbers i in the range 0<=i<=num, calculate the number of 1's in
their binary representation and return them as an array.

Example:
For num = 5, you should return [0,1,1,2,1,2]

Follow up:
- It is very easy to come up with a solution with run time O(n*sizeof(integer)). But you can do it in linear time O(n),
possibly in a single pass?
- Space complexity should be O(n).
"""


def count_bits(num):
    """O(num*sizeof(int)) implementation"""
    lst_ones = []
    for i in range(0, num + 1):
        num_of_ones = 0
        while i > 0:
            if i & 1 == 1:
                num_of_ones += 1

            i >>= 1
        lst_ones.append(num_of_ones)

    return lst_ones


def count_bits_linear_time(num):
    "O(num) implementation"

    lst_ones = [0 for i in range(0, num + 1)]
    for i in range(1, num + 1):
        lst_ones[i] = lst_ones[i >> 1] + (i & 1)

    return lst_ones


if __name__ == "__main__":
    assert count_bits(7) == [0, 1, 1, 2, 1, 2, 2, 3]
    assert count_bits(12) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2]
    assert count_bits_linear_time(7) == [0, 1, 1, 2, 1, 2, 2, 3]
    assert count_bits_linear_time(12) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2]

    print("All test cases passed successfully.")
