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

from art import logo
def calculator():
    print(logo)
    num1 = float(input("What's the first number?"))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above")
        num2 = float(input("What's the second number?"))
        operation = operations[operation_symbol]
        result = operation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:") == 'y':
            num1 = result
        else:
            should_continue = False
            calculator()

calculator()