def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


num1 = int(input("What's the first number?"))
num2 = int(input("What's the second number?"))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above")
operation = operations[operation_symbol]

result = operation(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {result}")
