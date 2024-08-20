#!/usr/bin/python3
"""
LIFO caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache: Inherits from BaseCaching and its caching system

    Logic:
        - store the cached keys in a Stack to manage the LIFO order.
        - discard the oldest item when the cache hits the MAX_ITEMS limit.
        - print the word "DISCARD:" with the key that got discarded.

    Implement:
        - def put(self, key, item):
            assigns to the dictionary self.cache_data the item value.
        - def get(self, key):
            returns the value in self.cache_data using the key.
    """

    def __init__(self):
        """Initiliaze LIFOCache instance"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value
        """
        if key is None or item is None:
            return

        if (
            len(self.cache_data) >= BaseCaching.MAX_ITEMS
            and key not in self.cache_data
        ):
            discard_key = self.stack.pop()
            del self.cache_data[discard_key]
            print('DISCARD:', discard_key)

        if key in self.cache_data:
            self.stack.remove(key)

        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data using the key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
