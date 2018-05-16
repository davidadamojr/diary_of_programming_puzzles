"""
Write a method to return all subsets of a set
"""

all_subsets = [[]]


# @param original_set a list of integers
def get_all_subsets(original_set, n):
    # recursive solution - O(2^n) where n is the size of the original set

    if n >= len(original_set):
        return

    new_subsets = []
    for subset in all_subsets:
        new_subset = []
        new_subset.extend(subset)
        new_subset.append(original_set[n])
        new_subsets.append(new_subset)
    all_subsets.extend(new_subsets)
    get_all_subsets(original_set, n + 1)


if __name__ == '__main__':
    get_all_subsets([1, 2, 3, 4, 5], 0)
    print(all_subsets)
