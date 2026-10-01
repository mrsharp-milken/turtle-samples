import turtle
turtle.setup(startx=10, starty=10)
tina = turtle.Turtle()
tina.shape('turtle')

tina.width(50)
tina.speed(0)
tina.color('red', 'yellow')

tina.teleport(0, -300)
tina.begin_fill()
tina.circle(300)
tina.end_fill()

tina.teleport(0, -150)
tina.begin_fill()
tina.circle(150)
tina.end_fill()

turtle.done()
