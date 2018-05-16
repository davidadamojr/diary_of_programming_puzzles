"""
Write a function that reverses the order of the words in a string. For example,
your function should transform the string "Do or do not, there is no try." to
"try. no is there not, do or Do". Assume that all words are space delimited and
treat punctuation the same as letters.
"""


def reverse_words1(string):
    """
    Build up a new reversed string
    Traverse the string from the end
    When a word is detected, traverse forward and add the word to the new 
    reverse string
    """
    if string == "":
        return ""

    new_string = ""
    string_length = len(string)
    token_read_pos = string_length - 1
    word_read_pos = 0
    word_end = 0

    while token_read_pos >= 0:
        if string[token_read_pos] == ' ':  # non word character
            # write character to buffer
            new_string = new_string + string[token_read_pos]
            token_read_pos = token_read_pos - 1
        else:  # word characters
            # store position of end of word
            word_end = token_read_pos

            # scan until next non-word character
            while token_read_pos >= 0 and string[token_read_pos] != ' ':
                token_read_pos = token_read_pos - 1

            # token_read_pos went past the start of a word
            word_read_pos = token_read_pos + 1
            while word_read_pos <= word_end:
                new_string = new_string + string[word_read_pos]
                word_read_pos = word_read_pos + 1

    return new_string


def reverse_words2(string):
    """
    split the string into words
    reverse the entire string
    then, reverse each word
    
    Example:
    "All is well" -> "llew si llA" -> "well is All"
    """

    string = string[::-1]  # reverses the string
    string_list = string.split()
    word_count = len(string_list)
    for word_index in range(0, word_count):
        # reverse each word
        word = string_list[word_index]
        reversed_word = word[::-1]
        string_list[word_index] = reversed_word

    return ' '.join(string_list)


if __name__ == '__main__':
    print(reverse_words1("All is well that ends well."))
    print(reverse_words2("All is well that ends well."))
