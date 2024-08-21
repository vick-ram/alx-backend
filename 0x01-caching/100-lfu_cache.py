#!/usr/bin/python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines a caching system with an LFU eviction policy """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.frequency = {}
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            """Update the item and increase its frequency"""
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            """If the cache is full, we need to evict an item"""
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                """Find the least frequently used items"""
                min_freq = min(self.frequency.values())
                lfu_keys = [
                    k for k, v in self.frequency.items() if v == min_freq]

                """Among the LFU items, find the least recently used (LRU)"""
                if len(lfu_keys) > 1:
                    lru_key = None
                    for k in self.order:
                        if k in lfu_keys:
                            lru_key = k
                            break
                else:
                    lru_key = lfu_keys[0]

                """Remove the LRU item from cache"""
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                self.order.remove(lru_key)
                print(f"DISCARD: {lru_key}")

            """Add the new item to cache"""
            self.cache_data[key] = item
            self.frequency[key] = 1

        """Update the usage order"""
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        """Increase the frequency of the key"""
        self.frequency[key] += 1

        """Update the usage order"""
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
