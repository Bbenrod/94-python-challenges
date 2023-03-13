# Calculate the execution time of a Python program

from time import time


def run():
    start = time()
    print("Time execution:\t", (time() - start))


if __name__ == "__main__":
    run()
