from random import randint

print(f"----------------- Guess the Number (game) -----------------\n\n")
player_name = input("\tEnter your name:\n\n")
difficulty = int(input("\n\tSelect your Difficulty\n1. Easy (Number 1-10)\n2. Normal (Number 1-50)\n3. Hard (Number 1-100)\n"))

easy, normal, hard = 1, 2, 3
flag = 1
guesses_used = 0

if difficulty == easy:
    game_number = randint(1, 10)
    print(game_number)
elif difficulty == normal:
    game_number = randint(1, 50)
    print(game_number)
elif difficulty == hard:
    game_number = randint(1, 100)
    print(game_number)


else:
    print("Please Select proper difficulty")



while (flag == 1):
    guessed_number = int(input("guess number:\n "))
    if guessed_number != game_number:
        guesses_used += 1
    else:
        print("Hooray..!! you Guessed it Right\n\n")
        print(f"Your Score: {guesses_used + 1}\n\n")
        flag == 0
        break
