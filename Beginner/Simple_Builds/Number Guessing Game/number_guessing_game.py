"""
Beginner Level - Simple Project
Dice Roller Game
By StriX ProDev
"""

# Generate a random number
# Ask the user to make a guess
# If not a valid number
# Print an error
# If number < guess
#   Print too low
# If number > guess
#   Print too high
# Else
#   Print well done

import random

number_to_guess = random.randint(1, 50)

while True:
    try:
        user_input = input("Guess the number between 1 and 50: ")
        guess = int(user_input)
        
        if guess < number_to_guess:
            print('Too low!')
            
        elif guess > number_to_guess:
            print('Too High!')
            
        else:
            print('Congratulations! You guessed the number.')
            break
    except ValueError:
        print("Please enter a valid number")
