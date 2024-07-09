import random
import sys


def main():
    level = get_level()
    num = random.randint(1, level)
    guess = get_guess()
    check_guess(guess, num)

def get_level():
    try:
        question = int(input("Level: "))
        if question < 1:
            return get_level()
        else:
            return question
    except ValueError:
        return get_level()

def get_guess():
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            return get_guess()
        else:
            return int(guess)
    except ValueError:
        get_guess()

def check_guess(g, n):
    while True:
        if g < n:
            print("Too small!")
            g = get_guess()
        elif g > n:
            print("Too Large!")
            g = get_guess()
        elif g == n:
            sys.exit("Just Right!")

main()