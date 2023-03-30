from turtle import Turtle

SNAKE_BODY_OFFSET = 20
MOVE_DISTANCE = 20
class Snake:
    def __init__(self, head_coordinates):
        self.head_coordinates = head_coordinates
        self.init_snake_body()

    def init_snake_body(self):
        self.segments = []
        for i in range(0, 3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.setx(self.head_coordinates[0] - i * SNAKE_BODY_OFFSET)
            self.segments.append(segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0 , -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
