#import vs, logo, and game data
from game_data import data
from art import vs
from art import logo
import random


import os
def clear():
    os.system("cls")

def lower_higher():
    print(logo)
    random.shuffle(data)
    # retrieve the data
    n1 = 0
    first = data[n1]
    n2 = 1
    gotten_correct = 0

    correct_continue = True
    while correct_continue:

        second = data[n2]

        # ask the user to pick the famous person with the highest number of followers
        response = input(f"""
        Compare A: {first["name"]} a {first["description"]} from {first["country"]} 

        {vs}

        Against B: {second["name"]} a {second["description"]} from {second["country"]} 
        
        Who has more instagram followers?
        Type A or B:         

        """).upper()

        # Check if the user choose the correct answer
        if first["follower_count"] > second["follower_count"]:
            answer = "A"
        else:
            answer = "B"

        if response == answer:
            gotten_correct += 1
            print(f"Correct! current score is {gotten_correct}")
            n2 +=1
            first = second
            

        else:
            print(f"You lost the game, but you got {gotten_correct} correct answers")
            
            correct_continue = False
            continue_with_game = input("Type Y to continue with the game and N to stop: ").upper()
            if continue_with_game == "Y":
                clear()
                lower_higher()
            
            else:
                clear()
                print(logo)
                print(f"You got {gotten_correct} answers correct in the previous game.")
                print("We regret to see you go! hope you come back again.")


lower_higher()