"""
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each 
letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9, 7, 8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect because it splits S into less parts.

Note:
1. S will have length in range [1, 5000].
2. S will consist of lowercase letters {'a' to 'z'} only.

https://leetcode.com/problems/partition-labels/description/
"""


def partition_labels(str_to_be_partitioned):
    last_occurrence = {c: i for i, c in enumerate(str_to_be_partitioned)}
    partition_sizes = []
    left_partition_idx = 0
    right_partition_idx = 0
    for i in range(len(str_to_be_partitioned)):
        current_char = str_to_be_partitioned[i]
        char_last_occurrence_idx = last_occurrence[current_char]
        if char_last_occurrence_idx > right_partition_idx:
            right_partition_idx = char_last_occurrence_idx

        if i == right_partition_idx:
            partition_sizes.append(len(str_to_be_partitioned[left_partition_idx:right_partition_idx + 1]))
            left_partition_idx = i + 1
            right_partition_idx = i + 1

    return partition_sizes

assert partition_labels("a") == [1]
assert partition_labels("ab") == [1, 1]
assert partition_labels("aabb") == [2, 2]
assert partition_labels("aaaaaaa") == [7]
assert partition_labels("") == []
print("All tests passed successfully.")
