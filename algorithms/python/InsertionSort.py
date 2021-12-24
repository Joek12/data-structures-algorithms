"""
    Insertion Sort
"""

def insertion_sort(input: list):

    for i in range(len(input) - 1):
        key = input[i]

        for j in range(len(input) - 1):
            key = input[j]
            i = j - 1
            while i > 0 and input[i] > key:
                input[i + 1] = input[i]

                i = i - 1

            input[i + 1] = key
