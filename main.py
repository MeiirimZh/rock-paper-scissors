import keyboard
import time
import os
from random import choice


class Game:
    def __init__(self):
        self.player_wins = 0
        self.ai_wins = 0

        self.choices = ["Rock", "Paper", "Scissors"]
        self.current_choice = 0

    def run(self):
        while True:
            for choice in self.choices:
                if choice == self.choices[self.current_choice]:
                    print(f'> {choice}')
                else:
                    print(choice)

            key = keyboard.read_key()

            if key == "up":
                self.current_choice = max(0, self.current_choice - 1)
            if key =="down":
                self.current_choice = min(len(self.choices) - 1, self.current_choice + 1)

            time.sleep(.15)

            os.system("cls")


if __name__ == "__main__":
    game = Game()
    game.run()
