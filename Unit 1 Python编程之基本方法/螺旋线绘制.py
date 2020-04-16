import turtle
import time
turtle.speed(0.5)
turtle.pensize(2)
for x in range(100):
    turtle.forward(2*x)
    turtle.left(90)
time.sleep(3)
