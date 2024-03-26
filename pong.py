import turtle 
from playsound import playsound 

wn = turtle.Screen()
wn.title("Pong by @AquilOps LLC")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#gamer A
gamer_a = turtle.Turtle()
gamer_a.speed(0)
gamer_a.shape("square")
gamer_a.color("white")
gamer_a.shapesize(stretch_wid=5, stretch_len=1)
gamer_a.penup()
gamer_a.goto(-350,0)

#gamer B
gamer_b = turtle.Turtle()
gamer_b.speed(0)
gamer_b.shape("square")
gamer_b.color("white")
gamer_b.shapesize(stretch_wid=5, stretch_len=1)
gamer_b.penup()
gamer_b.goto(350,0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1/8
ball.dy = 1/8


#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B:0", align="center", font=("Courier", 24, "normal"))

#Function
def gamer_a_up():
    y = gamer_a.ycor()
    y += 40
    gamer_a.sety(y)

def gamer_a_down():
    y = gamer_a.ycor()
    y -= 40
    gamer_a.sety(y)


def gamer_b_up():
    y = gamer_b.ycor()
    y += 40
    gamer_b.sety(y)
 

def gamer_b_down():
    y = gamer_b.ycor()
    y -= 40
    gamer_b.sety(y)

#Keyboard Binding
wn.listen()
wn.onkeypress(gamer_a_up, "w")
wn.onkeypress(gamer_a_down, "s")
wn.onkeypress(gamer_b_up, "Up")
wn.onkeypress(gamer_b_down, "Down")


#Main Game Loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border check
    if ball.ycor() > 290:
       ball.sety(290)
       ball.dy *= -1
       playsound("beeep.mp3")
    elif ball.ycor() < -290:
       ball.sety(-290)
       ball.dy *= -1
       playsound("beeep.mp3")

    if ball.xcor() > 350:
       score_a += 1
       pen.clear()
       pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
       ball.goto(0, 0)
       ball.dx *= -1      

    elif ball.xcor() < -350:
       score_b += 1
       pen.clear()
       pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
       ball.goto(0, 0)
       ball.dx *= -1      
  

    # Gamer and ball collisions
    if ball.xcor() < -340 and ball.ycor() < gamer_a.ycor() + 50 and ball.ycor() > gamer_a.ycor() - 50:
        ball.dx *= -1 
        playsound("beeep.mp3")

    elif ball.xcor() > 340 and ball.ycor() < gamer_b.ycor() + 50 and ball.ycor() > gamer_b.ycor() - 50:
        ball.dx *= -1
        playsound("beeep.mp3")

