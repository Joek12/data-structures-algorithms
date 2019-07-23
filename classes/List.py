"""
    make a custom (albeit naive) implementation of list in python 3 without using the built-in list()
        (i.e. implement linked list in python)
"""

class Node:

    def __init__(self,value:int, parent=None, child=None):
        self.parent = parent
        self.child = child
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __iter__(self):

        yield self.value

        if self.child:
            yield from self.child.__iter__()


    def set_child(self, value):
        self.child = Node(value, parent=self)

    def set_parent(self, value):
        self.parent = Node(value, child=self)

class List:

    def __init__(self):
        self.count = 0
        self.root = None
        self.foot = None

    def __iter__(self):
        if not self.root:
            return []

        yield from self.root.__iter__()

    def __len__(self):
        return self.count


    def emplace_back(self, value):
        if not self.root:
            self.root = Node(value)
            self.foot = self.root
            self.count = 1

        else:
            self.foot.set_child(value)
            self.foot = self.foot.child
            self.count += 1

    def emplace_front(self, value):
        if not self.root:
            self.root = Node(value)
            self.foot = self.root
            self.count = 1


        else:
            self.root.set_parent(value)
            self.root = self.root.parent
            self.count += 1

    def insert(self, index, value):
        pointer = self.root
        assert index < self.count
        for i in range(index):
            pointer = pointer.child

        if pointer != self.root:
            temp = pointer.parent
            temp.set_child(value)
            temp.child.child = pointer
            pointer.parent = temp.child
            self.count += 1

        else:
            self.emplace_front(value)

    def swap(self, index, value):
        pointer = self.root
        assert index < self.count
        for i in range(index):
            pointer = pointer.child

        pointer.value = value

    def delete(self, index):
        pointer = self.root
        assert index < self.count
        for i in range(index):
            pointer = pointer.child

        if pointer != self.root:

            temp = pointer.parent

            if pointer:
                temp.child = pointer.child

            else:
                temp.child = None

        else:
            self.root = pointer.child

        self.count -= 1

    def at(self, index):
        pointer = self.root
        assert index < self.count
        for i in range(index):
            pointer = pointer.child

        return pointer.value



