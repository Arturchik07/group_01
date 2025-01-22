from my_env.logic import GuessNumberGame


def main():
    print("Welcome to the Guess Number Game!")
    game = GuessNumberGame()

    while not game.is_game_over():
        print(f"\nYou have {game.attempts} attempts left and your current capital is {game.current_capital}")
        try:
            guess = int(input(f"Guess a number between {game.min_number} and {game.max_number}: "))
            bet = int(input("Enter your bet amount: "))

            if guess < game.min_number or guess > game.max_number:
                print(f"Your guess must be between {game.min_number} and {game.max_number}.")
                continue

            print(game.play_round(guess, bet))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    print("\nGame over! Thank you for playing.")


if __name__ == "__main__":
    main()
