"""
    disclaimers:
    1. Python's built-in dict() is a much better implmentation of a hash table
    2. As direct addressing of memory in Python is not easily done, will use
        a list to simulate direct addressing


    from "Introduction to Algorithms":
        use "...[hash table] as doubly linked because
            deletion is faster that way"
"""

from Node import Node
from Container import Container

import hashlib

class HashTable(Container):

    def __init__(self, max=1000):
        self.max = max
        self.values = [None] * max
        self.keys = [None] * max
        super().__init__()

    def __getitem__(self, item):
        return self.chained_hash_search(item)

    def __setitem__(self, key, value):
        self.chained_hash_insert(value, key)

    def hash(self, value):
        # will limit the result of hashing with md5 to mod 1000
        hashed = hashlib.md5(bytes(str(value), encoding="ascii")).hexdigest()
        return int(hashed, 16) % self.max

    def chained_hash_insert(self, x, key):
        hashed = self.hash(key)
        obj = self.values[hashed]

        if not obj:
            self.values[hashed] = Node(x)

        else:
            temp = Node(x)
            temp.child = obj
            obj.parent = temp
            self.values[hashed] = temp

        self.size += 1

    def chained_hash_search(self, k):
        obj = self.values[self.hash(k)]
        if obj:
            while obj and obj.value != k:
                obj = obj.child

        return obj

    def chained_hash_delete(self, x, key):
        obj = self.chained_hash_search(key)
        if obj:
            obj.parent.child = obj.child
            obj.child.parent = obj.parent

        self.size -= 1


