"""
Compare two version numbers "version1" and "version2".capitalize

If "version1" > "version2" return 1, if "version1" < "version2" return -1, 
otherwise return 0.

You may assume that the version strings are non-empty and contain only digits 
and the "." character.

The "." character does not represent a decimal point and is used to separate 
number sequences.

For instance, "2.5" is not "two and a half" or "half way to version three", it 
is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

Leetcode problem: https://leetcode.com/problems/compare-version-numbers/
"""


def compare_version(version1, version2):
    version1seq = version1.split(".")
    version2seq = version2.split(".")

    version1length = len(version1seq)
    version2length = len(version2seq)

    i = 0
    j = 0
    while i < version1length and j < version2length:
        if int(version1seq[i]) < int(version2seq[j]):
            return -1
        elif int(version1seq[i]) > int(version2seq[j]):
            return 1

        i = i + 1
        j = j + 1

    while i < version1length:
        if int(version1seq[i]) != 0:
            return 1

        i = i + 1

    while j < version2length:
        if int(version2seq[j]) != 0:
            return -1
        j = j + 1

    return 0


if __name__ == '__main__':
    print(compare_version("2.1.0", "2.1"))
    print(compare_version("10.1", "9.2.8"))
    print(compare_version("10.2", "10.4"))
