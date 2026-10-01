import turtle
turtle.setup(startx=10, starty=10)
tina = turtle.Turtle()
tina.shape('turtle')

tina.up()
tina.goto(-200, -100)
tina.down()

tina.width(5)
tina.color("purple")

tina.begin_fill()
tina.forward(400)
tina.left(120)
tina.forward(400)
tina.left(120)
tina.forward()
tina.end_fill()





turtle.done()