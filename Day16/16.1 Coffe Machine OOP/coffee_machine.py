class CoffeeMachine:
    status = True
    resources = {
        "coffee": 100,
        "water": 300,
        "milk": 200,
        "sugar": 100,
        "current_balance": 0
    }

    espresso_ingredients = {
        "coffee": 18,
        "water": 50
    }

    cappuccino_ingredients = {
        "coffee": 24,
        "water": 250,
        "milk": 100
    }

    latte_ingredients = {
        "coffee": 24,
        "water": 200,
        "milk": 150
    }

    machine_menu = [
        {"name": "espresso", "ingredients": espresso_ingredients, "price": 1.5},
        {"name": "cappuccino", "ingredients": cappuccino_ingredients, "price": 2.5},
        {"name": "latte", "ingredients": latte_ingredients, "price": 3.0}
    ]

    def print_menu(self):
        print("menu")


    def __init__(self):
        self.status = True
        print("init")


    def check_balance(self, coffee):
        if self.resources["current_balance"] >= coffee["price"]:
            return True
        return False

    def try_make_coffee(self, coffee):
        ingredients = coffee["ingredients"]
        for key in ingredients.keys():
            print(f"Adding ... {key}")
            if self.resources[key] < ingredients[key]:
                print(f"Sorry there is not enough {key}")
                return False
            self.resources[key] -= ingredients[key]
        self.resources["current_balance"] -= coffee["price"]
        return True

    def get_minimal_price(self):
        result = []
        for el in self.machine_menu:
            result.append(el["price"])
        return min(result)

    def buy_coffee(self):
        user_choice = input("What would you like? (espresso/latte/cappuccino):")
        for el in self.machine_menu:
            if el["name"] == user_choice:
                user_choice = el
        if not self.check_balance(user_choice):
            print("You have not enough money")
            return
        if self.try_make_coffee(user_choice):
            print("Take your coffee, please")
        else:
            print("There are no ingredients")


    def work(self):
        while self.status:
            action = input(
                "What would you like to do? (1.Take some coffee\n2. Report machine resources\n3. Turn off the machine)")
            if action == "1":
                for el in self.machine_menu:
                    if self.resources["current_balance"] < self.get_minimal_price():
                        balance = float(input("Please insert coins"))
                        self.resources["current_balance"] += balance
                try:
                    self.buy_coffee()
                except:
                    print("Invalid input")
            elif action == "2":
                for key in self.resources.keys():
                    print(f"|{key}:\t{self.resources[key]}|")
            elif action == "3":
                print(f"Refunding {self.resources['current_balance']}")
                print("Turning the machine off")
                self.status = False
            else:
                print("Invalid input")