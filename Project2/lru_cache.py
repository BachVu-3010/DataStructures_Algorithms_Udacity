from collections import deque
# use double ended queue
# append() and popleft() fuctions provide 0(1) time complexity for enqueue and dequeue


class LRU_Cache(object):

    def __init__(self, max_capacity=5):
        # Initialize class variables

        self.max_capacity = max_capacity
        self.items = {}
        self.keys = deque()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        # "key in self.items.keys()" is 0(1) not 0(n) operation ?
        if key in self.keys:
            self.keys.append(key)
            self.handle_max_capacity()
            return self.items[key]

        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        # if len(self.items) == self.max_capacity:

        #     least_used_key = self.keys.popleft()

        #     self.items.pop(least_used_key)

        self.items[key] = value
        self.keys.append(key)
        self.handle_max_capacity()

    def handle_max_capacity(self):

        if len(self.keys) > 5:
            self.keys.popleft()


# Edge test cases for empty cache
our_cache = LRU_Cache(0)
print("our_cache:", our_cache, '\n')

print("--our_cache.set(1, 1)--")
our_cache.set(1, 1)  # Can't perform operations on a 0 capacity cache
print("our_cache:", our_cache, '\n')

print("--our_cache.get(1)--")
print("our_cache.get(1):", our_cache.get(1))  # returns -1
print("our_cache:", our_cache, '\n')

# General test cases
our_cache = LRU_Cache(5)
print("our_cache:", our_cache, '\n')

print("--our_cache.set(1, 1)--")
our_cache.set(1, 1)  # No return
print("our_cache:", our_cache, '\n')

print("--our_cache.set(2, 2)--")
our_cache.set(2, 2)  # No return
print("our_cache:", our_cache, '\n')

print("--our_cache.set(3, 3)--")
our_cache.set(3, 3)  # No return
print("our_cache:", our_cache, '\n')

print("--our_cache.set(4, 4)--")
our_cache.set(4, 4)  # No return
print("our_cache:", our_cache, '\n')

print("--our_cache.get(1)--")
print("our_cache.get(1):", our_cache.get(1))  # returns 1
print("our_cache:", our_cache, '\n')

print("--our_cache.get(2)--")
print("our_cache.get(2):", our_cache.get(2))  # returns 2
print("our_cache:", our_cache, '\n')

print("--our_cache.get(9)--")
# returns -1 because 9 is not present in the cache
print("our_cache.get(9):", our_cache.get(9))
print("our_cache:", our_cache, '\n')

print("--our_cache.set(5, 5)--")
our_cache.set(5, 5)  # No return
print("our_cache:", our_cache, '\n')

print("--our_cache.set(6, 6)--")
our_cache.set(6, 6)  # No return
print("our_cache:", our_cache, '\n')

print("--our_cache.get(3)--")
print("our_cache.get(3):", our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print("our_cache:", our_cache, '\n')
