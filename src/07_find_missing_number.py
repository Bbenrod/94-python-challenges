import random

# Given an array containing a range of numbers from 0 to n with a missing number, find the missing number in the input array.


def find_missing_number(arr):
    res = [i for i in range(arr[0], arr[-1] + 1) if (i not in arr)]
    return res


if __name__ == "__main__":
    arr = [i for i in range(20) if random.randint(0, 1)]
    res = find_missing_number(arr)

    print("ARR:\t", arr)
    print("RES:\t", res)
