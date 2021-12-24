from math import floor

def merge(input: list, p: int, q: int, r: int):
    """
        p must be less than or equal to q and q must be less than r
    :param input:
    :param p:
    :param q:
    :param r:
    :return:
    """
    assert p <= q < r

    sentinel = '$'

    n_1 = q - p + 1
    n_2 = r - q

    array_l = [None] * (n_1 + 1)
    array_r = [None] * (n_2 + 1)

    for i in range(n_1):
        array_l[i] = input[p + i - 1]

    for j in range(n_2):
        array_r[j] = input[q + j]

    array_l[n_1] = sentinel
    array_r[n_2] = sentinel

    i = 0
    j = 0

    for k in range(r - p + 1):
        if array_l[i] <= array_r[j]:
            input[k+p] = array_l[i]
            i += 1

        else:
            input[k+p] = array_r[j]
            j += 1


def merge_sort(input: list, p: int, r: int):
    if p < r:
        q = floor((p + r) / 2)
        merge_sort(input, p, q)
        merge_sort(input, q + 1, r)
        merge(input, p, q, r)
