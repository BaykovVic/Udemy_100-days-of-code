# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = weight / (height * height)

if bmi < 18.5:
    res = "Underweight"
elif 18.5 <= bmi < 25:
    res = "Normal weight"
elif 25 <= bmi < 30:
    res = "Overweight"
elif 30 <= bmi < 35:
    res = "Obese"
else:
    res = "cliniically obese"

print(f"Your BMI is {round(bmi)}, you are {res}")
