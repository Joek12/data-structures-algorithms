"""
    inspired by Introduction to Algorithms 3rd Edition by Thomas Cormen

    simple (albeit naive) implementation in Python
"""
from Node import Node
from Container import Container
from Common_Exceptions import Overflow, Underflow


class StackUnderflow(Underflow):
    """Stack Underflow Error"""
    pass


class StackOverflow(Overflow):
    """Stack Overflow Error"""
    pass


class Stack(Container):
    """
        as we are simulating static arrays in Python, will alter the
        implementation of top by making it a pointer to the top element
        as opposed to the index of the top element in the base array
        will use size to hold the number of entries instead
        self.root = None
    """

    def __init__(self, size):
        super().__init__()
        self.max = size

    def push(self, value):
        if self.max == self.size:
            raise StackOverflow()

        if not self.tail:
            self.tail = Node(value)

        else:
            self.tail.set_child(value)

        self.size += 1

    def pop(self):
        return_value = self.tail.value

        if not self.tail:
            assert self.size == 0
            raise StackUnderflow()

        elif self.size == 1:
            self.tail = None

        else:
            self.tail = self.tail.parent
            self.tail.child = None

        self.size -= 1

        return return_value

    def empty(self):
        return bool(self.tail)

