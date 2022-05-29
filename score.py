from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 4
        self.update_score()
        self.reset_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 300)
        self.write(f'Score: {self.score}', align='center', font=('Courier', 22, 'normal'))
        self.goto(100, 300)
        self.write(f'Lives: {self.lives}', align='center', font=('Courier', 22, 'normal'))

    def point(self, no):
        self.score += no
        self.update_score()

    def lives_left(self):
        self.lives -= 1
        self.update_score()

    def reset_score(self):
        self.lives_left()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over'.upper(), align='center', font=('Courier', 40, 'normal'))

    def you_win(self):
        self.goto(0, 0)
        self.write('You Win!!!'.upper(), align='center', font=('Courier', 40, 'normal'))
