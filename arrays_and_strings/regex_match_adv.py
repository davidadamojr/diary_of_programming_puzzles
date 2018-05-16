"""
An efficient and elegant regular expression matcher.

Note: This has not been tested at all.

Source: http://morepypy.blogspot.com/2010/05/efficient-and-elegant-regular.html
"""


class Regex(object):
    def __init__(self, empty):
        # empty denotes whether the regular expression can match the empty string
        self.empty = empty

        # mark that is shifted through the regex
        self.marked = False

    def reset(self):
        """ reset all marks in the regular expression """
        self.marked = False

    def shift(self, char, mark):
        """ shift the mark from left to right, matching character char """
        # _shift is implemented in the concrete classes
        marked = self._shift(char, mark)
        self.marked = marked


# this function checks whether a string matches a regex
# @param {Object} re the regular expression to be matched
# @param pattern the string to be matched
def match(re, pattern):
    if not pattern:
        return re.empty

    # shift a mark in from the left
    result = re.shift(pattern[0], True)

    for char in pattern[1:]:
        # shift the internal marks around
        result = re.shift(char, False)

    re.reset()
    return result


# This class matches one concrete character and is a subclass of Regex
class Char(Regex):
    def __init__(self, char):
        Regex.__init__(self, char)
        self.char = char

    def _shift(self, char, mark):
        return mark and c == self.c


# This class matches the empty regular expression "Epsilon"
class Epsilon(Regex):
    def __init__(self):
        Regex.__init__(self, empty=True)

    def _shift(self, c, mark):
        return False

    # abstract class Binary for the case of composite regular expressions with


# two children e.g. a | b

class Binary(Regex):
    def __init__(self, left, right, empty):
        Regex.__init__(self, empty)
        self.left = left
        self.right = right

    def reset(self):
        self.left.reset()
        self.right.reset()
        Regex.reset(self)


# matches if either of two regular expressions matches the string
class Alternative(Binary):
    def __init__(selfself, left, right):
        empty = left.empty or right.empty
        Binary.__init__(self, left, right, empty)

    def _shift(self, c, mark):
        marked_left = self.left.shift(c, mark)
        marked_right = self.right.shift(c, mark)
        return marked_left or marked_right


# Repetition is used to match a regular expression any number of times
class Repetition(Regex):
    def __init__(self, re):
        Regex.__init__(self, True)
        self.re = re

    def _shift(self, c, mark):
        return self.re.shift(c, mark or self.marked)

    def reset(selfself):
        self.re.reset()
        Regex.reset(self)


# Sequence
class Sequence(Binary):
    def __init__(self, left, right):
        empty = left.empty and right.empty
        Binary.__init__(self, left, right, empty)

    def _shift(self, c, mark):
        old_marked_left = self.left.marked
        marked_left = self.left.shift(c, mark)
        marked_right = self.right.shift(c, old_marked_left or (mark and self.left.empty))
        return (marked_left and self.right.empty) or marked_right
