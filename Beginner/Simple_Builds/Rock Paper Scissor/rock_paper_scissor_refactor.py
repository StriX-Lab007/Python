"""
Beginner Level - Simple Project
Dice Roller Game
By StriX ProDev
"""

# Refactoring ----
# Changing the sturcture of the code without changing its functionality.


# Technique we are gonna use :- MODULARIZATION ---- Breaking down a large program into smaller resulable parts called "modules or functions". 

# Ask the user to make a choice
# If choice is not valid
#   Print an error
# Let the computer to make a choice
# Print Choices (emojies)
# Determine the winner 
# Ask the user if they want to continue
# If not 
#   Terminate


 #Key -> Value 
# 'r' -> '🪨'
# 's' -> '✂️'

import random

emojis = {'r':'🪨', 's':'✂️', 'p': '📃'}
choices = ['r', 'p', 's']


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
    (user_choice == 'r' and computer_choice == 's') or 
    (user_choice == 's' and computer_choice == 'p') or 
    (user_choice == 'p' and computer_choice == 'r')):
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

# By refactoring we broke down our program into small reusable functions, each of these functions has only a few line.
# So, if there's a bug in any one of these functions we can only focus on those few.
# This is easier than reading and understanding an entire script 
# This is the benifit of Modularizing code.