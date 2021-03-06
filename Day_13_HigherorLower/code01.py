import random
from game_data import data
from art import logo, vs
from replit import clear


def get_random_data():
    "Function that will return a random choide of data"
    return random.choice(data)

def format_data(account):
    "Function that returns format for the account"
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    "Function that checks user's guess"
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def main():
    print(logo)
    score = 0
    game_continue = True
    account_a = get_random_data()
    account_b = get_random_data()

    while game_continue:
        account_a = account_b
        account_b = get_random_data()

        while account_a == account_b:
            account_b = get_random_data()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Compare B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


main()





