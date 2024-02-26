from time import*
from snake import*
from food import*
from score import*
# settings
speedOfSnake = 0.1
turn_up = 'w'
turn_right = 'd'
turn_down = 's'
turn_left = 'a'
# secreen
window = Screen()
window.bgcolor('#faedcd')
window.setup(width=1000, height=1000)
window.tracer(0)
window.title('SnakeXenizia')
# creating snake, food and score
snake = Snake()
snake.wall()
food = Food()
score = Score()
# controls
window.listen()
window.onkey(fun=snake.turnUp, key=turn_up)
window.onkey(fun=snake.turnRight, key=turn_right)
window.onkey(fun=snake.turnLefet, key=turn_left)
window.onkey(fun=snake.turnDown , key=turn_down)
# start game!
while snake.is_game_on :
    window.update()
    sleep(speedOfSnake)
    snake.move()
    snake.gameOver()
    if snake.segments[0].distance(food) < 20 :
        food.hideturtle()
        food = Food()
        score.hide_turtle()
        snake.add_segment()

window.mainloop()