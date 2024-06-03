import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1,10)
    print(secret_number)
    
    attempts = 0
    max_attempts = 3

    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 10. Try to guess it.")

    while attempts < max_attempts:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Congratulations! You guessed the number in", attempts, "attempts.")
            break
    else:
        print("Sorry, you've run out of attempts. The number was", secret_number)

# Start the game
guess_number()
