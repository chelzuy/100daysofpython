import random
from art import logo


EASY_LEVEL = 10
HARD_LEVEL = 5

def setdifficulty():
    """Function to choose level of game difficulty"""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL 
    elif level == 'hard':
        return HARD_LEVEL

def check_guess(guess,number,trial):
    """Function to check user guess vs real answer"""
    if guess > number:
        print("Too high.")
        return trial - 1
    elif guess < number:
        print("Too low.")
        return trial - 1
    elif guess == number:
        print(f"You got it! The answer was {number}.")

def game():
    """Main Game Function"""
    print (logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    
    #Game chooses random number from 1 to 100
    number = random.randint(1,100)
    print(f"The number you need to look for is {number}.")
    
    #Returns maximum trial
    trial = setdifficulty()
    
    #Loop until the user guess correct or runs out of trial
    guess = 0
    while guess!=number:
        print(f"You have {trial} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        #Check if user input a correct guess
        trial = check_guess(guess,number,trial)
        if trial == 0:
            print("You've run out of guesses, you lose.")
        elif guess!=number:
            print("Guess again.")

game()







