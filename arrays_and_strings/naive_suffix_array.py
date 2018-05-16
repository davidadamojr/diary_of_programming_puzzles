"""
Given a string, construct its suffix array.

String comparison for sorting potentially O(n^2)

Naive implementation: O(n^2logn)
"""


def build_suffix_array(input_string):
    suffixes = {}
    for i in range(0, len(input_string)):
        suffixes[i] = input_string[i:]

    suffixes = sorted(list(suffixes.items()), key=lambda suffix: suffix[1])
    suffix_arr = [suffix[0] for suffix in suffixes]
    print(suffix_arr)


if __name__ == '__main__':
    build_suffix_array("attcatg")
