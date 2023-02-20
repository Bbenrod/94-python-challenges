# To create a guessing game, we need to write a program to select a random number between 1 and 10. To give hints to the user, we can use conditional statements to tell the user if the guessed number is smaller, greater than or equal to the randomly selected number.

import random


def run():
    ran_number = random.randrange(0, 10)
    guess = int(input("GUESS NUMBER BETWEEN 0 AND 9:\t"))

    while (ran_number != guess):
        print("{} IS {} THAN SECRET NUMBER.".format(
            guess, ("GREATER" if (guess > ran_number) else "LOWER")))
        guess = int(input("TRY AGAIN:\t"))
    print(f"YOU GUESSED {guess} IS RIGHT")


if __name__ == "__main__":
    run()
