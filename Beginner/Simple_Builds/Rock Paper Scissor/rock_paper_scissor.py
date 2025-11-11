"""
Beginner Level - Simple Project
Dice Roller Game
By StriX ProDev
"""

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


while True:
    user_choice = input('rock, paper, or scissors? (r/p/s): ').lower()
    if user_choice not in choices:
        print('Invaild Choice')
        continue

    computer_choice = random.choice(choices)

    print(f"You Chose {emojis[user_choice]}")
    print(f"Computer Chose {emojis[computer_choice]}")


    if user_choice == computer_choice:
        print('Tie!')
    elif(
    (user_choice == 'r' and computer_choice == 's') or 
    (user_choice == 's' and computer_choice == 'p') or 
    (user_choice == 'p' and computer_choice == 'r')):
        print('You Win')
    else:
        print("You Lose")

    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == 'n' :
        print("Thanks For Playing the Game...Visit Again")
        break
    
