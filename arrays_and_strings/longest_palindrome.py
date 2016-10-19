"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that
can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


def longest_palindrome(input_str):
    char_dict = {}
    for character in input_str:
        if character in char_dict:
            char_dict[character] = char_dict[character] + 1
        else:
            char_dict[character] = 1

    even_sum = 0
    odd_chars = False
    for char_key in char_dict:
        if char_dict[char_key] % 2 == 0:
            even_sum = even_sum + char_dict[char_key]
        else:
            even_sum = even_sum + (char_dict[char_key] - 1)
            odd_chars = True

    if odd_chars:
        return even_sum + 1

    return even_sum

if __name__ == '__main__':
    assert longest_palindrome("abccccdd") == 7
    assert longest_palindrome("aaaabbbcccdddeeeeee") == 17
    assert longest_palindrome("aaaabbbb") == 8
    print "All test cases passed successfully."