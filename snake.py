from turtle import Turtle, Screen
screen = Screen()
screen.listen()
distances_list = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270
class Snake:
    def __init__(self):
        self.my_turtles_list = []
        self.create_snake()
        self.head = self.my_turtles_list[0]

    def create_snake(self):
        for distance in distances_list:
            self.add_snake(distance)

    def add_snake(self, distance):
        t = Turtle('square')
        t.color('white')
        t.penup()
        t.goto(distance)
        self.my_turtles_list.append(t)

    def extend(self):
        self.add_snake(self.my_turtles_list[-1].position())

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move(self):
        for seg_num in range(len(self.my_turtles_list) - 1, 0, -1):
            new_x = self.my_turtles_list[seg_num - 1].xcor()
            new_y = self.my_turtles_list[seg_num - 1].ycor()
            self.my_turtles_list[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def reset_position(self):
        for segments in self.my_turtles_list:
            segments.goto(1000,1000)
        self.my_turtles_list.clear()
        self.create_snake()
        self.head = self.my_turtles_list[0]