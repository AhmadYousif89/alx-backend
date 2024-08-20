#!/usr/bin/env python3
"""
LRU Caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class Node:
    """Doubly Linked List Node"""

    def __init__(self, key, value):
        """Initialize the node"""
        self.key = key
        self.value = value
        self.prev: None | Node = None
        self.next: None | Node = None

    def __repr__(self):
        """Return the string representation of the node"""
        return self.value


class LRUCache(BaseCaching):
    """
    LRU Caching system implemented using a dictionary and a doubly linked list
    for storing the data in the cache system
    with searching and shifting time complexity of O(1).
    """

    def __init__(self):
        """Initialize the LRUCache"""
        super().__init__()
        self.head = Node(None, None)  # Head of the doubly linked list
        self.tail = Node(None, None)  # Tail of the doubly linked list
        self.head.next = self.tail  # Initially, head is connected to tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        """
        Remove a node from the doubly linked list
        This node is the least recently used node.
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_node_to_end(self, node):
        """
        Add a node at end of the list
        The node is the most recently used node
        """
        prev_last = self.tail.prev
        if prev_last:  # If the list is not empty
            prev_last.next = node
        node.prev = prev_last
        node.next = self.tail
        self.tail.prev = node

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove the existing node before updating it
            self._remove_node(self.cache_data[key])

        new_node = Node(key, item)
        self._add_node_to_end(new_node)
        self.cache_data[key] = new_node

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the least recently used node, which is next to head
            lru_node = self.head.next
            self._remove_node(lru_node)
            if lru_node:
                del self.cache_data[lru_node.key]
                print(f"DISCARD: {lru_node.key}")

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        node = self.cache_data[key]
        # Move the accessed node to the end (most recently used)
        self._remove_node(node)
        self._add_node_to_end(node)

        return node.value
