import turtle

turtle.color('red')

turtle.up()
turtle.goto(-250, 250)
turtle.down()

turtle.begin_fill()

# draw square
for i in range(4):
    turtle.fd(400)
    turtle.right(90)
    
turtle.end_fill()

turtle.done()