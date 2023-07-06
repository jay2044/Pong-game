from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed = 3
        self.reset_position()

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # Increase the speed of the ball with each bounce

    def reset_position(self):
        self.goto(0, 0)
        self.x_move = self.move_speed
        self.y_move = self.move_speed
        self.move_speed = 3
