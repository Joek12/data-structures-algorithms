"""
    inspired by Introduction to Algorithms 3rd Edition by Thomas Cormen

    simple (albeit naive) implementation in Python

"""
from Node import Node
from Common_Exceptions import Overflow, Underflow
from Container import Container


class QueueOverflow(Overflow):
    """queue overflow error"""
    pass


class QueueUnderflow(Underflow):
    """queue underflow error"""
    pass


class QueueCustom(Container):

    def __init__(self, size):
        super().__init__()
        self.max = size

    def enqueue(self, value):
        if self.size == self.max:
            raise QueueOverflow()

        if not self.head:
            self.head = Node(value)
            self.tail = self.head

        else:
            self.tail.set_child(value)
            self.tail = self.tail.child

        self.size += 1

    def dequeue(self):

        if not self.head:
            raise QueueUnderflow()

        value = self.head.value

        if self.size == 1:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.child

        return value
