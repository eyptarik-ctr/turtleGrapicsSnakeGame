from turtle import*
from random import*
starting_pos = [0, -20 ,-40]
move_distance = 20
color_list = ['#ffb703','#219ebc','#e3d5ca','#780000','#003049','#bc6c25','#ff006e','#006d77','#f77f00','#006d77','#3a5a40','#8338ec','#bf0603','#386641','#40916c','#124559','#ff70a6','#7b2cbf','#240046','#c9184a','#ab81cd','#b95cad','#6930c3','#7b2d26','#819595','#19535f','#363946','#0496ff','#72efdd','#0b7a75','#0f59ff']
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.new_x = 0
        self.new_y = 0
        self.is_game_on = True

    def create_snake(self):
        for pos in starting_pos:
            new_segment = Turtle()
            new_segment.color(choice(color_list))
            new_segment.penup()
            new_segment.shape('square')
            new_segment.setx(pos)
            self.segments.append(new_segment)

    def move(self):
        for seg_no in range(len(self.segments) -1, 0, -1):
            self.new_x = self.segments[seg_no - 1].xcor()
            self.new_y = self.segments[seg_no - 1].ycor()
            color = choice(color_list)
            self.segments[seg_no].color(color)
            self.segments[seg_no].setx(self.new_x)
            self.segments[seg_no].sety(self.new_y)
        self.segments[0].forward(move_distance)
        self.segments[0].color(choice(color_list))
    def turnUp(self):
        if self.segments[0].heading() != 270 and self.segments[0].heading() != 90:
            self.segments[0].setheading(90)
    def turnDown(self):

        if self.segments[0].heading() != 270 and self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def turnRight(self):

        if self.segments[0].heading() != 180 and self.segments[0].heading() != 0:
            self.segments[0].setheading(0)
    def turnLefet(self):

        if self.segments[0].heading() != 180 and self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def gameOver(self):
        if self.segments[0].xcor() < -490 or self.segments[0].ycor() < -490:
            self.is_game_on = False
        elif self.segments[0].xcor() > 485 or self.segments[0].ycor() > 490:
            self.is_game_on = False
        for i in range(2, len(self.segments)):
            if self.segments[0].distance(self.segments[i]) < 10:
                self.is_game_on = False

    def wall(self):
        wall_pen = Turtle()
        wall_pen.speed('fastest')
        wall_pen.penup()
        wall_pen.pensize(30)
        wall_pen.sety(-490)
        wall_pen.setx(-490)
        wall_pen.pendown()
        wall_pen.forward(980)
        wall_pen.left(90)
        for i in range(1,4):
            wall_pen.forward(990)
            wall_pen.left(90)

    def add_segment(self):
        last_seg_x = self.segments[len(self.segments)-1].xcor()
        last_seg_y = self.segments[len(self.segments)-1].ycor()
        new_segment = Turtle()
        new_segment.color('black')
        new_segment.penup()
        new_segment.shape('square')
        if self.segments[len(self.segments)-1].heading() == 270:
            new_segment.sety(last_seg_y + 20)
            new_segment.setx(last_seg_x)
            self.segments.append(new_segment)
        elif self.segments[len(self.segments)-1].heading() == 90:
            new_segment.sety(last_seg_y - 20)
            new_segment.setx(last_seg_x)
            self.segments.append(new_segment)
        elif self.segments[len(self.segments)-1].heading() == 180:
            new_segment.setx(last_seg_x + 20)
            new_segment.sety(last_seg_y)
            self.segments.append(new_segment)
        elif self.segments[len(self.segments)-1].heading() == 0:
            new_segment.setx(last_seg_x - 20)
            new_segment.sety(last_seg_y)
            self.segments.append(new_segment)