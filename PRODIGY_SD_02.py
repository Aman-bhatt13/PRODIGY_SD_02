import tkinter as tk
from tkinter import messagebox
import random

class GuessingGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("🎯 Number Guessing Game")
        self.master.geometry("400x350")
        self.master.resizable(False, False)
        
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.high_score = None

        # Widgets
        self.label_intro = tk.Label(master, text="Guess a number between 1 and 100", font=("Arial", 14))
        self.label_intro.pack(pady=10)

        self.entry_guess = tk.Entry(master, font=("Arial", 12))
        self.entry_guess.pack()

        self.button_submit = tk.Button(master, text="Submit Guess", font=("Arial", 12), bg="green", fg="white", command=self.check_guess)
        self.button_submit.pack(pady=10)

        self.feedback = tk.StringVar()
        self.label_feedback = tk.Label(master, textvariable=self.feedback, font=("Arial", 12), fg="blue")
        self.label_feedback.pack()

        self.label_attempts = tk.Label(master, text="Attempts: 0", font=("Arial", 12))
        self.label_attempts.pack(pady=5)

        self.label_high_score = tk.Label(master, text="High Score: —", font=("Arial", 12), fg="purple")
        self.label_high_score.pack()

        self.button_reset = tk.Button(master, text="Reset Game", font=("Arial", 12), bg="orange", command=self.reset_game)
        self.button_reset.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            if guess < 1 or guess > 100:
                messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 100.")
                return

            self.attempts += 1
            self.label_attempts.config(text=f"Attempts: {self.attempts}")

            if guess < self.secret_number:
                self.feedback.set("🔻 Too low! Try again.")
            elif guess > self.secret_number:
                self.feedback.set("🔺 Too high! Try again.")
            else:
                self.feedback.set(f"✅ Correct! The number was {self.secret_number}.")
                messagebox.showinfo("Congratulations", f"You guessed the number in {self.attempts} attempts!")

                # Update high score
                if self.high_score is None or self.attempts < self.high_score:
                    self.high_score = self.attempts
                    self.label_high_score.config(text=f"High Score: {self.high_score}")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.feedback.set("")
        self.label_attempts.config(text="Attempts: 0")
        self.entry_guess.delete(0, tk.END)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGameGUI(root)
    root.mainloop()
