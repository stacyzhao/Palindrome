import random

def get_random_number():
    return random.randint(0,100)

def has_already_guessed_number(user_input):
    return user_input in guess_numbers

def low_or_high_guesses(user_input):
    if user_input < random_number:
        print ("Your guess is too low")
    else:
        print ("Your guess is too high")

tries = 5
random_number = get_random_number()
guess_numbers = []


while tries > 0:
    try:
        user_input = int(input("what guess a number from 0 to 20? "))

        if has_already_guessed_number(user_input):
            print ("you already guessed the number")
            continue

        guess_numbers.append(user_input)

        if user_input == random_number:
            print ("You guessed correctly! Game over")
            break

        low_or_high_guesses(user_input)

        tries -= 1

        print ("you have {} tries.".format(tries))

    except ValueError:
        print ("that is not a number!")
        continue
else:
    print ("you lose. the random number is {}".format(random_number))


# After 5 incorrect guesses, the program needs to tell you that you lose and the game is over.
# If your guess is correct, the program needs to tell you that you win and the game is over.
# If your guess is < than the computer's number, it needs to tell you that your guess was too low.
# If your guess is > than the computer's number, it needs to tell you that your guess was too high.
# If you guess the same number twice, the program needs to ask you if you're feeling all right (or something similarly sarcastic).
# The program must output the number of turns you took.
