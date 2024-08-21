#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a caching system with a LIFO eviction policy """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print(f"DISCARD: {self.last_key}")
                del self.cache_data[self.last_key]
            self.last_key = key

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
