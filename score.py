from turtle import Turtle
class Score():
    def __init__(self):
        self.score_value = 0
        self.increase_score()
    def increase_score(self):
        self.current_score = Turtle()
        self.current_score.hideturtle()
        self.current_score.penup()
        self.current_score.setx(-60)
        self.current_score.sety(420)
        self.current_score.write(f'Score {self.score_value}', font=('ariel', 35, 'bold'))
        self.score_value += 1
    def hide_turtle (self):
        self.current_score.clear()
        self.current_score.write(f'Score {self.score_value}', font=('ariel', 35, 'bold'))
        self.score_value += 1
