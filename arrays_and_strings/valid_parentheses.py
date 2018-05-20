"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same tpe of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
"""


def valid_parentheses(string_to_validate):
    character_map = {'(': ')', '{': '}', '[': ']'}
    stack = []
    string_is_valid = True
    for character in string_to_validate:
        if character in character_map:
            stack.append(character)
        else:
            if not stack:
                return False

            top = stack.pop()
            if character_map[top] != character:
                return False

    if not stack:
        return True

    return string_is_valid

assert valid_parentheses("()") is True
assert valid_parentheses("{{(())}}[]") is True
assert valid_parentheses("") is True
assert valid_parentheses("[[[}}}") is False
assert valid_parentheses("{]") is False
print("All tests passed successfully.")
