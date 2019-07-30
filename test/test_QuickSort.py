from algorithms import QuickSort as qs


def test_qs():
    """
    my_arr = [3, 1, 4, 5]

    qs.quick_sort(my_arr, 0, len(my_arr) - 1)
    print(len(my_arr))
    print(my_arr)
    """


    second_arr = [2,8,7,1,3,5,6,4]
    qs.quick_sort(second_arr, 0, len(second_arr) - 1)
    print(second_arr)


if __name__ == "__main__":
    test_qs()
