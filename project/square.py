import turtle
import Tkinter

def draw_art(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art1(some_turtle):
	for i in range(1,4):
		some_turtle.forward(300)
		some_turtle.right(120)

def draw_square():
	window=turtle.Screen()
	window.bgcolor("red")

	brad=turtle.Turtle()
	brad.shape("triangle")
	brad.color("yellow","green")
	brad.speed(2)
	
	for i in range(1,37):
		draw_art(brad)
		brad.left(10)

	window.exitonclick()

def draw_circle():
	window=turtle.Screen()
	window.bgcolor("green")

	sam=turtle.Turtle()
	sam.shape("classic")
        sam.color("white","blue")

        sam.circle(50)

	window.exitonclick()


def draw_triangle():
	window=turtle.Screen()
	window.bgcolor("pink")

	angie=turtle.Turtle()
	angie.shape("arrow")
	angie.color("yellow","red")

	draw_art1(angie)

	window.exitonclick()

	
print draw_square()
print draw_circle()
print draw_triangle()
