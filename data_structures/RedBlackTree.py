from Node import TreeNode
from data_structures.BinarySearchTree import BinarySearchTree


red = "RED"
black = "BLACK"


class RBNode(TreeNode):

    def __init__(self, color=black, value=None, parent=None, child=None, set_pos=None, left=None, right=None):
        super().__init__(value=value, parent=parent, child=child, set_pos=set_pos, left=left, right=right)
        self.color = color


class RedBlackTree(BinarySearchTree):

    def __init__(self):
        super().__init__()
        self.t_nil = RBNode(black)
        self.head = RBNode(black)

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

    def insert(self, n: int):
        rb_node = RBNode(value=n)
        self.rb_insert(rb_node)

    def rb_insert(self, z: RBNode):
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

    def rb_delete(self, z:RBNode):
        y = z
        y_oc = y.color
        if z.left == self.t_nil:
            x = z.right
            self.rb_transplant(z, z.right)

        elif z.right == self.t_nil:
            x = z.left
            self.rb_transplant(z, z.left)

        else:
            y = self.tree_minimum(z.right)
            y_oc = y.color
            x = y.right

            if y.parent == z:
                x.parent = y

            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.p = y

            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_oc == black:
            self.rb_delete_fixup(x)


    def rb_delete_fixup(self, x):
        while x != self.head and x.color == black:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == red:
                    # case 1
                    w.color = black
                    x.parent.color = red

                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == black and w.right.color == black:
                    # case 2
                    w.color = red
                    x = x.parent

                elif w.right.color == black:
                    # case 3
                    w.left.color = black
                    w.color = red
                    self.right_rotate(w)
                    w = x.parent.right

                else:
                    # case 4
                    w.color = x.parent.color
                    x.parent.color = black
                    w.right.color = black

                    self.left_rotate(x.parent)
                    x = self.head

            else:

                w = x.parent.left
                if w.color == red:
                    # case 1
                    w.color = black
                    x.parent.color = red

                    self.right_rotate(x.parent)
                    w = x.parent.left

                if w.right.color == black and w.left.color == black:
                    # case 2
                    w.color = red
                    x = x.parent

                elif w.left.color == black:
                    # case 3
                    w.right.color = black
                    w.color = red

                    self.left_rotate(w)

                    w = x.parent.left

                else:
                    # case 4
                    w.color = x.parent.color
                    x.parent.color = black
                    w.left.color = black

                    self.right_rotate(x.parent)
                    x = self.head

        x.color = black


