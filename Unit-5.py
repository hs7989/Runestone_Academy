"""Write a program that prints We like Python's turtles! 100 times."""

for I in range(100):
    print("We like Python's turtles!")



"""Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):

An equilateral triangle

A square

A hexagon (six sides)

An octagon (eight sides)"""
import turtle

wn = turtle.Screen()
nora = turtle.Turtle()
for i in range(4):
    nora.forward(100)
    nora.left(90)


"""Write a program to draw a shape like this:

../_images/star.png"""
import turtle
wn = turtle.Screen()
turing = turtle.Turtle()
for i in range(5):
    turing.forward(100)
    turing.left(216)


"""Write a program to draw a face of a clock that looks something like this:"""
import turtle

nw = turtle.Screen()
nw.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
tess.penup()

james = turtle.Turtle()
james.color("blue")
james.shape("classic")
james.penup()

for i in range(12):
    james.forward(100)
    tess.forward(110)
    james.stamp()
    tess.stamp()
    james.forward(-100)
    tess.forward(-110)
    james.right(30)
    tess.right(30)


"""Write a program to draw some kind of picture. Be creative and experiment with the turtle methods."""
import turtle

tut = turtle.Turtle()
tut.hideturtle()
tut.speed(50)
dist=5
for i in range(250):
    tut.forward(dist)
    tut.right(95)
    dist = dist+1


"""Create a turtle and assign it to a variable. When you print its type, what do you get?"""
import turtle

tut = turtle.Turtle()
print(type(tut))