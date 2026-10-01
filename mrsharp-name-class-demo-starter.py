import turtle
turtle.setup(startx=10, starty=10)
tina = turtle.Turtle()
tina.shape('turtle')

tina.width(10)
tina.color('turquoise')

GAP = 20     # space between letters
SPACE = 45   # space between words

# ---- get to the starting spot without teleport/goto, just moves and turns ----
tina.penup()
tina.left(180)
tina.forward(250)
tina.left(90)
tina.forward(50)
tina.left(90)          # now facing east, ready to draw


def draw_M(t):
    t.pendown()
    t.left(90); t.forward(60)      # left leg up
    t.right(135); t.forward(40)    # diagonal down to the middle
    t.left(90); t.forward(40)      # diagonal up to the peak
    t.right(135); t.forward(60)    # right leg down
    t.penup()
    t.left(90); t.forward(GAP)


def draw_R(t):
    t.pendown()
    t.left(90); t.forward(60)      # stem up
    t.right(90)                    # face across the top
    t.circle(-15, 180)             # the bowl
    t.left(135); t.forward(45)     # kicking leg down
    t.penup()
    t.left(45); t.forward(GAP)


def draw_period(t):
    t.pendown()
    t.circle(3, 360)
    t.penup()
    t.forward(GAP)


def draw_S(t):
    t.pendown()
    t.circle(15, 180)              # top curve
    t.circle(-15, 180)             # bottom curve, opposite way
    t.penup()
    t.forward(GAP)


def draw_H(t):
    t.pendown()
    t.left(90); t.forward(60)      # left stem
    t.penup()
    t.backward(60)
    t.right(90); t.forward(40)     # slide over to the right stem's base
    t.left(90)
    t.pendown(); t.forward(60)     # right stem
    t.penup()
    t.backward(30)
    t.left(90)
    t.pendown(); t.forward(40)     # crossbar
    t.penup()
    t.backward(40)
    t.left(90); t.forward(30)
    t.left(90); t.forward(GAP)


def draw_A(t):
    t.pendown()
    t.left(45); t.forward(56)      # left leg up to the peak
    t.right(90); t.forward(56)     # right leg down
    t.penup()
    t.backward(28)                 # halfway back up the right leg
    t.right(135)
    t.pendown(); t.forward(40)     # crossbar
    t.penup()
    t.backward(40)
    t.left(135); t.forward(28)     # back down to the bottom of the right leg
    t.left(45); t.forward(GAP)


def draw_P(t):
    t.pendown()
    t.left(90); t.forward(60)      # stem up
    t.right(90)
    t.circle(-15, 180)             # the bowl (no leg, unlike R)
    t.penup()
    t.left(90); t.forward(30)      # back down to the baseline
    t.left(90); t.forward(40)      # clear the bowl's width
    t.forward(GAP)


draw_M(tina)
draw_R(tina)
draw_period(tina)
tina.forward(SPACE)
draw_S(tina)
draw_H(tina)
draw_A(tina)
draw_R(tina)
draw_P(tina)

tina.hideturtle()
turtle.done()