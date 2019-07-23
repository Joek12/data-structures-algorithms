"""

    generic node class for various data structures

"""


class Node:

    def __init__(self, value=None, parent=None, child=None, set_pos=None):
        self.parent = parent
        self.child = child
        self.value = value

        if set_pos:
            self.position = set_pos

    def __eq__(self, other):
        return self.value == other.value

    def __iter__(self):

        yield self.value if self.value else 0

        if self.child:
            yield from self.child.__iter__()

    def set_child(self, value):
        self.child = Node(value, parent=self)

    def set_parent(self, value):
        self.parent = Node(value, child=self)

