def number_guessing_name():
    # Ask and check the difficulty level
    from art import logo
    print(logo)
    difficulty = input("Choose difficulty: Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        tries = 10

    elif difficulty == "hard":
        tries = 5

    import random
    #generate a random number
    num = random.randint(1, 100)
    
    valid = True
    while valid:
        guessed = int(input("Guess a number between 1 and 100: "))

        if guessed == num:
            print("Correct. You win!")
            valid = False


        else:
            if guessed < num:
                print(f"Incorrect {guessed} is too low")
            elif guessed > num:
                print(f"Incorrect. {guessed} is too heigh")

            tries -=1
            if tries > 0:
                print(f"You have {tries} remaining tries")

            else: 
                print("You have no tries left. You loose!")

            if tries == 0:
                valid = False

import os
def clear():
    os.system("cls")
while input("type y to play the number guessing game and n to pass.") == "y":
    clear()
    number_guessing_name()