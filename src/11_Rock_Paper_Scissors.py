import random


def game():
    options = ['rock', 'paper', 'scissors']
    results = {'rock': {'rock': 'TIE!', 'paper': 'COMPUTER WINS!', 'scissors': 'YOU WIN!'},
               'paper': {'rock': 'YOU WIN!', 'paper': 'TIE!', 'scissors': 'COMPUTER WINS!'},
               'scissors': {'rock': 'COMPUTER WINS!', 'paper': 'YOU WIN!', 'scissors': 'TIE!'}}

    while True:
        player_choice = input(
            "ENTER YOUR CHOICE (ROCK/PAPER/SCISSORS): ").lower()
        if player_choice not in options:
            print("INVALID INPUT. TRY AGAIN.")
            continue

        computer_choice = random.choice(options)
        print(f"COMPUTER CHOICE:\t{computer_choice}.")

        print(results[player_choice][computer_choice])

        play_again = input("DO YOU WANNA PLAY AGAIN? (Y/N): ").lower()
        if play_again != 'y':
            break


if __name__ == "__main__":
    game()
