import turtle
turtle.setup(startx=10, starty=10)
tina = turtle.Turtle()
tina.shape('turtle')
tina.width(200)
tina.speed(10)


def main():
    move_over()
    tina.color("darkseagreen")
    hills()
    tina.color("mediumseagreen")
    hills()
    tina.color("darkgreen")
    hills()
    hills()




def move_over():
    tina.penup()
    tina.forward(450)
    tina.pendown()
    tina.left(90)

def hills():
    tina.circle(160, 180)
    tina.left(180)
    tina.circle(160, 180)
    tina.left(180)
    tina.circle(160, 180)
    tina.forward(150)
    tina.right(90)
    tina.backward(1000)
    tina.right(90)





main()



