# Import the randint function from the random module
from random import randint

# Welcome message and player name input
print(f"----------------- Guess the Number (game) -----------------\n\n")
player_name = input("\tEnter your name:\n\n")

# Difficulty selection
difficulty = int(input("\n\tSelect your Difficulty\n1. Easy (Number 1-10)\n2. Normal (Number 1-50)\n3. Hard (Number 1-100)\n"))

# Define the difficulty levels
easy, normal, hard = 1, 2, 3

# Flag variable for game loop
flag = 1

# Counter for the number of guesses used
guesses_used = 0

# Condition for selecting the difficulty
if difficulty == easy:
    # Generate a random number between 1 and 10 for easy mode
    game_number = randint(1, 10)
    print(game_number)
elif difficulty == normal:
    # Generate a random number between 1 and 50 for normal mode
    game_number = randint(1, 50)
    print(game_number)
elif difficulty == hard:
    # Generate a random number between 1 and 100 for hard mode
    game_number = randint(1, 100)
    print(game_number)
else:
    # Error message for invalid input
    print("Please Select proper difficulty")

# Game loop
while (flag == 1):
    # Get the player's guess
    guessed_number = int(input("guess number:\n "))

    # Check if the guess is correct
    if guessed_number != game_number:
        if(guessed_number > game_number):
            # Message for a guess that is too high
            print("the number is smaller that this number")
        elif(guessed_number < game_number):
            # Message for a guess that is too low
            print("the number is Bigger that this number")
        # Increment the guesses used counter
        guesses_used += 1
    else:
        # Message for a correct guess
        print("\n\nHooray..!! you Guessed it Right\n\n")
        # Show the number of guesses used
        print(f"Your Score: {guesses_used + 1}\n\n")
        # Set flag to end the game loop
        flag == 0
        break
