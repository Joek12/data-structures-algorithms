
class Container:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        if not self.head:
            return []

        yield from self.head.__iter__()


