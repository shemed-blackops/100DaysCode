# Print variables
# Printing by swapping number

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

a = a + b
b = a - b
a = a - b

print("a: {} ".format(a))
print("b: {} ".format(b))
