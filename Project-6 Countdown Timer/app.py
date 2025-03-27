# PROJECT 5 : COUNTDOWN TIMER IN PYTHON AND GOOGLE COLAB

# DESCRIPTION : This is a simple countdown timer program that will take the input from the user and then countdown to 0.

# INSTRUCTOR : AREEBA TANVEER AWAN

import time
import sys

def rocket_launch_timer(total_seconds):
    print("\n🚀 Rocket Launch Countdown Started! Brace yourself... 🌌\n")
    for remaining in range(total_seconds, -1, -1):
        mins, secs = divmod(remaining, 60)
        timer = f"{mins:02d}:{secs:02d}"
        # Create a progress bar (20 blocks wide)
        progress = int(((total_seconds - remaining) / total_seconds) * 20) if total_seconds > 0 else 20
        bar = "[" + "🚀" * progress + "-" * (20 - progress) + "]"
        # Print the timer and progress bar on the same line
        sys.stdout.write(f"\r🕒 T-minus {timer} {bar}")
        sys.stdout.flush()
        time.sleep(1)

    print("\n\n✨🚀 BLAST OFF! Your rocket is soaring through the stars! 🌠✨")

try:
    print("\n 🌌 Welcome to the Areeba's Rocket Launch Game!")
    print("\n 🎮 Objective: Set your countdown and watch your rocket take off into space!")
    total_seconds = int(input("\n ⏲️ Enter your countdown time in seconds: "))
    rocket_launch_timer(total_seconds)
except ValueError:
    print("\n ⚠️ Please enter a valid number. Let's try that again!")

# Run the program
# python app.py

# --------------------------- FINISHED --------------------------- #