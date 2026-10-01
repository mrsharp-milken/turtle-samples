import turtle
turtle.setup(startx=10, starty=10)
tina = turtle.Turtle()
tina.shape('turtle')

tina.forward(100)
tina.left(45)
tina.color('blue')
tina.forward(100)
tina.circle(50)

tina.penup()
tina.forward(100)
tina.pendown()
tina.width(5)
tina.forward(200 / 4)

turtle.done()