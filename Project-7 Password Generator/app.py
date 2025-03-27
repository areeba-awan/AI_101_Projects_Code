# PROJECT: 07 PASSWORD GENERATOR IN PYTHON

# DESCRIPTION:  This code is a simple password generator that creates a secure password based on user input.

# INSTRUCTOR : AREEBA TANVEER AWAN

# IMPORTS RANDOM MODULE

import random

# IMPORTS STRING MODULE FOR CHARACTER SETS

import string

def generate_password(length):
    if length < 4:
        return "\n ⚠️ Password length should be at least 4 characters."

    # Ensure at least one lowercase, uppercase, digit, and special character
    password_chars = [
        random.choice(string.ascii_lowercase),  # Lowercase letter
        random.choice(string.ascii_uppercase),  # Uppercase letter
        random.choice(string.digits),          # Digit
        random.choice(string.punctuation)      # Special character
    ]

    # Combine all character types into a pool
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Add random characters to meet the desired length
    password_chars.extend(random.choice(all_chars) for _ in range(length - len(password_chars)))
    random.shuffle(password_chars)  # Shuffle for randomness

    return ''.join(password_chars)

def main():
    print("\n 🔒 Welcome to the Secure Password Generator 🔒")
    try:
        length = int(input("\n 👉 Enter your desired password length (minimum 4): "))
        print("\n ⏳ Crafting your secure password...")
        password = generate_password(length)
        print(f"\n 🔑 Your New Password: {password}")
        print("\n 📝 Reminder: Store your password securely and do not share it with anyone!")
    except ValueError:
        print("\n ❌ Error: Please enter a valid number.")

if __name__ == "__main__":
    main()

# This code is a simple password generator that creates a secure password based on user input.

# This code generates a secure password with at least one lowercase letter, one uppercase letter, one digit, and one special character.
# It ensures that the password length is at least 4 characters and provides user-friendly messages.

# ----------------------------------  FINISIH  ----------------------------------