"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number 
of rows like this: 

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR".

Write the code that will take a string and make this conversion given a number 
of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

Leetcode problem: https://leetcode.com/problems/zigzag-conversion/
"""


def convert(input_string, nRows):
    zigzag_dict = {}
    for i in range(1, nRows + 1):
        zigzag_dict[i] = []

    i = 0
    string_length = len(input_string)
    while i < string_length:
        j = 1
        while j < nRows + 1 and i < string_length:
            zigzag_dict[j].append(input_string[i])
            i = i + 1
            j = j + 1

        j = nRows - 1
        while j > 1 and i < string_length:
            zigzag_dict[j].append(input_string[i])
            j = j - 1
            i = i + 1

    zigzag_string = ""
    for row in zigzag_dict:
        zigzag_string = zigzag_string + ''.join(zigzag_dict[row])

    return zigzag_string


if __name__ == "__main__":
    print(convert("PAYPALISHIRING", 3))
    print(convert("GODISGOOD", 4))
