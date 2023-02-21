# Calculate mean, median and mode using Python without using any built-in Python library or module.

def mode(numbers):
    elements = list(set(numbers))
    frecuencies = {element: numbers.count(element) for element in elements}
    max_frecuency = max(frecuencies.values())

    mode = []
    for value, frecuency in frecuencies.items():
        if (frecuency == max_frecuency):
            mode.append(value)

    return mode


def median(numbers):
    numbers.sort()
    size = len(numbers)
    mid = ((size//2) - 1)
    # Odd set
    if (size % 2 != 0):
        return numbers[mid]
    # Even set
    else:
        return mean(numbers[slice(mid, mid + 2)])


def mean(numbers):
    return sum(numbers)/len(numbers)


def run():
    # numbers = list(range(10))
    numbers = [12, 16, 20, 20, 16, 16, 12, 30, 25, 23, 24, 20]
    print("MEAN: ", mean(numbers))
    print("MEDIAN: ", median(numbers))
    print("MODE: ", mode(numbers))


if __name__ == "__main__":
    run()
