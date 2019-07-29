from data_structures.RedBlackTree import RedBlackTree


def test_rb_tree():
    my_rb = RedBlackTree()
    my_rb.insert(3)
    print(my_rb)
    my_rb.insert(4)
    print(my_rb)


if __name__ == "__main__":
    test_rb_tree()

