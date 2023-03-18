from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, attempts):
    """Checks answer against guess. Returns the number of attempts remaining."""
    if guess > answer:
        print("Too high")
        attempts -= 1
    elif guess < answer:
        attempts -= 1
        print("Too low")
    else:
        print(f"You got it! The answer was {answer}.")
    return attempts

def set_diffuculty():
    difficultty = input("Choose a difficulty. Type 'easy' or 'hard'")
    if difficultty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 an 100")
    answer = randint(1, 100)
    turns = set_diffuculty()
    guess = 0
    print(f"You have {turns} remaining to guess the number.")
    while guess != answer:
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you loose")
            return

game()