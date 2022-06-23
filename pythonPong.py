

# ##########################################
# written by: Tuscanny Polk
# date: June 23, 2022
# Purpose: To improve my skills in Python
# ##########################################


import turtle
import os

win = turtle.Screen()
win.title("Pong by TuscannyCodes")
win.bgcolor("cadetblue")
win.setup(width=800, height=600)
win.tracer(0)

# score
scoreL = 0
scoreR = 0



# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("coral")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("coral")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("coral")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2


pen = turtle.Turtle()
pen.speed(0)
pen.color("coral")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player L: 0 Player R: 0", align= "center", font=("courier",24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")

win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")

# Main game loop

while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreL += 1
        pen.clear()
        pen.write(f"player L: {scoreL} Player R: {scoreR}", align="center", font=("courier", 24, "normal"))



    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreR += 1
        pen.clear()
        pen.write(f"player L: {scoreL} Player R: {scoreR}", align="center", font=("courier", 24, "normal"))
# collide ball with paddle
    if (ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50)):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50)):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")








