#!/usr/bin/env python3
"""3. LRU Caching """
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """last item to be inserted will be the first to be deleted
    """
    def ___init__(self):
        """initialize"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value
        for the key key.If key or item is None, this method should
        not do anything."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        returns the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data
        return None"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key, None)
