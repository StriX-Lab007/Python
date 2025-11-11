"""
Beginner Level - Simple Project
Dice Roller Game
By StriX ProDev
"""

# Refactoring ----  
# Changing the sturcture of the code without changing its functionality.


# Technique we are gonna use :- DRY PRINCIPLE [ Don't Repeat Yourself ] ---- Used whne, we don't want to have repetition or duplicatioin in our code

# Ask the user to make a choice

# If choice is not valid
#   Print an error

# Let the computer to make a choice
#   Print Choices (emojies)

# Determine the winner 
# Ask the user if they want to continue

# If not 
#   Terminate


 #Key -> Value 
# 'r' -> '🪨'
# 's' -> '✂️'
# 'p' -> '📃'

import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = {ROCK:'🪨', SCISSORS:'✂️', PAPER: '📃'}
print()
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        user_choice = input('rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invaild Choice')


def display_choices(user_choice, computer_choice):
    print(f"You Chose {emojis[user_choice]}")
    print(f"Computer Chose {emojis[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif(
    (user_choice == ROCK and computer_choice == SCISSORS) or 
    (user_choice == SCISSORS and computer_choice == PAPER) or 
    (user_choice == PAPER and computer_choice == ROCK)):
        print('You Win')
    else:
        print("You Lose")


def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input("Continue? (y/n): ").lower()
        if should_continue == 'n' :
            print("Thanks For Playing the Game...Visit Again")
            break
    
play_game()



# “What was the real benefit of doing this?” :- 

# Using constants (ROCK, SCISSORS, PAPER)
# Instead of hardcoding 'r', 's', 'p' everywhere, we define constants.
# Real benefit:
# If we ever want to change 'r' to 'rock', we only update one line, not hunt through multiple places.
# Improves readability — if user_choice == ROCK is much clearer than if user_choice == 'r'.
