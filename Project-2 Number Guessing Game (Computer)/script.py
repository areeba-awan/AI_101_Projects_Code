# Project 2: Guess The Number Game by Computer

# 1 to 100 Numbers

import random
def guess_the_number():
    """Project 2 : Guess The Number Game by Computer."""
    number = random.randint(1, 100)
    guesses_left = 7

    # Print Welcome Message
    print("\n😃 Welcome to the Areeba's Number Guessing Game 🔢\n")
    print("🎯 I have selected a number between 1 and 100. Can you guess it? 🤔")

    # Loop for the number of attempts
    while guesses_left > 0:
        print(f"\n🤔 You have {guesses_left} attempts remaining to guess the number!")
        try:
            guess = int(input("\n👉🔢 Take a guess of Number : "))
        except ValueError:
            print("\n⚠️ Invalid Input: Please enter a valid number🚫 : ")
            continue

        # guess the number
        if guess < number: 
            print("\n📉 Too low number. Try again Please! 🔄")
        elif guess > number:
            print("\n📈 Too high number. Try again Please! 🔄")
        else:
            print(f"\n🎉 Congratulations! You have guessed the correct number in {7 - guesses_left + 1} tries! 🏆")
            return  # Exit the game
        
        guesses_left -= 1
    
    
    
    # If the user runs out of guesses (moved outside the while loop)
    print(f"\n🚨 You've run out of guesses! The number is {number} You Lose! 😔")

            
                

# Call the function
guess_the_number()            

      
