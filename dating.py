#!/usr/bin/env python3
# Created by: Gustav I
# Created on: March 24, 2025
# This program checks if the user's age is between 25 and 40 to determine if they can date a grandchild.
# It ensures the input is a valid integer and between 0 and 120.


def get_age():
    # This function prompts the user to enter their age and ensures the input is valid.
    while True:
        try:
            # Try to convert the user input to an integer.
            age = int(input("Enter your age: "))

            # Check if the age is within a valid range (0-120).
            if 0 <= age <= 120:
                return age  # Return the valid age input.
            else:
                # Prompt again if the age is outside the valid range.
                print("Please enter a valid age between 0 and 120.")
        except ValueError:
            # Handle the case where the input is not a number.
            print("Invalid input! Please retry and enter a number.")


def main():
    # Main function where the program logic begins.
    age = get_age()  # Get the user's valid age.

    # Check if the age is between 25 and 40
    if age > 25 and age < 40:  # AND operator used here
        print("You can date their grandchild!")  # If valid, approval is given.
    else:
        print(
            "Sorry, you cannot date their grandchild."
        )  # Otherwise, approval is denied.


# Ensure the main function is called when the script runs directly.
if __name__ == "__main__":
    main()
