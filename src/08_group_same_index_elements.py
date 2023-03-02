from collections import defaultdict


def run(arr):
    res = defaultdict(list)

    for numbers in arr:
        for i, number in enumerate(numbers):
            res[i].append(number)

    return res.values()


if __name__ == "__main__":
    arr = [['a', 'b'], ['c', 'd'], ['e', 'f', 'g'], ['h', 'i']]
    print(run(arr))
