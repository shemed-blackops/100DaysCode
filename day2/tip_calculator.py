# Tip Calculator
# Author: Seleman Hemed
# This program calculates bills to be paid with tip inclusive

import sys

print("Welcome to tip calculator.")
bill = input("What was the total bill? $")
tip_percentage = input("How much is the tip percentage? 10, 12 or 15? ")
number_of_people = input("How many people to split the bill? ")

# Tip Calculation

bill = float(bill)
tip_percentage = float(tip_percentage)
number_of_people = float(number_of_people)

tip = bill * (tip_percentage / 100)
total_bill = tip + bill
bill_per_person = total_bill / number_of_people

output = f"Each person should pay: ${round(bill_per_person, 2)}"
print(output)
