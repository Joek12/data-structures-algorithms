"""
    create vector class that resizes a simulated static array when needed
"""

from Node import Node
# reuse Node and List class from List file


class Array:
    # simulate a static array

    def __init__(self, size=1, old_array=None, growth=2):
        # default exhibits exponential growth

        self.root = Node()
        self.count = 0

        if not old_array:
            self.size = size
            # create size number of Nodes of 0's

        else:
            old_size = len(old_array)
            self.size = old_size * growth
            pointer = self.root

            # copy old array into first half of new array
            for val in old_array:
                pointer.value = val
                pointer.set_child()
                pointer = pointer.child

            # set count to a count of non-null elements
            self.count = old_size

            # zero the second half of new array

            for _ in range(old_size):
                if _ < old_size - 1:
                    pointer.set_child()
                    pointer = pointer.child



    def __len__(self):
        return self.size

    def __iter__(self):
        if not self.root:
            return []

        yield from self.root.__iter__()

    def insert(self, index, value):
        # swap, not insert
        # as this is simulating a static array
        assert index < self.size
        pointer = self.root
        for _ in range(index):
            pointer = pointer.child

        if not pointer.value:
            self.count += 1

        pointer.value = value

    def at(self, index):
        assert index < self.size
        pointer = self.root
        for _ in range(index):
            pointer = pointer.child

        return pointer.value


class Vector:

    def __init__(self):
        self.base = Array()
        self.size = len(self.base)


    def __len__(self):
        return self.size

    def __iter__(self):
        yield from self.base.__iter__()

    def push_back(self, value):
        pointer = self.base.root
        for _ in range






