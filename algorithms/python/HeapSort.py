
"""

"""
# from Container import Container
# as we are representing the heap as an array, we won't need to
    # import base class Container


class MaxHeap:

    def __init__(self):
        """
        an array A that represents a heap is an object
        with two attributes: A.length, which gives the number
        of elements in the array,

        and A.heap-size, which represents how many elements in
        the heap are stored within array A
        """
        self.base = []
        self.heap_size = 0

    def __len__(self):
        return len(self.base)

    def __getitem__(self, item):
        return self.base[item]

    def __setitem__(self, key, value):
        self.base[key] = value

    def max_heapify(self, index:int):
        left = lambda index : index << 1
        right = lambda index : (index << 1) + 1

        largest = left if (left <= self.heap_size and self[left] > self[index]) else index
        if right <= self.heap_size and self[right] > self[largest]
            largest = right
        if largest != index:
            temp = self[largest]
            self[index] = self[largest]
            self[largest] = temp

            self.max_heapify(largest)



