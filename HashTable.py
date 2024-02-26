
class CreateHashMap:

    # Initialize the hash map with empty bucket lists.
    # Time Complexity: O(N)
    def __init__(self, initial_capacity=16):
        self.table = [[] for _ in range(initial_capacity)] #O(N)

    # Insert or update an item in the hash map.
    # Time Complexity: O(N)
    def insert(self, key, item):
        # Determine the bucket index using the hash function.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Update the value if the key already exists in the bucket.
        for kv in bucket_list: # O(N)
            if kv[0] == key:
                kv[1] = item
                return True

        # If the key is not found, append a new key-value pair to the bucket.
        bucket_list.append([key, item])
        return True

    # Lookup the value associated with a given key in the hash map.
    # Time Complexity: O(N)
    def lookup(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Search for the key in the bucket list.
        for kv in bucket_list: # O(N)
            if kv[0] == key:
                return kv[1]  # Return the value if the key is found.
        return None  # Return None if the key is not found.

    # Remove the key-value pair associated with a given key from the hash map.
    # Time Complexity: O(N)
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Remove the key-value pair if the key is found in the bucket.
        for kv in bucket_list: # O(N)
            if kv[0] == key:
                bucket_list.remove(kv)
                return


    def remove(self, key): # Big O(N) Time Complexity
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:# O(N)
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

