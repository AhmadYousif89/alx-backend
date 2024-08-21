#!/usr/bin/env python3
"""
LFU Caching module
"""

from collections import defaultdict, OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFU (Least Frequency Used) Caching system that implements
    the put and get methods using dictionary look ups for tracking
    the frequency of use of the cache data.
    """

    def __init__(self):
        """Initialize the LFUCache"""
        super().__init__()
        # e.g. {1: {key1: None}, 2: {key2: None}}
        self.freq = defaultdict(OrderedDict)
        self.key_freq = {}  # e.g. {key1: 1, key2: 2}
        self.min_freq = 0

    def put(self, key, item):
        """Add an item in the LFUCache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.get(key)  # Increase the frequency of the key
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # extracts the LFU key that has the min freq value
            lfu_key, _ = self.freq[self.min_freq].popitem(last=False)
            # check if all keys with this frequency key have been removed
            if not self.freq[self.min_freq]:
                # remove the orderdict itself from the freq dict
                del self.freq[self.min_freq]
            del self.cache_data[lfu_key]
            del self.key_freq[lfu_key]
            print("DISCARD:", lfu_key)
        # Add the new key to the cache
        self.cache_data[key] = item
        # Add new key with frequency of 1 and value of None
        self.key_freq[key] = 1
        self.freq[1][key] = None
        # Reset the min frequency to 1 because we add a new item
        self.min_freq = 1

    def get(self, key):
        """Get an item from the LFUCache"""
        if key is None or key not in self.cache_data:
            return None

        freq = self.key_freq[key]
        del self.freq[freq][key]

        if not self.freq[freq]:
            del self.freq[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        self.key_freq[key] = freq + 1
        self.freq[freq + 1][key] = None
        return self.cache_data[key]
