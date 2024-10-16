
import random
from Hangman_art import stages
from Hangman_art import logo
from hangman_words import ListA

print(logo)
word = random.choice(ListA)
word = word.lower()
num = len(word)
word_fill = []

for i in range(num):
    word_fill.append("-")

lives = 6   
endGame = False
while not endGame:
    guess = input("please guess the letter in the word: ").lower()
    if guess in word_fill:
        print(f"You have already guessed {guess}")
    for position in range(len(word)):
        if word[position] == guess:
            word_fill[position] = word[position]
    


    print(word_fill)
    if guess not in word:
        print(f"you have guessed {guess} and it's not in the word. You loose a life!")
        lives -=1
        print(lives)
        print(stages[lives])
        if lives == 0:
            endGame = True
            print("You Lose!")
        

    if "-" not in word_fill:
        endGame = True
        print("You WOn")
    
    

    



  



        
        
  
  





