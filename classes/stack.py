"""
    inspired by Introduction to Algorithms 3rd Edition by Thomas Cormen

    simple (albeit naive) implementation in Python
"""
from classes.Node import Node
from classes.Container import Container
from classes.Common_Exceptions import Overflow, Underflow


class StackUnderflow(Underflow):
    """Stack Underflow Error"""


class StackOverflow(Overflow):
    """Stack Overflow Error"""


class Stack(Container):
    """
        as we are simulating static arrays in Python, will alter the
        implementation of top by making it a pointer to the top element
        as opposed to the index of the top element in the base array
        will use size to hold the number of entries instead
        self.root = None
    """

    def __init__(self, size):
        self.max = size
        super().__init__()
        # will not use self.head at all

    def push(self, value):
        """
            standard push function
            updates self.tail afterwards
        :param value:
        :return:
        """
        if self.max == self.size:
            raise StackOverflow()

        if not self.tail:
            self.tail = Node(value)
            self.head = self.tail

        else:
            self.tail.set_child(value)
            self.tail = self.tail.child

        self.size += 1

    def pop(self):
        """
            standard pop function
            updates self.tail and returns the popped value
        :return:
        """
        return_value = self.tail.value if self.tail else None

        if not self.tail:
            assert self.size == 0 and not self.head
            raise StackUnderflow()

        elif self.size == 1:
            self.tail = self.head = None

        else:
            self.tail = self.tail.parent
            self.tail.child = None

        self.size -= 1

        return return_value

    def empty(self):
        """
            returns bool(stack is empty?)
        :return:
        """
        return bool(self.tail)
