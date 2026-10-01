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
    size_height = 50
    draw_outline(size_height, size_height)
    # TODO: Replace letter_U(size_height) with a
    # call to your letter function
    letter_U(size_height)

# TODO: Replace this definition of question_mark(size)
# with your letter function definition
def letter_U(size_height):
    tina.penup()
    tina.left(90)
    tina.forward(size_height * 0.40)
    tina.pendown()
    tina.forward(size_height * 0.60)
    tina.backward(size_height * 0.60)
    tina.left(180)
    tina.circle(size_height * 0.40, 180)
    tina.forward(size_height * 0.60)
    tina.penup()
    tina.backward(size_height * 1)
    tina.right(90)
    tina.forward(size_height * 0.50)
    


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
