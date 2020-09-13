# Represents a single node in the Trie
class TrieNode:
    def __init__(self, prefix: str = ""):
        # Initialize this node in the Trie
        self.prefix = prefix
        self.children = {}
        self.isWord = False

    # def insert(self, char):
    #     # Add a child node in this Trie

    #     self.children[char] = TrieNode(char)

    def suffixes(self, suffix=''):
        suffixes = []

        for char, TrieNode in self.children.items():
            if TrieNode.isWord:
                suffixes.append(suffix + char)
            if TrieNode.children:
                suffixes.extend(TrieNode.suffixes(suffix + char))

        return suffixes

        # Recursive function that collects the suffix for
        # all complete words below this point

        # The Trie itself containing the root node and insert/find functions


class Trie:
    def __init__(self):
        # Initialize this Trie (Trie always starts with an empty string)
        self.root = TrieNode("")

    def insert(self, word):
        # Add a word to the Trie
        current = self.root
        for index, char in enumerate(word):
            if char not in current.children:

                # Slicing does not contain the last index
                prefix = word[0:index + 1]
                current.children[char] = TrieNode(prefix)
                current = current.children[char]
            else:

                current = current.children[char]

        current.isWord = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return current


def test(prefix):
    # if prefix != '':
    prefix_node = MyTrie.find(prefix)
    print(prefix + ".suffixes():")
    if prefix_node:
        print(prefix_node.suffixes())
    else:
        print(prefix + " not found")
    print('')


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    MyTrie.insert(word)

print("Word List:", wordList, '\n')

test('')
# expected output: ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory',
# 'trie', 'trigger', 'trigonometry', 'tripod']

test('f')
# expected output: ['un', 'unction', 'actory']
test('an')
# expected output: ['t', 'thology', 'tagonist', 'tonym']

test('ant')
# expected output: ['hology', 'agonist', 'onym']

test('tripod')
# expected output: []
