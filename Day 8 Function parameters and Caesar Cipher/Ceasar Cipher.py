alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)

reRun = True
def caesar(plain_text, plain_shift, direction):
    cipher_text = ""
    if direction == "decode":
        plain_shift *= -1
    for letter in plain_text:
        if letter.isalpha():
            position = alphabet.index(letter)
            new_position = (position + plain_shift) % 26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
        
        
    
    print(f"the {direction} text is {cipher_text}")


while reRun:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(plain_shift = shift, plain_text= text, direction= direction)
    # end_the_cipher = input("Type 'yes'and 'no' to stop.").lower()

    should_continue = input("Type 'yes' if you want to continue and 'no' if you don't.").lower()

    if should_continue == "no":
        reRun = False
        print("Good Bye!")