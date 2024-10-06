import tkinter as tk
from tkinter import messagebox
import random

def check_guess():
    try:
        guess = int(entry.get())
        if guess < 1 or guess > 100:
            result_label.config(text="Please enter a number between 1 and 100.", fg="red")
        else:
            global attempts
            attempts += 1
            if guess < secret_number:
                result_label.config(text="Too low! Try again.", fg="blue")
            elif guess > secret_number:
                result_label.config(text="Too high! Try again.", fg="blue")
            else:
                result_label.config(text=f"Correct! You guessed it in {attempts} attempts.", fg="green")
                guess_button.config(state="disabled")
    except ValueError:
        result_label.config(text="Invalid input! Please enter a number.", fg="red")

def new_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="Guess a number between 1 and 100.", fg="black")
    entry.delete(0, tk.END)
    guess_button.config(state="normal")

root = tk.Tk()
root.title("Number Guessing Game")
root.configure(bg="#2E2E2E")

intro_label = tk.Label(root, text="Welcome to the Number Guessing Game!", font=('Arial', 16), bg="#2E2E2E", fg="white")
intro_label.pack(pady=10)

instruction_label = tk.Label(root, text="I have selected a number between 1 and 100. Can you guess it?", font=('Arial', 12), bg="#2E2E2E", fg="white")
instruction_label.pack(pady=5)

entry = tk.Entry(root, width=10, font=('Arial', 14), bg="#D9D9D9", fg="black")
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", font=('Arial', 12), bg="#FF9500", fg="white", command=check_guess)
guess_button.pack(pady=5)

result_label = tk.Label(root, text="Guess a number between 1 and 100.", font=('Arial', 12), bg="#2E2E2E", fg="white")
result_label.pack(pady=10)

new_game_button = tk.Button(root, text="New Game", font=('Arial', 12), bg="#4CD964", fg="white", command=new_game)
new_game_button.pack(pady=5)

secret_number = random.randint(1, 100)
attempts = 0

root.mainloop()
