import random
from decouple import config

class GuessNumberGame:
    def __init__(self):
        self.min_number = config('min_number', cast=int, default=1)
        self.max_number = config('max_number', cast=int, default=100)
        self.attempts = config('attempts', cast=int, default=5)
        self.start_capital = config('start_capital', cast=int, default=100)
        self.secret_number = random.randint(self.min_number, self.max_number)
        self.current_capital = self.start_capital

    def play_round(self, guess, bet):
        if bet > self.current_capital:
            return "Insufficient funds to make this bet."

        self.attempts -= 1
        if guess == self.secret_number:
            winnings = bet * 2
            self.current_capital += winnings
            return f"Congratulations! You guessed the number and won {winnings}! Current capital: {self.current_capital}"
        else:
            self.current_capital -= bet
            return f"Wrong guess. The number was {self.secret_number if self.attempts == 0 else 'not that one.'} Remaining capital: {self.current_capital}"

    def is_game_over(self):
        return self.attempts == 0 or self.current_capital <= 0

---
