import os
from art import logo

print(logo)
clear = lambda: os.system('clear')
bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    return winner


while not bidding_finished:
    name = input("What is your name?")
    price = int(input("What is your bid?"))
    bids[name] = price
    should_continue = input("Are there any pther bidders? Type 'yes' or 'no'")
    if should_continue == 'no':
        bidding_finished = True
        winner_name = find_highest_bidder(bids)
        print(f'The winner is {winner_name} with a bid of ${bids[winner_name]}')
    elif should_continue == 'yes':
        print("clear")
