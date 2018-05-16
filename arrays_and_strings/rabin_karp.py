"""
Write an implementation of the Rabin-Karp algorithm, a string searching algorithm 
that uses hashing to find any one of a set of pattern strings in a text.

For text of length n and p patterns of combined length m
Best case running time - O(n+m)
Worst case running time is - O(nm)
Space complexity - O(p)

- Originally contributed by Nishant - https://github.com/Optimus-Nishant
"""


def rabin_karp_search(text, pattern):
    """
    Rabin karp search is best with a rolling hash algorithm
    The key to the algorithm's performance is the efficient computation of 
    hash values of the successive substrings of text.
    """

    text_length = len(text)
    pattern_length = len(pattern)
    pattern_hash = hash(pattern)
    substr_hash = hash(text[0:pattern_length])

    for i in range(0, text_length - (pattern_length - 1)):
        if pattern_hash == substr_hash:
            if pattern == text[i:i + pattern_length]:  # in case of collisions
                return i
        substr_hash = rolling_hash(i + 1, text, pattern, substr_hash)

    return None


def hash(unhashed_str):
    """This hash function uses 5 as the base for hashing"""
    hash_value = 0
    exponent = len(unhashed_str) - 1
    for character in unhashed_str:
        hash_value = hash_value + ord(character) * (5 ** exponent)
        exponent = exponent - 1

    return hash_value


def rolling_hash(start_index, text, pattern, previous_hash):
    exponent = len(pattern) - 1
    old_first = ord(text[start_index - 1])
    new_last = ord(text[start_index + exponent])
    hash_value = (5 * (previous_hash - (old_first * 5 ** exponent))) + \
                 (new_last * 5 ** 0)
    return hash_value


if __name__ == '__main__':
    print(rabin_karp_search("abracadabra", "cad"))
