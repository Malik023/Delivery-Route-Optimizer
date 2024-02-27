
class HashTable:
    def __init__(self, key, value):
        # Initializes a new node with a key, value, and next pointer
        self.key = key
        self.value = value
        self.next = None

class CreateHashMap:
    def __init__(self, initial_capacity=16):
        # Creates a new hash map with a default initial capacity of 16
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [None] * initial_capacity

    def _hash_function(self, key):
        # Calculates the index in the bucket array for a given key
        return hash(key) % self.capacity

    def insert(self, key, value):
        # Inserts a key-value pair into the hash map
        # Time Complexity: O(1) (average), O(n) (worst case)
        index = self._hash_function(key)
        node = self.buckets[index]
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next
        new_node = HashTable(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node
        self.size += 1

    def lookup(self, key):
        # Looks up the value associated with a given key in the hash map
        # Time Complexity: O(1) (average), O(n) (worst case)
        index = self._hash_function(key)
        node = self.buckets[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def remove(self, key):
        # Removes the key-value pair associated with a given key from the hash map
        # Time Complexity: O(1) (average), O(n) (worst case)
        index = self._hash_function(key)
        node = self.buckets[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.buckets[index] = node.next
                self.size -= 1
                return
            prev = node
            node = node.next

