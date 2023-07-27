from turtle import Turtle

MOVE_DISTANCE = 20
SEGMENT_WIDTH = 20
NUM_STARTING_SEGMENTS = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for num in range(NUM_STARTING_SEGMENTS):
            position = -(num * SEGMENT_WIDTH), 0
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def grow_snake(self):
        self.add_segment(self.segments[-1].position())

    def remove_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()

    def reset_snake(self):
        self.remove_snake()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        # move segments to previous segment's position, starting from the end
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # move head segment forward
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
