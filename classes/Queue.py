"""
    inspired by Introduction to Algorithms 3rd Edition by Thomas Cormen

    simple (albeit naive) implementation in Python

"""
from Node import Node
from Common_Exceptions import Overflow, Underflow


class QueueOverflow(Overflow):
    """queue overflow error"""
    pass


class QueueUnderflow(Underflow):
    """queue underflow error"""
    pass


class Queue:

    def __init__(self, size):
        self.tail = None
        self.head = None
        self.length = None
        self.max = size

    def __len__(self):
        return self.length

    def enqueue(self, value):
        if self.length == self.max:
            raise QueueOverflow()

        if not self.head:
            self.head = Node(value)
            self.tail = self.head

        else:
            self.tail.set_child(value)
            self.tail = self.tail.child

        self.length += 1

    def dequeue(self):

        if not self.head:
            raise QueueUnderflow()

        value = self.head.value

        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.child

        return value
