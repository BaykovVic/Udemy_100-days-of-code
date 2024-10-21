height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError("Human height should not be greater than 3 meters.")

bmi = weight / (height * height)
print(f"BMI is {bmi:.2f}")