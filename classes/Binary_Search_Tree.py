from Node import Node
from Container import Container

"""
    from "Introduction to Algorithms":
    
    "If y is a node in the left subtree of x,
        then y.key <= x.key.
        
     If y is a node in the right subtree of x,
        then y.key >= x.key"
        
"""

class Tree_Node(Node):
    def __init__(self):
        super().__init__()
        self.left = None
        self.right = None

    def __iter__(self):

        if self.left:
            yield from self.left.__iter__()

        yield self.value

        if self.right:
            yield from self.right.__iter__()


class Binary_Search_Tree(Container):

    def tree_search(self, x:Tree_Node, k):
        while x and k != x.value:
            x = x.left if k < x.value else x.right

        return x

    def tree_minimum(self, x:Tree_Node=None):
        if not x:
            x = self.head
        while x.left:
            x = x.left
        return x

    def tree_maximum(self, x:Tree_Node=None):
        if not x:
            x = self.head
        while x.right:
            x = x.right
        return x

    def tree_successor(self, x:Tree_Node):
        if not x.right:
            return self.tree_minimum(x.right)

        y = x.parent

        while y and x == y.right:
            x = y
            y = y.parent

        return y


    def tree_insert(self, z:Tree_Node):
        y = None
        x = self.head
        while x:
            y = x
            x = x.left if z.value < x.value else x.right

        z.parent = y

        if not y:
            self.head = z

        elif z.value < y.value:
            y.left = z

        else:
            y.right = z

