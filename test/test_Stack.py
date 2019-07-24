from classes.stack import Stack, StackOverflow, StackUnderflow


def test_stack():

    try:

        mys = Stack(10)
        mys.push(1)
        mys.push(2)
        mys.pop()
        mys.push(3)
        mys.push(4)
        mys.pop()

        print(list(mys))

        for i in range(5):
            mys.push(i)

        print(list(mys))

        for i in range(7):
            mys.pop()

        mys.pop()
        print(list(mys))

        for i in range(1000):
            mys.push(1)

    except StackUnderflow:
        print("Stack underflow was caught")
        return

    except StackOverflow:
        print("Stack overflow was caught")
        pass


def test_underflow():
    try:
        mys = Stack(1)
        mys.pop()
        mys.pop()

    except Exception as e:
        assert type(e) == StackUnderflow


def test_overflow():
    try:
        mys = Stack(1)
        mys.push(1)
        mys.push(1)

    except Exception as e:
        assert type(e) == StackOverflow


if __name__ == '__main__':
    test_stack()
    test_underflow()
    test_overflow()
