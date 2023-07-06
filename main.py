from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

def play_game():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    r_paddle = Paddle(350, 0)
    l_paddle = Paddle(-350, 0)
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkeypress(r_paddle.go_up, "Up")
    screen.onkeypress(r_paddle.go_down, "Down")
    screen.onkeypress(l_paddle.go_up, "w")
    screen.onkeypress(l_paddle.go_down, "s")

    def game_over():
        game_over_text = Turtle()
        game_over_text.color("white")
        game_over_text.penup()
        game_over_text.goto(0, 0)
        game_over_text.write("Game Over", align="center", font=("Courier", 24, "normal"))

        # Retry button
        retry_button = Turtle()
        retry_button.color("white")
        retry_button.penup()
        retry_button.goto(0, -50)
        retry_button.write("Retry", align="center", font=("Courier", 18, "normal"))

        # Function to handle retry button click
        def handle_click(x, y):
            if -50 < x < 50 and -70 < y < -30:
                screen.clear()  # Clear the screen
                play_game()  # Restart the game

        # Bind the handle_click function to mouse clicks on the screen
        screen.onscreenclick(handle_click)


    game_is_on = True
    while game_is_on:
        time.sleep(0.01)
        screen.update()
        ball.move()

        # Ball collision with top/bottom walls
        if abs(ball.ycor()) > 280:
            ball.bounce_y()

        # Ball collision with paddles
        if (ball.distance(r_paddle.paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle.paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()
            if ball.distance(r_paddle.paddle) < 50:
                scoreboard.increase_score_b()
            if ball.distance(l_paddle.paddle) < 50:
                scoreboard.increase_score_a()

        # Paddle boundaries
        for paddle in [r_paddle, l_paddle]:
            if paddle.paddle.ycor() > 250:
                paddle.paddle.sety(250)
            elif paddle.paddle.ycor() < -240:
                paddle.paddle.sety(-240)

        # Ball out of bounds
        if abs(ball.xcor()) > 390:
            ball.reset_position()
            game_is_on = False
            game_over()

    screen.mainloop()

play_game()
