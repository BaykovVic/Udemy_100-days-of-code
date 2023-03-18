import random
from game_data import data
from art import logo, vs

def make_choise(data_dict):
    return random.choice(data_dict)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(player_choise, choise_a, choise_b):
    if choise_a["follower_count"] > choise_b["follower_count"]:
        return player_choise == "a"
    else:
        return player_choise == "b"


def game():
    print(logo)
    score = 0
    is_game_over = False
    choiseB = make_choise(data)
    while not is_game_over:
        new_data = data
        for el in new_data:
            if el["name"] == choiseB["name"]:
                new_data.remove(el)
        choiseA = choiseB
        choiseB = make_choise(new_data)
        print(format_data(choiseA))
        print(vs)
        print(format_data(choiseB))
        player_choise = input("Who has more followers? Type 'A' or 'B': ").lower()

        is_correct = check_answer(player_choise, choiseA, choiseB)
        if is_correct:
            score += 1
        else:
            is_game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")

game()

#choiseB = random.choice(data - choiseA)
#print(choiseA)