from turtle import *
from paddle import Paddle
from ball import Ball
from score import Score
import time

YELLOW_BLOCKS = []
ORANGE_BLOCKS = []
RED_BLOCKS = []
DEEP_ORANGE_BLOCKS = []
DEEP_RED_BLOCKS = []
ALL_BLOCKS = []
HITTED = []


def game():
    # screen setup
    screen = Screen()
    screen.setup(width=800, height=700)
    screen.bgcolor('black')
    screen.title('Break Out')
    screen.tracer(0)

    # creating yellow blocks
    pos_x = -345
    pos_y = 100
    pos_x1 = -345
    for x in range(22):
        block = Turtle()
        block.speed('fastest')
        block.penup()
        block.color('yellow')
        block.shape('square')
        block.shapesize(stretch_wid=1, stretch_len=3)
        if pos_x > 355:
            block.sety(130)
            block.setx(pos_x1)
            pos_x1 += 70
        else:
            block.sety(pos_y)
            block.setx(pos_x)
            pos_x += 70
        YELLOW_BLOCKS.append(block)
        ALL_BLOCKS.append(block)

    # creating orange blocks
    or_posx = -345
    or_posy = 165
    or_posx1 = -345
    for x in range(22):
        block = Turtle()
        block.speed('fastest')
        block.penup()
        block.color('orange')
        block.shape('square')
        block.shapesize(stretch_wid=1, stretch_len=3)
        if or_posx > 355:
            block.sety(190)
            block.setx(or_posx1)
            or_posx1 += 70
        else:
            block.sety(or_posy)
            block.setx(or_posx)
            or_posx += 70
        ORANGE_BLOCKS.append(block)
        ALL_BLOCKS.append(block)

    # creating red blocks
    red_posx = -345
    red_posy = 230
    red_posx1 = -345
    for x in range(22):
        block = Turtle()
        block.speed('fastest')
        block.penup()
        block.color('red')
        block.shape('square')
        block.shapesize(stretch_wid=1, stretch_len=3)
        if red_posx > 355:
            block.sety(265)
            block.setx(red_posx1)
            red_posx1 += 70
        else:
            block.sety(red_posy)
            block.setx(red_posx)
            red_posx += 70
        RED_BLOCKS.append(block)
        ALL_BLOCKS.append(block)

    # object instantiations
    paddle = Paddle()
    ball = Ball()
    score = Score()

    # event listeners i.e key control
    screen.listen()
    screen.onkey(fun=paddle.go_left, key='Left')
    screen.onkey(fun=paddle.go_right, key='Right')

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        ball.move()

        # detect collision with blocks
        for block in ALL_BLOCKS:
            if ball.distance(block) < 40:

                if block in YELLOW_BLOCKS:
                    score.point(1)
                    ALL_BLOCKS.remove(block)
                    block.hideturtle()
                    block.clear()

                elif block in ORANGE_BLOCKS:
                    score.point(2)
                    block.color('green')
                    # keeping count of hits for orange blocks
                    if block in DEEP_ORANGE_BLOCKS:
                        ALL_BLOCKS.remove(block)
                        block.hideturtle()
                        block.clear()
                    else:
                        DEEP_ORANGE_BLOCKS.append(block)

                elif block in RED_BLOCKS:
                    score.point(3)
                    block.color('pink')
                    # keeping count of hits for red blocks
                    if block in DEEP_RED_BLOCKS:
                        ALL_BLOCKS.remove(block)
                        block.hideturtle()
                        block.clear()
                    else:
                        DEEP_RED_BLOCKS.append(block)
                HITTED.append(block)
                ball.bounce_y()

        # detect collision with paddle
        if ball.distance(paddle) < 30:
            ball.bounce_y()

        # detect collision with wall
        if ball.xcor() >= 380 or ball.xcor() <= -380:
            ball.bounce_x()
        elif ball.ycor() >= 275:
            ball.bounce_y()

        # detect when ball misses paddle
        if ball.ycor() < -320:
            if score.lives == 0:
                score.game_over()
                game_is_on = False
            else:
                # paddle.reset_paddle()
                ball.reset_ball()
                score.reset_score()

        # detect when there are no more blocks
        if len(ALL_BLOCKS) == 0:
            score.you_win()
            game_is_on = False

    screen.exitonclick()


game()
