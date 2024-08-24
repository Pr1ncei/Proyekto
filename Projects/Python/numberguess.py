"""
NUMBER GUESSING GAME:

- User inputs the lower bound and upper bound of the range.
- The compiler generates a random integer between the range and store it in a variable for future references.
- For repetitive guessing, a while loop will be initialized.
- If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
- Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
- And if the user guessed the right number, the loop breaks” Output.
"""

import random

# Check if the user's input is valid
def input_validator(prompt, lower=None, upper=None):
    while True:
        try:
            value = int(input(prompt))
            if lower is not None and upper is not None:  # When validating guesses
                if lower <= value <= upper:
                    return value
                else:
                    print(f"Please enter a number between {lower} and {upper}.")
            else:  # When setting the bounds
                return value
        except ValueError:
            print("Invalid Input. Try Again.")


# Function to get valid lower and upper bounds
def get_bounds():
    while True:
        lower = input_validator("Enter Lower Bound: ")
        upper = input_validator("Enter Upper Bound: ")
        if lower < upper:
            return lower, upper
        else:
            print(
                "The lower bound must be less than the upper bound. Please try again."
            )


# User tries to guess the number
def number_guess(random_number, lower, upper):
    count = 1
    guess = input_validator(f"{count} Try: ", lower, upper)

    while random_number != guess:
        if guess < random_number:
            print(f"The number is higher than {guess}")
        elif guess > random_number:
            print(f"The number is lower than {guess}")

        count += 1
        guess = input_validator(f"{count} Try: ", lower, upper)

    print(f"You got it right! The correct number is {random_number}")


# Main Function
def main():
    lower, upper = get_bounds()  # Get valid bounds
    random_number = random.randint(lower, upper)

    print(f"Start the Game, Guess a number from {lower} to {upper}")
    number_guess(random_number, lower, upper)


if __name__ == "__main__":
    main()
