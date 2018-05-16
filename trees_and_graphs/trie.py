class TrieNode:
    def __init__(self, words=0, prefixes=0):
        self.words = words
        self.prefixes = prefixes

        # children representing all 26 English alphabets
        self.nodes = [None for _ in range(0, 26)]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # adds the given word to the trie
    # @param String word the word to be added
    def add_word(self, word):
        word = word.lower()
        current_vertex = self.root

        for char in word:
            char_num = ord(char) - ord('a')
            child_node = current_vertex.nodes[char_num]
            if child_node:
                child_node.prefixes = child_node.prefixes + 1
            else:
                child_node = TrieNode()
                child_node.prefixes = child_node.prefixes + 1
                current_vertex.nodes[char_num] = child_node

            current_vertex = child_node

        current_vertex.words = current_vertex.words + 1

    # determines if the given word exists in the trie
    # @param String word the word to find
    # @return True if word exists False if not
    def find_word(self, word):
        word = word.lower()
        current_vertex = self.root

        for char in word:
            char_num = ord(char) - ord('a')
            if not current_vertex.nodes[char_num]:
                return False

            current_vertex = current_vertex.nodes[char_num]

        found_word = True if current_vertex.words else False
        return found_word

    # determines if there is any word in the trie that starts with the given prefix
    def starts_with(self, prefix):
        prefix = prefix.lower()
        current_vertex = self.root
        for char in prefix:
            char_num = ord(char) - ord('a')
            if not current_vertex.nodes[char_num]:
                return False

            current_vertex = current_vertex.nodes[char_num]

        return True

    # determines the number of words in the dictionary that start with a certain prefix
    def count_prefixes(self, prefix):
        prefix = prefix.lower()
        current_vertex = self.root
        for char in prefix:
            char_num = ord(char) - ord('a')
            if not current_vertex.nodes[char_num]:
                return 0

            current_vertex = current_vertex.nodes[char_num]

        return current_vertex.prefixes


if __name__ == '__main__':
    test_trie = Trie()
    test_trie.add_word("Camera")
    test_trie.add_word("manger")
    test_trie.add_word("man")
    test_trie.add_word("mango")
    test_trie.add_word("camcorder")

    # find_word
    assert test_trie.find_word("Camera") == True
    assert test_trie.find_word("Dungeon") == False
    assert test_trie.find_word("") == False

    # starts_with
    assert test_trie.starts_with("Cam") == True
    assert test_trie.starts_with("") == True
    assert test_trie.starts_with("glob") == False

    # count_prefixes
    assert test_trie.count_prefixes("man") == 3
    assert test_trie.count_prefixes("pac") == 0
    assert test_trie.count_prefixes("") == 0
    print("All tests passed")
