class Hashtable:
    """Implements a hashtable class with methods for adding, retrieving,
    checking existence, and listing keys, along with a simple hash function.
    """
    def __init__(self, size=10):
        """Initializes the hashtable with a specified size and creates
        an array of empty lists (buckets) for handling collisions.

        :param `size`: The size of the hashtable (default: 10).
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        """Generates a hash value for a given key.

        :param `key`: The key to hash.
        :returns: An integer representing the hash value of the key.
        """
        return sum(ord(char) for char in key) % self.size

    def set(self, key, value):
        """Sets a key-value pair in the hashtable. If the key already exists,
        its value is updated with the provided value.

        :param `key`: The key for the data.
        :param `value`: The value to be associated with the key.
        """
        index = self.hash(key)
        found = False
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                found = True
                break
        if not found:
            self.table[index].append((key, value))

    def get(self, key):
        """Retrieves the value associated with a given key.

        :param `key`: The key for which the value is to be retrieved.
        :returns: The value associated with the key, or None if the key is not found.
        """
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def has(self, key):
        """Checks if a given key exists in the hashtable.

        :param `key`: The key to check.
        :returns: True if the key exists, False otherwise.
        """
        index = self.hash(key)
        for k, _ in self.table[index]:
            if k == key:
                return True
        return False

    def keys(self):
        """Returns a collection of all keys in the hashtable.

        :returns: A list of all keys.
        """
        keys_list = []
        for bucket in self.table:
            keys_list.extend([k for k, _ in bucket])
        return keys_list

    def _buckets(self):
        """A helper method for displaying the internal structure of the hashtable,
        primarily for testing and debugging purposes.

        :returns: A list of dictionaries representing the display function for each bucket.
        """
        return [{'display': lambda bucket=bucket: [(k, v) for k, v in bucket]} for bucket in self.table if bucket]
