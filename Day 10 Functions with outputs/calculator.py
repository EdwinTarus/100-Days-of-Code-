from art import logo

signs = {}

print("hello world24")
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

signs["+"] = add
signs["-"] = sub
signs["*"] = mul
signs["/"] = div

import os
def clear():
    os.system("cls")

def calculator():
    print(logo) 
    num1 = float(input("Please put the first number: "))
    for symbol in signs:
            print(symbol)

    continue_operation = True 

    while continue_operation:
        num2 = float(input("please put the second number: "))

        sign = input("pick a symbol from the line above")

        answer = signs[sign](num1, num2)

        print(f"{num1} {sign} {num2} = {answer}")

        next_op = input("Type y to continue and n to stop")
        if next_op == "y":
            num1 = answer
        
        else:
            continue_operation = False
            clear()
            calculator()


calculator()
