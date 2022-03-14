# GuessMyPassword.py is a quick revision application

import random

# Initialise variables:
response1 = "I am afraid not. Please try again."
response2 = "That is a good password, but not my password. Keep guessing."
response3 = "That is not my password. It really is easy to guess my password."
response4 = "Well done! You must work for MI6. Give my regards to James Bond."
MY_PASSWORD = "my password"

# Function to find out if the user has guessed correctly:
def is_correct(guess, password):
    if guess == password:
        guess_correct = True
    else:
        guess_correct = False
    return guess_correct

# Start the game:
print("Hello.\n")
users_guess = input("See if you can guess my password? ")

# Use our function:
true_or_false = is_correct(users_guess, MY_PASSWORD)

# Run the game until the user is correct:
while true_or_false == False:
    computer_response = random.randint(1, 3)
    if computer_response == 1:
        print(response1)
    elif computer_response == 2:
        print(response2)
    else:
        print(response3)

    # Collect the user's next guess
    users_guess = input("\nWhat is your next guess? ")

    # Use our function again:
    true_or_false = is_correct(users_guess, MY_PASSWORD)

# End the game:
print(response4)
input("\n\n\nPress RETURN to exit.")
