import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Python Turtle")
turtle.speed(0)
turtle_instance=turtle.Turtle()
turtle_colors=["green","red","orange","purple","yellow","pink"]

for i in range(15):
    turtle_instance.color(turtle_colors[i%6])
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)
    turtle_instance.left(i)

turtle.mainloop()
#turtle.done()
