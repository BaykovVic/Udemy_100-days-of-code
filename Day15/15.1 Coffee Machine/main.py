from coffee import espresso_ingredients, cappuccino_ingredients, latte_ingredients
from coffee_machine import try_make_coffee, status, machine_menu, resources, check_balance


def buy_coffee():
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    for el in machine_menu:
        if el["name"] == user_choice:
            user_choice = el
    if not check_balance(user_choice):
        print("You have not enough money")
        return
    if try_make_coffee(user_choice):
        print("Take your coffee, please")
    else:
        print("There are no ingredients")

action = ""

def get_minimal_price():
    result = []
    for el in machine_menu:
        result.append(el["price"])
    return min(result)

while status :
    action = input("What would you like to do? (1.Take some coffee\n2. Report machine resources\n3. Turn off the machine)")
    if action == "1":
        for el in machine_menu:
            if resources["current_balance"] < get_minimal_price():
                balance = float(input("Please insert coins"))
                resources["current_balance"] += balance
        try:
            buy_coffee()
        except:
            print("Invalid input")
    elif action == "2":
        for key in resources.keys():
            print(f"|{key}:\t{resources[key]}|")
    elif action == "3":
        print("Turning the machine off")
        status = False
    else:
        print("Invalid input")