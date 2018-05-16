"""
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2", then "one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string

Leetcode question: https://leetcode.com/problems/count-and-say/
"""


def count_and_say(n):
    nth_str = "1"
    for i in range(2, n + 1):
        character_count = 0
        new_str = ""
        current_character = nth_str[0]
        for j in range(0, len(nth_str)):
            if nth_str[j] == current_character:
                character_count = character_count + 1
            else:
                new_str = new_str + str(character_count) + current_character
                current_character = nth_str[j]
                character_count = 1

        new_str = new_str + str(character_count) + current_character
        nth_str = new_str

    return nth_str


if __name__ == '__main__':
    print(count_and_say(5))
    print(count_and_say(7))
