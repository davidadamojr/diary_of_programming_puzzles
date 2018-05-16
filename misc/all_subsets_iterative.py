"""
Write a method to return all subsets of a set
"""


# @param original_set a list of integers
def get_all_subsets(original_set):
    # iterative solution - O(2^n) where n is the size of the original set

    all_subsets = [[]]
    for element in original_set:
        subsets = []
        for subset_element in all_subsets:
            new_subset = []
            new_subset.extend(subset_element)
            new_subset.append(element)
            subsets.append(new_subset)
        all_subsets.extend(subsets)

    return all_subsets


if __name__ == '__main__':
    print(get_all_subsets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
