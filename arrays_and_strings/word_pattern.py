"""
Given a "pattern" and a string "str", find if "str" follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter 
in "pattern" and a non-empty word in "str".

Examples:
1. pattern = "abba", str = "dog cat cat dog" should return true.
2. pattern = "abba", str = "dog cat cat fish" should return false.
3. pattern = "aaaa", str = "dog cat cat dog" should return false.
4. pattern = "abba", str = "dog dog dog dog" should return false.

You may assume "pattern" contains only lowercase letters, and "str" contains 
lowercase letters separated by a single space.

Leetcode question: https://leetcode.com/problems/word-pattern/
"""

#param {string} pattern the pattern to be matched
#param {string} the string to be checked 
def word_pattern(pattern, str):
    pattern_str = {}
    str_pattern = {}
    pattern_lst = list(pattern)
    str_lst = str.split()
    
    # if the number of characters in the pattern does not match each non-empty 
    # word in the string, then there is no match
    if len(pattern_lst) != len(str_lst):
        return False
    
    for key, value in zip(pattern_lst, str_lst):
        if key in pattern_str:
            if pattern_str[key] != value:
                return False
        elif value in str_pattern:
            if str_pattern[value] != key:
                return False
        else:
            pattern_str[key] = value
            str_pattern[value] = key
    
    return True

if __name__ == '__main__':
    assert(word_pattern("abba", "dog cat cat dog") == True)
    assert(word_pattern("abba", "dog cat cat fish") == False)
    assert(word_pattern("aaaa", "dog cat cat dog") == False)
    assert(word_pattern("abba", "dog dog dog dog") == False)
    assert(word_pattern("abb", "dog cat cat cat") == False)