from art import logo

import os
def clear_console():
    os.system('cls')

print(logo)

auction = {}
bidding_finished = False
    
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    

while not bidding_finished:
    name = input("What's your name?: ")
    price = int(input("What's your bid?:  $"))
    auction [name] = price
    should_countinue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_countinue == 'no':
        bidding_finished = True
        find_highest_bidder(auction)
    elif should_countinue == 'yes':
        clear_console()