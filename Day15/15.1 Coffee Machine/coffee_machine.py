from coffee import espresso_ingredients, cappuccino_ingredients, latte_ingredients

resources = {
    "coffee" : 100,
    "water" : 300,
    "milk" : 200,
    "sugar" : 100,
    "current_balance": 0
}

machine_menu = [
    {"name" : "espresso", "ingredients" : espresso_ingredients, "price" : 1.5},
    {"name" : "cappuccino", "ingredients" :cappuccino_ingredients, "price" : 2.5},
    {"name" : "latte", "ingredients" : latte_ingredients, "price" : 3.0}
]

status = True

def check_balance(coffee):
    if resources["current_balance"] >= coffee["price"]:
        return True
    return False

def try_make_coffee(coffee):
    ingredients = coffee["ingredients"]
    for key in ingredients.keys() :
        print(f"Adding ... {key}")
        if resources[key] < ingredients[key]:
            print(f"Sorry there is not enough {key}")
            return False
        resources[key] -= ingredients[key]
    resources["current_balance"] -= coffee["price"]
    return  True


