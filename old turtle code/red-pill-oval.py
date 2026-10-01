import turtle

# turtle.hideturtle()
turtle.color('red')

turtle.penup()
turtle.goto(50,-100)
turtle.pendown()

turtle.begin_fill()

for i in range(12):
    turtle.forward(100)
    turtle.circle(20, 180)
    turtle.forward(100)
    turtle.right(150)

    
turtle.end_fill()