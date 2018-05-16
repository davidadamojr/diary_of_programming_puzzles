"""
Write a program to match a pattern with a regular expression.
If there is a match, your program returns true, else it returns false.
For example,
regex = "ab*" and pattern ="abb" should return true.
Assume the regular expression can only contain alphabets and *
"""


def regex_match(regex, pattern):
    if len(pattern) == 0:
        return True

    if len(regex) == 0 and len(pattern) != 0:
        return False

    if len(regex) > 1 and regex[1] == "*":
        pattern = match_star(pattern[0], pattern)
        regex = regex[2:]
        return regex_match(regex, pattern)
    else:
        if not match_chr(regex[0], pattern[0]):
            return False
        else:
            return regex_match(regex[1:], pattern[1:])


def match_chr(regex_chr, pattern_chr):
    return regex_chr == pattern_chr


def match_star(character, pattern_substr):
    while pattern_substr and pattern_substr[0] == character:
        pattern_substr = pattern_substr[1:]

    return pattern_substr


if __name__ == '__main__':
    assert regex_match("ab*", "abb") == True
    assert regex_match("ab*", "ab") == True
    assert regex_match("ab*", "a") == True
    assert regex_match("ab*", "abc") == False
    assert regex_match("a*b", "b") == True
    assert regex_match("a*b", "ab") == True
    assert regex_match("a*b", "aaaaaaaaaaab") == True
    assert regex_match("a*b", "cabc") == False
    print("All tests passed successfully.")
