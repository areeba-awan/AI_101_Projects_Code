# Project 4 : Rock , Paper , Scissors Game By Python

# Instructor : Areeba Tanveer Awan

# Rock 💎 , Paper 📄, Scissors ✂️ Game By Python

# import random module

import random

# Function to display welcome message

def welcome_message():
    print("\n 🌟 WELCOME TO AREEBA'S ROCK 💎, PAPER 📄, SCISSORS ✂️  GAME! 🌟")
    print("\n  The first to win 2 rounds will be declared the winner! Let the battle begin ⚔️  !")

# Function to determine the winner
def is_winner(player, opponent):
    return (player == "r" and opponent == "s") or \
           (player == "s" and opponent == "p") or \
           (player == "p" and opponent == "r")

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1
    
    while user_score < 2 and computer_score < 2:
        print(f"\n✨ Round {round_number}")
        user_choice = input("\n Enter your choice: 'r' for Rock, 'p' for Paper, 's' for Scissors: ").lower()

        if user_choice not in ['r', 'p', 's']:
            print("\n ⚠️Invalid choice! Please choose 'r', 'p', or 's'.")
            continue

        computer_choice = random.choice(['r', 'p', 's'])
        choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}
        print(f"\n 🖥️  Computer chose: {choices[computer_choice]}")
        print(f"\n 👤 You chose: {choices[user_choice]}")

        if user_choice == computer_choice:
            print("\n 🤝 It's a tie!")
        elif is_winner(user_choice, computer_choice):
            print("\n 🎉 You win this round!")
            user_score += 1
        else:
            print("\n ❌ Computer wins this round!")
            computer_score += 1

        print(f"\n 📊 Score: You {user_score} - {computer_score} Computer")
        round_number += 1

    # Final result
    print("\n 🏆 FINAL RESULT 🏆")
    if user_score > computer_score:
        print("\n 🎉 Hurrayyyyy! You're the champion! 🎉")
    else:
        print("\n 😢 Oh no, the computer is the champion this time! Better luck next round!")

# Start the game
welcome_message()
play_game()
