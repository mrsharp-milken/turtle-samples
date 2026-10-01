import turtle
turtle.setup(startx=10, starty=10)
tina = turtle.Turtle()
tina.shape('turtle')

def main():
    s() # Sasha
    letterh() # Nash
    letter_A() # Andre
    R() # Darian
    letter_p() # Pip


    delay_and_restart()


def s():
    tina.right(90)
    tina.backward(50)
    tina. right(90)
    tina.forward(90)
    tina.left(90)
    tina.forward(50)
    tina.right(90)
    tina.forward(90)
    tina.left(90)
    tina.backward(50)
    
def letterh():
    tina.right(180)
    tina.forward(30)
    tina.left(90)
    tina.pendown()
    tina.forward(100)
    tina.right(90)
    tina.penup()
    tina.forward(40)
    tina.right(90)
    tina.pendown()
    tina.forward(100)
    tina.right(180)
    tina.penup()
    tina.forward(50)
    tina.left(90)
    tina.pendown()
    tina.forward(40)
    tina.penup()
    tina.forward(165)
    tina.right(90)
    tina.pendown()

def letter_A():
    tina.color('CornflowerBlue')
    tina.forward(100)
    tina.right (150)
    tina.forward(100)
    tina.right(180)
    tina.forward(45)
    tina.right(-80)
    tina.forward(30)
    tina.right(-180)
    tina.forward(30)

def R():
    tina.color('Bisque3')
    tina.forward (70)
    tina.pendown()
    tina.left(90)
    tina.forward(85)
    tina.right(20)
    tina. circle (-25)
    tina.right(140)
    tina.forward(90)
    tina.left(70)
    tina.penup()
    

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
