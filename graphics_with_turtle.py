# Turtle - it is a pre-installed python library that enables users to create picture and shapes by providing them wuth virtual canvas
import turtle

turtle.bgcolor('black')
turtle.pensize(5)
turtle.speed(0.2)
colours = ["green","red","blue",'yellow','violet','orange']
for i in range(20):
    for colour in colours:
        turtle.color(colour)
        turtle.circle(120)
        turtle.left(15)


turtle.mainloop()