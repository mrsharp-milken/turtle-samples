import turtle
turtle.setup(startx=10, starty=10)
tina = turtle.Turtle()
tina.shape('turtle')

def main():
#     s() # Sarah 
#     letterh() # Mathai
    letter_a() # Valentina
#     r() # Uri
#     write_p() # Pierson
# 
# 
#     delay_and_restart()


def s():
    tina.width(20)
    tina.penup()
    tina.backward(350)
    tina.pendown()
    tina.forward(30)
    tina.circle(70,180)
    tina.forward(1)
    tina.circle(-50,180)
    tina.forward(30)

def letterh():
    tina.left(90)
    tina.forward(100)
    tina.left(180)
    tina.forward(50)
    tina.left(90)
    tina.forward(50)
    tina.left(90)
    tina.forward(50)
    tina.left(180)
    tina.forward(100)

def letter_a():
    valentina = tina
    valentina.right(120)
    valentina.forward(100)
    valentina.penup()
    valentina.right(180)
    valentina.forward(100)
    valentina.right(120)
    valentina.pendown()
    valentina.forward(100)
    valentina.penup()
    valentina.right(180)
    valentina.forward(50)
    valentina.left(60)
    valentina.pendown()
    valentina.forward(50)

def r():
    tina.width(12)
    tina.left(90)
    tina.forward(80)
    tina.left(-45)
    tina.forward(40)
    tina.forward(-40)
    tina.left(45)
    tina.forward(20)
    tina.penup()
    tina.left(-90)
    tina.forward(100)
    tina.pendown()

def write_p ():
    tina.left(90)
    tina.forward(100)
    tina.right(90)
    tina.circle(25, 180)
    tina.left(90)
    tina.forward(100)
    tina.forward(50)
    tina.left(90)

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