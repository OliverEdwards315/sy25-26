import turtle
import time

# Screen setup
sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("black")
sc.setup(width=800, height=400)
sc.tracer(0)  # Manual screen updates

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("pink")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-350, 0)

# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 8.5  # Increased speed
ball.dy = 0.5

# Score variables
score_left = 0
score_right = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 160)
score_display.write("Player Left: 0  Player Right: 0", align="center", font=("Courier", 16, "normal"))

def update_score():
    score_display.clear()
    score_display.write(f"Player Left: {score_left}  Player Right: {score_right}", align="center", font=("Courier", 16, "normal"))

# Paddle movement functions
def left_pad_up():
    y = left_pad.ycor()
    if y < 160:
        left_pad.sety(y + 20)

def left_pad_down():
    y = left_pad.ycor()
    if y > -160:
        left_pad.sety(y - 20)

def right_pad_up():
    y = right_pad.ycor()
    if y < 160:
        right_pad.sety(y + 20)

def right_pad_down():
    y = right_pad.ycor()
    if y > -160:
        right_pad.sety(y - 20)

# Keyboard bindings
sc.listen()
sc.onkeypress(left_pad_up, "w")
sc.onkeypress(left_pad_down, "s")
sc.onkeypress(right_pad_up, "Up")
sc.onkeypress(right_pad_down, "Down")

# Game loop
while True:
    sc.update()
    time.sleep(0.01)  # Optional frame delay for consistent speed

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom collision
    if ball.ycor() > 190:
        ball.sety(190)
        ball.dy *= -1

    if ball.ycor() < -190:
        ball.sety(-190)
        ball.dy *= -1

    # Right wall — Left player scores
    if ball.xcor() > 390:
        score_left += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1

    # Left wall — Right player scores
    if ball.xcor() < -390:
        score_right += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1

    # Right paddle collision
    if (340 < ball.xcor() < 350) and (right_pad.ycor() - 60 < ball.ycor() < right_pad.ycor() + 60):
        ball.setx(340)
        ball.dx *= -1

    # Left paddle collision
    if (-350 < ball.xcor() < -340) and (left_pad.ycor() - 60 < ball.ycor() < left_pad.ycor() + 60):
        ball.setx(-340)
        ball.dx *= -1
