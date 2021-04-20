import turtle, time
import winsound as ws

# Window
wn = turtle.Screen()
wn.title('Pong')
wn.setup(width=1000, height=700, startx=None, starty=-30)
wn.bgcolor('black')
wn.tracer(0)

# Score
score_a, score_b = 0, 0

# Paddle_A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('lime', 'lime')
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5, stretch_len=1, outline=5)
paddle_a.goto(-450, 0)
paddle_a.dy1 = 20
paddle_a.dy2 = 20

# Paddle_B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('lime', 'lime')
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5, stretch_len=1, outline=5)
paddle_b.goto(450, 0)
paddle_b.dy1 = 20
paddle_b.dy2 = 20

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white','white')
ball.penup()
ball.shapesize(stretch_wid=1, stretch_len=1, outline=5)
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# Pen Score
pens = turtle.Turtle()
pens.penup()
pens.speed(0)
pens.color('blue')
pens.goto(0,250)
pens.hideturtle()
pens.write('Player 1: {}   Player 2: {}'.format(score_a, score_b), align = 'center', font = ('Arial', 24, 'bold'))

# Pen Winner
penw = turtle.Turtle()
penw.penup()
penw.speed(0)
penw.goto(0, 20)
penw.color('blue')
penw.hideturtle()
penw.write('', align = 'center', font = ('Arial', 24, 'normal'))

# Frame
frame = turtle.Turtle()
frame.shape('square')
frame.speed(0)
frame.color("Gray", "")
frame.shapesize(stretch_wid=30, stretch_len=48, outline=5)

# Functions
def paddle_a_up():
    paddle_a.sety(paddle_a.ycor()+paddle_a.dy1)

def paddle_a_down():
    paddle_a.sety(paddle_a.ycor()-paddle_a.dy2)

def paddle_b_up():
    paddle_b.sety(paddle_b.ycor()+paddle_b.dy1)

def paddle_b_down():
    paddle_b.sety(paddle_b.ycor()-paddle_b.dy2)

def gameexit():
    wn.bye()

# Key_bindings
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')
wn.onkey(gameexit, 'Escape')

# Game_main_loop
while True:
    
    wn.update()
    
    # A Win
    if score_a >= 10 and score_b+2 <= score_a:
        ws.PlaySound('Win.wav', ws.SND_ASYNC)
        wn.onkeypress(None, 'w')
        wn.onkeypress(None, 's')
        wn.onkeypress(None, 'Up')
        wn.onkeypress(None, 'Down')
        penw.write('Player 1 Win!', align = 'center', font = ('Arial', 40, 'normal'))
        time.sleep(4)
        score_a = 0
        score_b = 0
        pens.clear()
        penw.clear()
        pens.write('Player 1: {}   Player 2: {}'.format(score_a, score_b), align = 'center', font = ('Arial', 24, 'bold'))
        wn.onkeypress(paddle_a_up, 'w')
        wn.onkeypress(paddle_a_down, 's')
        wn.onkeypress(paddle_b_up, 'Up')
        wn.onkeypress(paddle_b_down, 'Down')
    
    # B Win
    if score_b >= 10 and score_a+2 <= score_b:
        ws.PlaySound('Win.wav', ws.SND_ASYNC)
        wn.onkeypress(None, 'w')
        wn.onkeypress(None, 's')
        wn.onkeypress(None, 'Up')
        wn.onkeypress(None, 'Down')
        penw.write('Player 1 Win!', align = 'center', font = ('Arial', 40, 'normal'))
        time.sleep(4)
        score_a = 0
        score_b = 0
        pens.clear()
        penw.clear()
        pens.write('Player 1: {}   Player 2: {}'.format(score_a, score_b), align = 'center', font = ('Arial', 24, 'bold'))
        wn.onkeypress(paddle_a_up, 'w')
        wn.onkeypress(paddle_a_down, 's')
        wn.onkeypress(paddle_b_up, 'Up')
        wn.onkeypress(paddle_b_down, 'Down')
    
    # Ball_move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball_borders_x
    if ball.xcor() > 465:
        ws.PlaySound('Goal.wav', ws.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pens.clear()
        pens.write('Player 1: {}   Player 2: {}'.format(score_a, score_b), align = 'center', font = ('Arial', 24, 'bold'))

    if ball.xcor() < -465:
        ws.PlaySound('Goal.wav', ws.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pens.clear()
        pens.write('Player 1: {}   Player 2: {}'.format(score_a, score_b), align = 'center', font = ('Arial', 24, 'bold'))

    # Ball_borders_y
    if ball.ycor() > 285:
        ball.sety(285)
        ball.dy *= -1
    #if ball.ycor() == 250 and ball.dy > 0:
        ws.PlaySound("BounceWall.wav", ws.SND_ASYNC)

    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1
    #if ball.ycor() == -250 and ball.dy < 0:
        ws.PlaySound("BounceWall.wav", ws.SND_ASYNC)

    # Paddle_A_borders
    if paddle_a.ycor() > 230:
        paddle_a.dy1 = 0
    else:
        paddle_a.dy1 = 20

    if paddle_a.ycor() < -230:
        paddle_a.dy2 = 0
    else:
        paddle_a.dy2 = 20
 
    # Paddle_B_borders
    if paddle_b.ycor() > 230:
        paddle_b.dy1 = 0
    else:
        paddle_b.dy1 = 20

    if paddle_b.ycor() < -230:
        paddle_b.dy2 = 0
    else:
        paddle_b.dy2 = 20

    # Collisions
    if (ball.xcor() > 425 and ball.xcor() < 435) and (ball.ycor() > (paddle_b.ycor()-55) and ball.ycor() < (paddle_b.ycor()+55)):
        ball.dx *= -1
        ball.setx(ball.xcor()-1)
        ws.PlaySound("Bounce.wav", ws.SND_ASYNC)

    if (ball.xcor() < -425 and ball.xcor() > -435) and (ball.ycor() > (paddle_a.ycor()-55) and ball.ycor() < (paddle_a.ycor()+55)):
        ball.dx *= -1
        ball.setx(ball.xcor()+1)
        ws.PlaySound("Bounce.wav", ws.SND_ASYNC)