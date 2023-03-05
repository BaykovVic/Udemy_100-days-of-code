#Write your code below this row 👇
max_range = int(input("Enter Fizz Buzz Range"))
for i in range(0, max_range + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
