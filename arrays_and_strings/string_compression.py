"""
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string "aabcccccaaa" would become
"a2b1c5a3". If the "compressed" string would not become smaller than the
original string, your method should return the original string. You can assume
the string has only upper and lower case letters (a-z)
"""


def compress_string(uncompressed_string):
    compressed_size = calc_compressed_size(uncompressed_string)
    uncompressed_size = len(uncompressed_string)
    if compressed_size >= uncompressed_size:
        return uncompressed_string

    compressed_string = ""
    count = 1
    last_char = uncompressed_string[0]

    for i in range(1, uncompressed_size):
        same_character = last_char == uncompressed_string[i]
        if same_character:
            count = count + 1
        else:
            compressed_string = compressed_string + last_char + str(count)
            last_char = uncompressed_string[i]
            count = 1

    compressed_string = compressed_string + last_char + str(count)

    return compressed_string


def calc_compressed_size(uncompressed_string):
    """
    calculates the size of the string after compression
    """
    uncompressed_length = len(uncompressed_string)
    last_char = uncompressed_string[0]
    count = 1
    size = 0

    for i in range(1, uncompressed_length):
        same_character = uncompressed_string[i] == last_char
        if same_character:
            count = count + 1
        else:
            size = size + 1 + len(str(count))
            last_char = uncompressed_string[i]
            count = 1

    size = size + 1 + len(str(count))

    return size


print(compress_string("aaabbbcccdddaaabbc"))
print(compress_string("abcdeff"))
