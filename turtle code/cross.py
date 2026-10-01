import turtle

tina = turtle.Turtle()

tina.up()
tina.goto(50, -50)
tina.down()

tina.color('red')

tina.begin_fill()

# draw square
for i in range(8):
    tina.forward(200)
    tina.circle(50, 180)
    tina.forward(200)
    tina.right(135)

tina.end_fill()

turtle.done()
