import tkinter as tk
from tkinter import Label, Button
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.instruction_label = Label(master, text="Choose rock, paper, or scissors:")
        self.instruction_label.pack(pady=10)

        self.result_label = Label(master, text="")
        self.result_label.pack(pady=10)

        self.score_label = Label(master, text="Score - You: 0, Computer: 0")
        self.score_label.pack(pady=10)

        self.create_buttons()

    def create_buttons(self):
        choices = ["Rock", "Paper", "Scissors"]
        for choice in choices:
            button = Button(self.master, text=choice, command=lambda c=choice: self.play(c))
            button.pack(pady=5)

    def play(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        result = self.determine_winner(user_choice, computer_choice)
        self.result_label.config(text=result)

        if "win" in result:
            self.user_score += 1
        elif "lose" in result:
            self.computer_score += 1

        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
                (user_choice == "Rock" and computer_choice == "Scissors") or
                (user_choice == "Scissors" and computer_choice == "Paper") or
                (user_choice == "Paper" and computer_choice == "Rock")
        ):
            return "You win!"
        else:
            return "You lose!"

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
