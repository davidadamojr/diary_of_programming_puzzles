"""
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these
N numbers successfully if one of the following is true for the ith position (1<=i<=N) in this array:

1. The number at the ith position is divisible by i.
2. i is divisible by the number at the ith position.

Now, given N, how many beautiful arrangements can you construct?

"""


def count_arrangements(n):
    numbers = [num for num in range(1, n + 1)]
    arrangement = [0 for _ in range(1, n + 1)]
    count = 0
    used = {}

    def make_arrangement(current_pos, n):
        nonlocal count
        if current_pos > n:
            count += 1
            return

        for number in numbers:
            if number in used and used[number]:
                continue

            if number % current_pos == 0 or current_pos % number == 0:
                arrangement[current_pos-1] = number
                used[number] = True
                make_arrangement(current_pos+1, n)

            used[number] = False

    make_arrangement(1, n)

    return count


assert count_arrangements(2) == 2
assert count_arrangements(1) == 1
print("All tests passed successfully.")

