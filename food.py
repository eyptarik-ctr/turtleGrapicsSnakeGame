from turtle import Turtle
from random import*
from snake import color_list
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color(choice(color_list))
        self.penup()
        self.speed('fastest')
        self.rand_x = randint(-475, 470)
        self.rand_y = randint(-475, 470)
        self.setx(self.rand_x)
        self.sety(self.rand_y)

