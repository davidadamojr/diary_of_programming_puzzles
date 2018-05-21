"""
Given a non-empty string s and a dictionary wordDict containing a list 
of non-empty words, determine if s can be segmented into a space-separated 
sequence of one or more dictionary words.

Note:
- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code"

https://leetcode.com/problems/word-break/description/
"""


def can_be_segmented(a_string, word_dict):
    rightmosts, words = [0], set(word_dict)
    for i in range(1, len(a_string) + 1):
        for last_index in rightmosts:
            if a_string[last_index:i] in words:
                rightmosts.append(i)
                if i == len(a_string):
                    return True
                break

    return False

assert can_be_segmented("antelope", ["ant", "elope"]) is True
assert can_be_segmented("germane", ["germ", "mane", "man"]) is False
assert can_be_segmented("", ["dog", "cat", "walrus"]) is False
assert can_be_segmented("a", ["a", "apple"]) is True
print("All tests passed successfully.")

