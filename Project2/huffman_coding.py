import sys

from heapq import heappush, heappop, heapify, heappushpop

# The following functions are provided:

# heapq.heappush(heap, item)
# Push the value item onto the heap, maintaining the heap invariant.

# heapq.heappop(heap)
# Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].

# heapq.heappushpop(heap, item)
# Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().

# heapq.heapify(x)
# Transform list x into a heap, in-place, in linear time.


class Node:
    def __init__(self, value=None, key=None):
        self.value = value
        self.key = key
        self.left = None
        self.right = None

    # Helper function to compare Node objects
    def __lt__(self, other):
        return self.value < other.value


def create_char_frequency(data):
    char_frequency = {}

    for char in data:
        if char not in char_frequency.keys():
            char_frequency[char] = 1
        else:
            char_frequency[char] += 1

    return char_frequency


def create_huffman_tree(data):

    char_frequency = create_char_frequency(data)

    huffman_tree = []

    # Create a min heapf from char_frequency

    for key, value in char_frequency.items():

        node = Node(value=value, key=key)
        heappush(huffman_tree, node)

    while len(huffman_tree) > 1:

        node1 = heappop(huffman_tree)
        node2 = heappop(huffman_tree)
        key = node1.key + node2.key
        value = node1.value + node2.value

        node = Node(key=key, value=value)
        node.left = node1
        node.right = node2

        heappush(huffman_tree, node)

    # print(huffman_tree[0].key)
    # print(huffman_tree[0].left.key)
    # print(huffman_tree[0].right.key)
    # print(huffman_tree[0].left.left.key)
    # print(huffman_tree[0].right.right.key)

    return huffman_tree[0]


def create_encoded_table(tree, current_code):

    encoded_table = {}

    if not tree:
        return {}

    if not tree.left and not tree.right:
        encoded_table[tree.key] = current_code

    encoded_table.update(create_encoded_table(tree.left, current_code + "0"))
    encoded_table.update(create_encoded_table(tree.right, current_code + "1"))

    return encoded_table


def huffman_encoding(data):

    huffman_tree = create_huffman_tree(data)
    encoded_table = create_encoded_table(huffman_tree, "")

    encoded_data = ""

    for char in data:
        encoded_data += encoded_table[char]

    return encoded_data, huffman_tree


def huffman_decoding(encoded_data, tree):

    current_node = tree
    decoded_data = ""

    for char in encoded_data:

        if current_node.left and char == "0":
            current_node = current_node.left

        elif current_node.right and char == "1":
            current_node = current_node.right

        if not current_node.left and not current_node.right:
            decoded_data += current_node.key
            current_node = tree

    return decoded_data


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(tree.left.key)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
