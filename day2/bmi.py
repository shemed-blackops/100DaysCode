# BMI Calculator

# BMI Categories:
# Underweight = <18.5
# Normal weight = 18.5 - 24.9
# Overweight = 25 - 29.9
# Obesity = BMI of 30 or greater

print("Welcome to BMI Calculator")
weight = input("How much do you weigh? (kg): ")
height = input("How much is your height? (cm): ")

weight_in_kg = float(weight)
height_in_cm = float(height)

height_in_m = height_in_cm / 100

# BMI Calculation

bmi = weight_in_kg/ height_in_m ** 2

#BMI Scales
message = ""
suggestion = ""

if bmi < 18.5:
    suggestion = "Underweight"
elif bmi >= 18.5 and bmi < 25:
    suggestion = "Normal weight"
elif bmi >= 25 and bmi < 30:
    suggestion = "Overweight"
else:
    suggestion = "Obese"
    
message = f"Your bmi is: {round(bmi, 1)}, You are {suggestion}"

print(message)

