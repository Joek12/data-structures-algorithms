"""
    make a custom (albeit naive) implementation of list in python 3 without using the built-in list()
        (i.e. implement linked list in python)
"""

from Node import Node

class List:

    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def __iter__(self):
        if not self.head:
            return []

        yield from self.head.__iter__()

    def __len__(self):
        return self.count


    def emplace_back(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self.count = 1

        else:
            self.tail.set_child(value)
            self.tail = self.tail.child
            self.count += 1

    def emplace_front(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self.count = 1


        else:
            self.head.set_parent(value)
            self.head = self.head.parent
            self.count += 1

    def insert(self, index, value):
        # inserting at specified index
        pointer = self.head
        assert index < self.count
        for i in range(index):
            pointer = pointer.child

        if pointer != self.head:
            temp = pointer.parent
            temp.set_child(value)
            temp.child.child = pointer
            pointer.parent = temp.child
            self.count += 1

        else:
            self.emplace_front(value)

    def insert(self, value):
        # inserting at head
        x = Node(value)
        x.child = self.head
        if self.head:
            self.head.parent = x
        self.head = x
        x.parent = None

    def swap(self, index, value):
        pointer = self.head
        assert index < self.count
        for i in range(index):
            pointer = pointer.child

        pointer.value = value

    def delete(self, index):
        # deleting at specified index
        # NOT O(1)
        # worst case: O(n)
        pointer = self.head
        assert index < self.count
        for i in range(index):
            pointer = pointer.child

        if pointer != self.head:

            temp = pointer.parent

            if pointer:
                temp.child = pointer.child

            else:
                temp.child = None

        else:
            self.head = pointer.child

        self.count -= 1

    def at(self, index):
        pointer = self.head
        assert index < self.count
        for i in range(index):
            pointer = pointer.child

        return pointer.value

    def search(self, value):
        x = self.head
        # while x != NIL and x.key != k
        while x and x.value != value:
            x = x.child

        return x


