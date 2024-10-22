from art import logo
import os

def clear():
    os.system("cls")

print(logo)
bidding_finished = False
bids = {}

def highest_bidder(record):
    highest_bid = 0
    winner = ""

    for bidder in record:
        bid_amount = record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished: 
    bName = input("Please input your name: ")
    bPrice = int(input("please input your price: "))

    bids[bName] = bPrice
    still_bid = input("Are there any other bidders? type 'yes' or 'no' ")
    
    if still_bid == 'no':
        bidding_finished = True
        highest_bidder(bids)
    
    elif still_bid == "yes":
        clear()
    
    




