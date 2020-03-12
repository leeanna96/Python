import turtle

t=turtle.Turtle()

t.pendown()
for angle in range(360):
    scaledX=angle
    scaledY=0
    t.goto(scaledX,scaledY)
for angle in range(360):
    scaledX=-angle
    scaledY=0
    t.goto(scaledX,scaledY)
for angle in range(180):
    scaledX=0
    scaledY=angle
    t.goto(scaledX,scaledY)
for angle in range(180):
    scaledX=0
    scaledY=-angle
    t.goto(scaledX,scaledY)

t.penup()
