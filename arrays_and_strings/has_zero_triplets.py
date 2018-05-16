"""
Given an array of integers that do not contain duplicate values, 
determine if there exists any triplets that sum up to zero.

For example, 

L = [-3, 2, -5, 8, -9, -2, 0, 1]
e = {-3, 2, 1}
return true since e exists

This solution uses a hash table to cut the time complexity down by n.
Time complexity: O(n^2)
Space complexity: O(n)

Hint: a+b+c = 0 => c = -(a+b)
Once we know the first two elements of the triplet, we can compute the third 
and check its existence in a hash table.
"""


# @param arr the list of integers to be checked for zero triples
# @return true if three elements exist that sum up to zero
def has_zero_triplet(arr):
    if not arr:
        return False

    numbers = set([])
    for number in arr:
        numbers.add(number)

    for i in range(0, len(arr) - 1):
        for j in range(i, len(arr)):
            first = arr[i]
            second = arr[j]
            third = -first - second
            if third in numbers:
                return True

    return False


if __name__ == '__main__':
    print(has_zero_triplet([-3, 2, -5, 8, -9, -2, 0, 1]))
