"""
    create vector class that resizes an array when needed
"""

from List import Node, List
# reuse Node and List class from List file

# simulate a static array
class Array:
    # default to size of 10
    def __init__(self, size=10):
        self.size = size
        # create size number of Nodes of 0's
        self.base = List()
        for _ in range(self.size):
            self.emplace_back(0)


    def


