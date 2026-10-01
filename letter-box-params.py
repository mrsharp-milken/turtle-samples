# Red outline - Copy with Cmd + A
'''
Use this program to help you add a size parameter
to your letter function

Copy in your letter function's definition, then
call it from the main() function
'''
import turtle
turtle.setup(startx=10, starty=10)
tina = turtle.Turtle()
tina.shape('turtle')

def main():
    size_height = 100
    draw_outline(size_height, size_height)
    # TODO: Replace question_mark(size_height) with a
    # call to your letter function
    question_mark(size_height)

# TODO: Replace this definition of question_mark(size)
# with your letter function definition
def question_mark(size_height):
    tina.penup()
    tina.left(90)
    tina.forward(size_height * 0.75)
    tina.pendown()
    tina.circle(size_height * -0.25, 230)
    tina.forward(size_height * 0.05)
    tina.circle(size_height * 0.25, 50)
    tina.forward(size_height * 0.20)
    tina.penup()
    tina.forward(size_height * 0.10)
    tina.pendown()
    tina.dot(size_height * 0.08)
    tina.penup()
    tina.forward(size_height * 0.035)
    tina.left(90)
    tina.forward(size_height * 0.25)
    tina.pendown()


# DO NOT EDIT THIS FUNCTION
def draw_outline(height, width):
    tina.width(3)
    tina.color('red')
    tina.penup()
    tina.goto(-5, -5)
    tina.pendown()
    tina.goto(-5, height + 5)
    tina.goto(width + 5, height + 5)
    tina.goto(width + 5, -5)
    tina.goto(-5, -5)
    tina.penup()
    tina.goto(0, 0)
    tina.pendown()
    tina.width(1)
    tina.forward(width)
    tina.goto(0,0)
    tina.color('black')

main()
turtle.done()

