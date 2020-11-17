# Love calculator
import sys

true_count = 0
love_count = 0
sum_char = 0
true_chunk = ['t', 'r', 'u', 'e']
love_chunk = ['l', 'o', 'v', 'e']

print("Welcome to love Calculator")

try:
    your_name = input("Who are you?: ").lower()
    partner_name = input("Who do you love?: ").lower()

    #Combine String
    
    combine_name =your_name + partner_name

    for letter in true_chunk:
        true_count += combine_name.count(letter)

    for letter in love_chunk:
        love_count += combine_name.count(letter)

    love_percentage = str(true_count) + str(love_count)
    print(f"Love percentage between {your_name} and {partner_name} is {love_percentage} %")

except Exception as e:
    print(e)
    sys.exit()
