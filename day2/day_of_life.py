import sys

current_age = input("Your current age is: ")

current_age = int(current_age)

maximum_age = 90

remaining_age = maximum_age - current_age

remaining_age_in_days = remaining_age * 365

remaining_age_in_weeks = remaining_age * 52

remaining_age_in_month = remaining_age * 12

print(f"You have {remaining_age_in_days} days, {remaining_age_in_weeks} weeks and {remaining_age_in_month} month left till {maximum_age} years ")
