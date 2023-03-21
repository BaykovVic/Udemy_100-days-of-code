import turtle as tm
import random

sc = tm.Screen()
sc.setup(width=500, height=400)
user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
is_race_on = False
color_list = ["red", "blue", "orange", "green", "purple", "yellow"]
number_of_participants = 6
zero_pos_x = -230
zero_pos_y = 120
step = zero_pos_y / (number_of_participants / 2) + 5
turtles = []

for i in range (0, number_of_participants):
    turtles.append(tm.Turtle(shape="turtle"))
    cur_pos_y = zero_pos_y - i * step
    turtles[i].penup()
    turtles[i].color(color_list[i])
    turtles[i].goto(zero_pos_x, cur_pos_y)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print("You win!")
            else:
                print("You loose!")
            print(f"The turtle with {winner_color} is a winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

sc.exitonclick()

