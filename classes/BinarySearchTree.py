from Node import TreeNode
from Container import Container

"""
    from "Introduction to Algorithms":
    
    "If y is a node in the left subtree of x,
        then y.key <= x.key.
        
     If y is a node in the right subtree of x,
        then y.key >= x.key"
        
"""


class BinarySearchTree(Container):

    def tree_search(self, x: TreeNode, k):
        while x and k != x.value:
            x = x.left if k < x.value else x.right

        return x

    def tree_minimum(self, x: TreeNode=None):
        if not x:
            x = self.head
        while x.left:
            x = x.left
        return x

    def tree_maximum(self, x: TreeNode=None):
        if not x:
            x = self.head
        while x.right:
            x = x.right
        return x

    def tree_successor(self, x: TreeNode):
        if not x.right:
            return self.tree_minimum(x.right)

        y = x.parent

        while y and x == y.right:
            x = y
            y = y.parent

        return y

    def tree_insert(self, z: TreeNode):
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

    def transplant(self, u: TreeNode, v: TreeNode):
        """

            NB: transplant() doesn't attempt to update v.left and v.right
                doing so, or not doing so, is the responsibility of transplant()'s caller
        :param u:
        :param v:
        :return:
        """
        if not u.parent:
            self.head = v

        elif u == u.parent.left:
            u.parent.left = v

        else:
            u.parent.right = v

        if not v:
            v.parent = u.parent

    def tree_delete(self, z: TreeNode):
        """
            "With the Transplant procedure in hand, here is the procedure
            that deletes node z from binary search tree T"
        :param z:
        :return:
        """

        if not z.left:
            self.transplant(z, z.right)

        elif not z.right:
            self.transplant(z, z.left)

        else:
            y = self.tree_minimum(z.right)

            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)

            y.left = z.left
            y.left.parent = y

