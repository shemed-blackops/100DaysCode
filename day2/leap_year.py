# Leap year calculator

# Condition
# Its Leap year if year is divisible by 4 evenly
# Except year  divisible by 100 evenly
# Unless  divisible by 400 evenly
# Then its a leap year
# Eg. year 2000
# 2000 / 4 = 500 ---- True (Leap year)
# 2000 / 100 = 20 ---- True (Not Leap Year)
# 2000 / 400 = 5 ----- True (Its Leap year)
#
# year 2100
# 2100 / 4 = 525 Leap Year
# 2100 / 100 = 21 Not Leap year
# 2100 / 400 =  5.25 Not Leap year since not divisible evenly by 400

print("Welcome to Leap year calculator")
year = input("Which year to check?: ")

# Convert string to int
year = int(year)

isLeapYear = False
# Check Leap year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    isLeapYear = True
else:
    isLeapYear = False

if isLeapYear:
    message = f"{year} is a Leap year"
else:
    message = f"{year} is not a Leap year"

print(message)