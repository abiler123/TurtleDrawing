import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Python Turtle")

turtle_instance=turtle.Turtle()
turtle_instance.color("blue")

def shrikingsquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size=size-5
shrikingsquare(150)
shrikingsquare(130)
shrikingsquare(110)
shrikingsquare(90)
shrikingsquare(70)
shrikingsquare(50)
shrikingsquare(30)
shrikingsquare(10)

turtle.done()