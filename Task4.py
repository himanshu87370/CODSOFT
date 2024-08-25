import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("400x300")
        self.root.configure(bg='#f0f8ff')

        # Initialize scores
        self.user_score = 0
        self.computer_score = 0

        # Create UI components
        self.title_label = tk.Label(self.root, text="Rock-Paper-Scissors", bg='#f0f8ff', font=('Arial', 16))
        self.title_label.pack(pady=10)

        self.choice_frame = tk.Frame(self.root, bg='#f0f8ff')
        self.choice_frame.pack(pady=20)

        self.rock_button = tk.Button(self.choice_frame, text="Rock", command=lambda: self.play_game('Rock'), bg='#ffb6c1', font=('Arial', 12))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.choice_frame, text="Paper", command=lambda: self.play_game('Paper'), bg='#add8e6', font=('Arial', 12))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.choice_frame, text="Scissors", command=lambda: self.play_game('Scissors'), bg='#90ee90', font=('Arial', 12))
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.result_label = tk.Label(self.root, text="", bg='#f0f8ff', font=('Arial', 12))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text=f"User: {self.user_score} | Computer: {self.computer_score}", bg='#f0f8ff', font=('Arial', 12))
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.play_again, bg='#ffd700', font=('Arial', 12))
        self.play_again_button.pack(pady=10)

    def play_game(self, user_choice):
        choices = ['Rock', 'Paper', 'Scissors']
        computer_choice = random.choice(choices)

        result = self.determine_winner(user_choice, computer_choice)
        self.update_scores(result)
        self.display_result(user_choice, computer_choice, result)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper') or \
             (user_choice == 'Paper' and computer_choice == 'Rock'):
            return "Win"
        else:
            return "Lose"

    def update_scores(self, result):
        if result == "Win":
            self.user_score += 1
        elif result == "Lose":
            self.computer_score += 1

    def display_result(self, user_choice, computer_choice, result):
        result_text = f"You chose {user_choice}. Computer chose {computer_choice}. You {result}!"
        self.result_label.config(text=result_text)
        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.computer_score}")

    def play_again(self):
        self.result_label.config(text="")
        self.play_again_button.config(state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
