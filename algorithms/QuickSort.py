

def quick_sort(arr: list, p: int, r: int):

    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q+1, r)


def partition(arr: list, p: int, r: int):

    x = arr[r]
    i = p - 1

    for j in range(r-1 - p + 1):
        ################
        dum = arr[j+p]

        if arr[j+p] <= x:
            i += 1

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i+1]
    arr[i + 1] = arr[r]
    arr[r] = temp

    return i + 1


