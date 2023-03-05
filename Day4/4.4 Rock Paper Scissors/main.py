import random

rock = '🪨'

paper = '📄'

scissors = '✂️'

#Write your code below this line 👇
figures = [rock, paper, scissors]
user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choise >= 3 or user_choise < 0:
    print("Incorrect input")
    exit(0)
print(f"Your choise is: \n{figures[user_choise]}")

computer_choise = random.randint(0, 2)
print(f"Computer choise is: \n{figures[computer_choise]}")

if computer_choise == 2 and user_choise == 0:
    print("You Win!")
elif computer_choise == 0 and user_choise == 2:
    print("You Loose!")
elif computer_choise > user_choise:
    print("You Loose!")
elif computer_choise < user_choise:
    print("You Win!")
elif computer_choise == user_choise:
    print("It's a Draw")


