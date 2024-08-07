"""
Today's lesson is about numbers, operations, type conversion and using the f-strings
"""
# Input the bill, the tip percentage, and the number of people to split the bill
bill = float(input("What is the Bill? "))
percentage = float(input("What is the percentage of the tip? "))
people = int(input("What is the number of people? "))

# Calculate the tip
totalBill = (bill + (bill * (percentage/100)))
individualpay = totalBill/people

print(f"The total bill is ${round(totalBill, 2)} and the amount to be paid by each individual is ${round(individualpay, 2)}")
