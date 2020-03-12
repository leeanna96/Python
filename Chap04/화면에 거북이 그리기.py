import turtle

window=turtle.Screen()
window.bgcolor("lightgreen")

t=turtle.Turtle()
t.shape("turtle")
t.color("blue")

for i in range(30):
    t.stamp()
    t.forward(20+3*i)
    t.right(24)
