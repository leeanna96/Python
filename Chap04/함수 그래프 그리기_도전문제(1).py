import math
import turtle

t=turtle.Turtle()

t.pendown()
for angle in range(360):
    y=math.cos(math.radians(angle))

    scaledX=angle
    scaledY=y*100
    t.goto(scaledX,scaledY)

t.penup()
