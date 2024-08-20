#!/usr/bin/env python3
"""
FIFO caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache: inherits from BaseCaching and is a caching system

    Logic:
        - store the cached keys in a Queue to manage the FIFO order.
        - discard the oldest item when the cache hits the MAX_ITEMS limit.
        - print the word "DISCARD:" with the key that got discarded.

    Implements the put and get methods:
        - put(key, item):
            assign to the dictionary self.cache_data the item value.
        - get(key): return the value in self.cache_data using the key.
    """

    def __init__(self):
        """Initialize class FIFOCache"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add key/value pair to the cache data"""
        if key is None or item is None:
            return

        # maintain the queue DS in sync with the cache_data
        if key in self.cache_data:
            print('Cache hit:', key)
            self.queue.remove(key)
        # append the new key to the queue and update the cache data
        self.queue.append(key)
        self.cache_data[key] = item
        # discard the oldest item when the cache hits its limit
        if len(self.cache_data) > self.MAX_ITEMS:
            diskey = self.queue.pop(0)
            self.cache_data.pop(diskey)
            print('DISCARD:', diskey)

    def get(self, key):
        """Get a value from cache by key"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
