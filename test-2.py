import turtle
turtle.setup(startx=10, starty=10)
tina = turtle.Turtle()
tina.shape('turtle')

def main():
    back_up()

def back_up():
    tina.penup()
    tina.backward(250)
    tina.pendown()

# tina.color("red")
# 
# tina.width(10)
# tina.left(60)
# tina.forward(100)
# tina.right(120)
# tina.forward(200)
# tina.left(120)
# tina.forward(100)
# tina.right(60)



main()
turtle.done()