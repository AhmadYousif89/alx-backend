#!/usr/bin/env python3
"""
MRU Caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that implements Most Recently Used (MRU) caching strategy.
    Inherits from BaseCaching and overrides put and get methods.

    MRU Caching system implemented using a dictionary lookup
    and a key for storing the data in the cache system, by marking
    the cached item as most recently used when inserted or accessed.

    The search and shift time complexity is O(1) for both put and get methods.
    """

    def __init__(self):
        """Initialize the MRUCache"""
        super().__init__()
        self.mru_key = None

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        # If the key is already in cache
        # update the item and mark it as most recently used
        if key in self.cache_data:
            self.cache_data[key] = item
            self.mru_key = key
        else:
            # If cache is full, discard the most recently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                del self.cache_data[self.mru_key]
                print(f"DISCARD: {self.mru_key}")
        # Add the new item to the cache and mark it as most recently used
        self.cache_data[key] = item
        self.mru_key = key

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        # Mark the accessed item as most recently used
        self.mru_key = key
        return self.cache_data[key]
