from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle = Turtle()
        self.length = 5
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=self.length)
        self.penup()
        self.goto(0, -320)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def reset_paddle(self):
        self.hideturtle()
        self.goto(0, -320)
        self.showturtle()
