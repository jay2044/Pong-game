from turtle import Turtle

class Paddle:
    def __init__(self, xcor, ycor):
        self.paddle = Turtle(shape="square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(xcor, ycor)

    def go_up(self):
        self.paddle.sety(self.paddle.ycor() + 20)

    def go_down(self):
        self.paddle.sety(self.paddle.ycor() - 20)
