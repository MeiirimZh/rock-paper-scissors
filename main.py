import keyboard
import time
import os
import random


class Game:
    def __init__(self):
        self.player_wins = 0
        self.ai_wins = 0

        self.player_choice = None
        self.ai_choice = None

        self.choices = ["Rock", "Paper", "Scissors"]
        self.current_choice = 0

        self.win = None
        self.win_conditions = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
        self.win_text = {"Player": "Player won!\n", "AI": "Computer won!\n", "Draw": "Draw!\n"}

    def run(self):
        while True:
            print(f'Player: {self.player_wins}\tComputer: {self.ai_wins}\n')

            if self.player_choice and self.ai_choice:
                print(f'Player: {self.player_choice}\nComputer: {self.ai_choice}')

            if self.win:
                print(self.win_text[self.win])

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
            if key == "enter":
                self.player_choice = self.choices[self.current_choice]
                self.ai_choice = random.choice(self.choices)
                self.win = self.check_win(self.ai_choice)

            time.sleep(.15)

            os.system("cls")

    def check_win(self, ai_choice):
        if self.choices[self.current_choice] == ai_choice:
            return "Draw"
        
        if self.win_conditions[self.choices[self.current_choice]] == ai_choice:
            self.player_wins += 1
            return "Player"
        else:
            self.ai_wins += 1
            return "AI"


if __name__ == "__main__":
    game = Game()
    game.run()
