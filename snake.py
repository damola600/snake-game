from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP =  90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("turtle")

    def create_snake(self):
        # TODO: 1. Create a snake body
        # for i in range(3):
        #     #x_cord = i * -20
        #     self.increase_segment()
        for position in STARTING_POSITIONS:
            self.add_segments(position)


    # TODO: 2. Move the snake
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    #TODO: 8. Move the snake when key is pressed
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

    def add_segments(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # def increase_segment(self):
    #     new_segment = Turtle("square")
    #     new_segment.color("white")
    #     new_segment.penup()
    #     new_segment.setx(len(self.segments) * -20)
    #     self.segments.append(new_segment)

    def extend(self):
        self.add_segments(self.segments[-1].position())