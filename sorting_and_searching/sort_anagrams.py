"""
Write a method to sort an array of strings so that all the anagrams are next 
to each other
"""


def sort_strings(string_list):
    groups = {}
    for string in string_list:
        key = ''.join(sorted(string))
        if key not in groups:
            groups[key] = [string]
        else:
            groups[key].append(string)

    sorted_anagrams = []
    for key in groups:
        sorted_anagrams = sorted_anagrams + groups[key]

    return sorted_anagrams


if __name__ == '__main__':
    print(sort_strings(['bate', 'tab', 'tabe', 'bat', 'moon', 'jade', 'oscar', 'noom', 'rasco', 'mono']))
