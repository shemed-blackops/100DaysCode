# Pizza restaurant

import sys
import math

PIZZA_LARGE = 25
PIZZA_MEDIUM = 20
PIZZA_SMALL = 15
PEPPERONI_SMALL = 2
PEPPERONI_LARGE_OR_MEDIUM = 3
EXTRA_CHEESE = 1

total_bill = 0
print("Welcome to Pizza Delivery")
size = input("What size of Pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


# convert to upper
size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = extra_cheese.upper()

if size == "S":
    total_bill += PIZZA_SMALL

    if add_pepperoni == "Y":
        total_bill += PEPPERONI_SMALL
if size == "M":
    total_bill += PIZZA_MEDIUM

    if add_pepperoni == "Y":
        total_bill += PEPPERONI_LARGE_OR_MEDIUM

if size == "L":
    total_bill += PIZZA_LARGE

    if add_pepperoni == "Y":
        total_bill += PEPPERONI_LARGE_OR_MEDIUM

if extra_cheese == "Y":
    total_bill += EXTRA_CHEESE


bill_text = f"Your final bill is: ${total_bill}"
print(bill_text)
