#!/usr/bin/env python3
"""
Basic caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache: inherits from BaseCaching and it's caching system

    Logic:
        - basic caching system that doesn't discard any item.
        - store in the cache the newest item with no limit.

    Implements put and get methods:
        - put(key, item):
            assign to the dictionary self.cache_data the item value.
        - get(key): return the value in self.cache_data using the key.
    """

    def __init__(self):
        """Initialize class BasicCache"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
