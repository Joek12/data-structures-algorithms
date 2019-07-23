"""
    inspired by Introduction to Algorithms 3rd Edition by Thomas Cormen

    simple (albeit naive) implementation in Python
"""
from Node import Node
from Common_Exceptions import Overflow, Underflow


class StackUnderflow(Underflow):
    """Stack Underflow Error"""
    pass


class StackOverflow(Overflow):
    """Stack Overflow Error"""
    pass


class Stack:

    def __init__(self, size):
        # as we are simulating static arrays in Python, will alter the
        # implementation of top by making it a pointer to the top element
        # as opposed to the index of the top element in the base array
        # will use size to hold the number of entries instead
        # self.root = None
        self.top = None
        self.size = 0
        self.max = size

    def __len__(self):
        return self.size

    def push(self, value):
        if self.max == self.size:
            raise StackOverflow()

        if not self.top:
            self.top = Node(value)

        else:
            self.top.set_child(value)

        self.size += 1

    def pop(self):
        return_value = self.top.value

        if not self.top:
            assert self.size == 0
            raise StackUnderflow()

        elif self.size == 1:
            self.top = None

        else:
            self.top = self.top.parent
            self.top.child = None

        self.size -= 1

        return return_value

    def empty(self):
        return bool(self.top)

