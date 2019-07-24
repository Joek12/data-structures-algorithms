from Node import TreeNode
from Container import Container


red = "RED"
black = "BLACK"


class RBNode(TreeNode):

    def __init__(self, color = black):
        super().__init__()
        self.color = color


class RedBlackTree(Container):

    t_nil = RBNode(black)

    def left_rotate(self, x:RBNode):
        assert x
        y = x.right
        x.right = y.left
        if y.left != self.t_nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == self.t_nil:
            self.head = y
        elif x == x.parent.left:
            x.parent.left = y

        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x:RBNode):
        assert x
        y = x.left
        x.left = y.right
        if y.right != self.t_nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent != self.t_nil:
            self.head = y

        elif x == x.parent.right:
            x.parent.right = y

        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def rb_insert(self, z: TreeNode):
        y = self.t_nil
        x = self.head

        while x != self.t_nil:
            y = x
            x = x.left if z.value < x.value else x.right

        z.parent = y
        if y == self.t_nil:
            self.head = z
        elif z.value < y.value:
            y.left = z
        else:
            y.right = z

        z.left = self.t_nil

        z.right = self.t_nil
        z.color = red
        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, z: TreeNode):
        while z.parent.color == red:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right

                if y.color == red:
                    z.parent.color = black
                    y.color = black
                    z.parent.parent.color = red
                    z = z.parent.parent

                elif z == z.parent.right:
                    z = z.parent
                    self.left_rotate(z)

                else:
                    z.parent.color = black
                    z.parent.parent.color = red
                    self.right_rotate(z.parent.parent)

            else:

                y = z.parent.parent.left

                if y.color == red:
                    z.parent.color = black
                    y.color = black
                    z.parent.parent.color = red
                    z = z.parent.parent

                elif z == z.parent.left:
                    z = z.parent
                    self.right_rotate(z)

                else:
                    z.parent.color = black
                    z.parent.parent.color = red
                    self.left_rotate(z.parent.parent)

        self.head.color = black

    def rb_transplant(self, u:RBNode, v:RBNode):
        if u.parent == self.t_nil:
            self.head = v

        elif u == u.parent.left:
            u.parent.left = v

        else:
            u.parent.right = v

        v.parent = u.parent




