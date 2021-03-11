from replit import clear
from art import logo
print(logo)

bid = {}
more_bidders = True

def find_highest_bidder(bid):
    highest_bid = 0
    winner = ""
    for x in bid:
        amount = bid[x]
        if amount > highest_bid:
            amount = highest_bid
            winner = x
    print(f"The winning bid is from {winner}.")

while more_bidders:
    name = input("What is your name? ")
    price = int(input("How much is your bid? "))
    bid[name] = price
    add_bidder = input("Are there anymore bidders? ")
    if add_bidder == "yes":
        clear()
    elif add_bidder == "no":
        find_highest_bidder(bid)
        more_bidders = False





