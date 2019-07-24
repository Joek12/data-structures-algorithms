from data_structures.List import List


def test_list():
    myl = List()
    myl.push_back(1)

    myl.push_back(2)

    myl.insert(0, 3)
    myl.insert(1, 4)
    myl.push_front(5)
    myl.insert(2, 6)
    myl.delete(2)

    read = list(myl)
    assert read == [5, 3, 4, 1, 2]

    assert len(myl) == 5

    assert myl.at(2) == 4
    assert myl.at(4) == 2

    myl.swap(3, 7)
    assert list(myl) == [5, 3, 4, 7, 2]


if __name__ == '__main__':
    test_list()
