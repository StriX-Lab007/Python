"""
Beginner Level - Simple Project
Dice Roller Game
By StriX ProDev
"""

import random

print("🎲 Welcome to the Dice Roller Game! 🎲")
print("Created by StriX ProDev\n")

while True:
    choice = input("Roll the dice? (y/n): ").lower().strip()

    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f" You rolled: ({die1}, {die2})\n")
    elif choice == "n":
        print("Thanks for playing! Goodbye! 👋")
        break
    else:
        print("Invalid choice! Please enter 'y' or 'n'.\n")