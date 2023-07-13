from turtle import Turtle

SNAKE_BODY_OFFSET = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self, head_coordinates):
        self.head_coordinates = head_coordinates
        self.init_snake_body()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

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

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.init_snake_body()
        self.head = self.segments[0]



