import random
from art import logo
print(logo)
def deal_card():
    """
    deal a random card from the cards list
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Lose, Computer has a blackjack"
    elif user_score == 0:
        return "Won with a blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "You win. Computer went over"
    elif user_score > computer_score:
        return "You win!"
    else: 
        return "You lose!"

def play():
    print(logo)

    comp_card = []
    user_card = []

    game_over = False
    for i in range(2):
        user_card.append(deal_card())
        comp_card.append(deal_card()) 

    while not game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(comp_card)
        print(f"Your cards: {user_card} and the current score {user_score}")
        print(f"Computer's first card: {comp_card[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        else:
            want_to_deal = input("Type 'y' to get another card or 'n' to pass: ").lower()
            if want_to_deal == "y":
                user_card.append(deal_card())
            
            else:
                game_over = True


    while computer_score != 0 and computer_score < 17:
        comp_card.append(deal_card())
        computer_score = calculate_score(comp_card)

    print(f"usercards: {user_card}, Your score: {user_score}")
    print(f"computercards: {comp_card}, Computer score: {computer_score}")
    print(compare(user_score, computer_score) )
import os
def clear():
    os.system("cls")

while input("type y to play the game of blackjack and n to pass.") == "y":
    clear()
    play()