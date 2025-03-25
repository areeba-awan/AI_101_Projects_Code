# Project 3 - Guess the Number Game Python Project (User)

# Instructor : Areeba Tanveer Awan

# Importing the random module

import random

print ("\n🔮 WELCOME TO THE NUMBER GUESSING GAME! 🔮")
# GENERATING RANDOM NUMBER

number = random.randint(1, 100)

while True : 
    guess = int(input("\n🧠 Think of a number between 1 and 50, and I'll try to read your mind! : "))
    if guess < number:
        print ("\n🔺 The number you've guessed is too low! 🔺")
        
    elif guess < number:
        print ("\n🔻 The number you've guessed is too high! 🔻")
    else:
        print ("\n🎉 Congratulations! You've guessed the number correctly! 🎉")
        break

    