#!/usr/bin/env python3
"""1. FIFO caching """
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """first item to be inserted will be the first to be deleted
    """
    def ___init__(self):
        """initialize"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value
        for the key key.If key or item is None, this method should
        not do anything."""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data =
            OrderedDict(reversed(list(self.cache_data.items())))
            first_key, _ = self.cache_data.popitem()
            self.cache_data =
            OrderedDict(reversed(list(self.cache_data.items())))
            print("DISCARD:", first_key)

    def get(self, key):
        """
        returns the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data
        return None"""
        return self.cache_data.get(key, None)
