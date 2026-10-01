import turtle

screen = turtle.Screen() # need this for input to work!

tina = turtle.Turtle()

tina.shape('turtle')


num = screen.textinput("Size", "How big are the circles?")
# make it an integer
num = int(num)

my_color = screen.textinput("Color", "What color to use?")

tina.color(my_color)

tina.penup()
tina.goto(-250, 0)
tina.pendown()


# use num in the loop to repeat num times!

for i in range(3):
    tina.begin_fill()
    tina.circle(num)
    tina.end_fill()

    tina.penup()
    
    tina.forward(circle_gap)

    tina.pendown()


turtle.done()