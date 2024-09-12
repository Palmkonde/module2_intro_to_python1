"""
This is the playground of turtle

HomeWork
at least 25 command lines
"""

import turtle

SPEED = 10
TRIANGLE_LENGTH = 200
TRIANGLE_LEFT_TURN_ANGLE = 120

SQUARE_LENGTH = 200
SQUARE_ANGLE = 90

CIRCLE_RADIUS = 100

TOPLEFT_X, TOPLEFT_Y = -384, 324  # 768, 648

turtle.speed(SPEED)
turtle.penup()
turtle.goto(TOPLEFT_X, TOPLEFT_Y)

# turtle.shape("turtle")
# turtle.penup()
# turtle.right(100)
# turtle.circle(100, 180)
# turtle.width(3)
# turtle.pendown()
# turle.home()


turtle.mainloop()
