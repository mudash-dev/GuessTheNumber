import random

guesses_taken = 0


# This is the number you guessed and it was correct.
def success(guess, number, guesses_taken):
    if guess == number:
        guesses_taken += 1
        # guesses_taken = str(guesses_taken + 1)
        print("Bingo!!" + player_name + " You guessed my number in " + str(guesses_taken) + " guess(s)!")
    return guesses_taken


print("Hello! What is your name?")
player_name = input()

number = random.randint(100, 300)
print("Well," + player_name + ",I am thinking of a number between 100 and 300.")

for guesses_taken in range(5):
    print("Take a guess")
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Your guess is too low.")

    elif guess > number:
        print("Your guess is too high.")

    else:
        guesses_taken = success(guess, number, guesses_taken)
        break


# This is the number the computer was guessing
def actual_guess(number):
    # global number
    number = str(number)
    print("Nope. The number I was thinking of was " + number + ".")


def get_bonus_guesses(number):
    print("Oops! You are out of guesses.\nNeed more guesses? Y/N:")
    response = input().upper()
    # response = str(response)
    if response == "Y":
        for guesses_taken in range(3):
            print("Take a guess")
            guess = input()
            guess = int(guess)
            if guess < number:
                print("Your guess is too low.")

            elif guess > number:
                print("Your guess is too high.")
            else:
                success(guess, number, guesses_taken)
                break

        actual_guess(number)

    elif response == "N":
        actual_guess(number)


if guess != 1:
    # actual_guess(number)
    get_bonus_guesses(number)
