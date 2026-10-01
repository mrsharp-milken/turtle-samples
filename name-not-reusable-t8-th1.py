import turtle
turtle.setup(startx=10, starty=10)
tina = turtle.Turtle()
tina.shape('turtle')

def main():
    drawS() # Sarah
    H() # Henry
    draw_a() # Sajan
    R() # Rishi
    letter_p() # Pip


    delay_and_restart()


def drawS():
    tina.circle(70,180)
    tina.circle(-70,180)
    
def H():
    tina.fd(100)
    tina.bk(50)
    tina.rt(90)
    tina.fd(50)
    tina.lt(90)
    tina.fd(50)
    tina.bk(100)

def draw_a():
    tina.left(75)
    tina.forward(100)
    tina.right(150)
    tina.forward(100)
    tina.backward(50)
    tina.right(105)
    tina.forward(26)

def R():
    tina. penup()
    tina.goto(-250, -250)
    tina. pendown ()
    tina. setheading(90)
    tina. forward (100)
    tina.right(90)
    tina. forward (50)
    tina.right (90)
    tina.forward(50)
    tina. right (90)
    tina. forward (50)
    tina. penup()
    tina.goto(-200, -200)
    tina. pendown ()
    tina. setheading(315)
    tina. forward (70)
    tina. penup ()
    tina.goto(-150, -150)
    tina.pendown()
    

def letter_p():
    tina.pendown()
    tina.forward(10)
    tina.circle(50)
    tina.left(180)
    tina.right(90)
    tina.penup()
    tina.forward(100)
    tina.pendown()
    tina.left(90)
    tina.forward(100)

def delay_and_restart():
    tina.hideturtle()
    tina.penup()
    tina.speed(1)
    tina.forward(500)
    tina.reset()
    tina.width(5)
    main()

turtle.hideturtle()
turtle.penup()
turtle.color("red")
turtle.goto(-450, -200)
turtle.write("Copy others' functions from the sheet", move=False, align="left", font=("Arial", 60, "bold"))
turtle.goto(-450, -280)
turtle.write("Use them to write your name", move=False, align="left", font=("Arial", 60, "bold"))
tina.width(5)
main()
turtle.done()

