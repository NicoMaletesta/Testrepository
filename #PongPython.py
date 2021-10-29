#PongPython
import turtle

Window = turtle.Screen()
#SettaggioScreen
#Titoloschermo
Window.title("NicoPong")
#coloreschermo
Window.bgcolor("green")
#grandezzaschermo
Window.setup(width=1200, height=1000)
#velocizzailgioco diminuendo quante volte viene ricaricato lo schermo
Window.tracer(0)

#Giocatore1
player1=turtle.Turtle()
#velocitaanimazione
player1.speed(0)
player1.shape("square")
player1.color("brown", "black")
player1.shapesize(stretch_wid=5,stretch_len=1)
player1.penup()
player1.goto(-450,0)
#Giocatore2
player2=turtle.Turtle()

player2.speed(0)
player2.shape("square")
player2.color("black", "brown")
player2.shapesize(stretch_wid=5,stretch_len=1)
player2.penup()
player2.goto(450,0)
#Palla
ball=turtle.Turtle()

ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1
#Punteggio
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))
punteggio_1 = 0
punteggio_2 = 0
#FunzioniMovimento
#Player1
def player1_up():
    y=player1.ycor()
    y += 20
    player1.sety(y)

def player1_down():
    y=player1.ycor()
    y -= 20
    player1.sety(y)
    
#Player2
def player2_up():
    y=player2.ycor()
    y += 20
    player2.sety(y)

def player2_down():
    y=player2.ycor()
    y -= 20
    player2.sety(y)



#ComandiGiocatori
Window.listen()
Window.onkeypress(player1_up, "w")
Window.onkeypress(player1_down, "s")
Window.onkeypress(player2_up, "Up")
Window.onkeypress(player2_down, "Down")
#Corpocodice
while True:
    Window.update()
   #MovimentoPalla
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #FisicitàBordi
    if ball.ycor()>490:
       ball.sety(490)
       ball.dy *= -1
    if ball.ycor()<-490:
       ball.sety(-490)
       ball.dy *= -1       
    if ball.xcor()>500:
       
       ball.goto(0,0)
       ball.dx *= -1
       punteggio_1 +=1
       pen.clear()
       pen.write("Player 1: {}  Player 2: {}".format(punteggio_1, punteggio_2), align="center", font=("Courier", 24, "normal"))
    if ball.xcor()<-500:
       punteggio_2 +=1
       pen.clear()
       pen.write("Player 1: {}  Player 2: {}".format(punteggio_1, punteggio_2), align="center", font=("Courier", 24, "normal"))
       ball.goto(0,0)
       ball.dx *= -1 
       punteggio_2 +=1    

      
    #CollisionePalla-Giocatore
    if (ball.xcor()>440 and ball.xcor()<450 ) and (ball.ycor()<player2.ycor() + 50 and ball.ycor()>player2.ycor() -55 ):
       ball.setx(440)
       ball.dx *=-1.1
    if (ball.xcor()<-440 and ball.xcor()>-450 ) and (ball.ycor()<player1.ycor() +50 and ball.ycor()>player1.ycor() -55 ):
       ball.setx(-440)
       ball.dx *=-1.1   