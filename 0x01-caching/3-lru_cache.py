#!/usr/bin/python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines a caching system with a LRU eviction policy """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                """Move the key to the end to mark it as recently used"""
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                """LRU eviction: discard the least recently used key"""
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            """Add the item to the cache and mark the key as recently used"""
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        """Move the key to the end to mark it as recently used"""
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
