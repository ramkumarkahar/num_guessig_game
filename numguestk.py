import tkinter as tk
import random
global secret_number, attempts_left

def start_game():
#global secret_number, attempts_left
    secret_number = random.randint(1, 10)
    attempts_left = 3
    info_label.config(text="I've picked a number between 1 and 10. Try to guess it.")
    attempts_label.config(text=f"Attempts left: {attempts_left}")

def check_guess():
    #global attempts_left
    guess = int(guess_entry.get())
    attempts_left = attempts_left - 1
    attempts_label.config(text=f"Attempts left: {attempts_left}")
    if guess < secret_number:
        result_label.config(text="Too low. Try again.")
    elif guess > secret_number:
        result_label.config(text="Too high. Try again.")
    else:
        result_label.config(text="Congratulations! You guessed the number.")
    if attempts_left == 0:
        result_label.config(text=f"Sorry, you've run out of attempts. The number was {secret_number}.")

# Create tkinter window
window = tk.Tk()
window.title("Number Guessing Game")

# Start game button
start_button = tk.Button(window, text="Start Game", command=start_game)
start_button.pack()

# Guess entry
guess_entry = tk.Entry(window)
guess_entry.pack()

# Check guess button
check_button = tk.Button(window, text="Check Guess", command=check_guess)
check_button.pack()

# Info label
info_label = tk.Label(window, text="")
info_label.pack()

# Attempts left label
attempts_label = tk.Label(window, text="")
attempts_label.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
