"""
This is the playground of turtle

HomeWork
at least 25 command lines
"""

import turtle

SPEED = 10

TOPLEFT_X, TOPLEFT_Y = -384, 324  # 768, 648, 13 x 16
DIFF_X, DIFF_Y = 60, 40.5

ANGLE = 90

turtle.speed(SPEED)
# grid()
turtle.penup()
turtle.goto(TOPLEFT_X, TOPLEFT_Y)

turtle.penup()
turtle.forward(3*DIFF_X)

# Hat
turtle.pendown()
turtle.color("black", "red")
turtle.begin_fill()
turtle.forward(6 * DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.left(ANGLE)
turtle.forward(3 * DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.right(ANGLE)
turtle.forward(10 * DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.right(ANGLE)
turtle.forward(DIFF_X)
turtle.left(ANGLE)
turtle.forward(DIFF_Y)
turtle.end_fill()

# face
turtle.penup()
turtle.backward(2 * DIFF_Y)
turtle.right(ANGLE)

turtle.pendown()
turtle.begin_fill()
turtle.color("black", "#FACC9C")
turtle.forward(7 * DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.left(ANGLE)
turtle.forward(2 * DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.left(ANGLE)
turtle.forward(DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.right(ANGLE)
turtle.forward(DIFF_X)
turtle.left(ANGLE)
turtle.forward(DIFF_Y)
turtle.right(ANGLE)
turtle.forward(DIFF_X)
turtle.left(ANGLE)
turtle.forward(DIFF_Y)
turtle.right(ANGLE)
turtle.forward(8 * DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.left(ANGLE)
turtle.forward(2 * DIFF_X)
turtle.right(ANGLE)
turtle.forward(3 * DIFF_Y)
turtle.right(ANGLE)
turtle.forward(DIFF_X)
turtle.left(ANGLE)
turtle.forward(DIFF_Y)
turtle.right(ANGLE)
turtle.forward(DIFF_X)
turtle.end_fill()

# hair
turtle.color("black", "#874306")
turtle.begin_fill()
turtle.forward(2 * DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.right(ANGLE)
turtle.forward(DIFF_X)
turtle.left(ANGLE)
turtle.forward(DIFF_Y)
turtle.left(ANGLE)
turtle.forward(DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.right(ANGLE)
turtle.forward(2 * DIFF_X)
turtle.right(ANGLE)
turtle.forward(2 * DIFF_Y)
turtle.left(ANGLE)
turtle.forward(DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.right(ANGLE)
turtle.forward(DIFF_X)
turtle.end_fill()

turtle.backward(DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.begin_fill()
turtle.forward(2 * DIFF_Y)
turtle.left(ANGLE)
turtle.forward(DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.right(ANGLE)
turtle.forward(2 * DIFF_X)
turtle.right(ANGLE)
turtle.forward(3 * DIFF_Y)
turtle.right(ANGLE)
turtle.forward(DIFF_X)
turtle.end_fill()

# eyes and moustache
turtle.penup()
turtle.forward(7 * DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.left(ANGLE)
turtle.forward(DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.left(ANGLE)
turtle.forward(2 * DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.right(ANGLE)
turtle.forward(4 * DIFF_X)
turtle.right(ANGLE)
turtle.forward(DIFF_Y)
turtle.right(ANGLE)
turtle.forward(DIFF_X)
turtle.left(ANGLE)
turtle.forward(DIFF_Y)
turtle.end_fill()

turtle.begin_fill()
turtle.forward(2 * DIFF_Y)
turtle.left(ANGLE)
turtle.forward(DIFF_X)
turtle.left(ANGLE)
turtle.forward(2 * DIFF_Y)
turtle.left(ANGLE)
turtle.forward(DIFF_X)
turtle.end_fill()

# turtle.shape("turtle")
# turtle.penup()
# turtle.right(100)
# turtle.circle(100, 180)
# turtle.width(3)
# turtle.pendown()
# turle.home()


turtle.mainloop()
