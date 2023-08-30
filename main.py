import turtle

drawing_board= turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")
#square
''' 
turtle_instance= turtle.Turtle()
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
'''
'''
turtle_instance= turtle.Turtle()
for x in range(4):
    turtle_instance.forward(200)
    turtle_instance.left(90)
'''
'''
#star
turtle_instance=turtle.Turtle()

for x in range(5):
    turtle_instance.left(144)
    turtle_instance.forward(100)
'''
#polygon(çokgen)

turtle_instance=turtle.Turtle()
num_sides=8
angle=360.0/num_sides
side_length=100


for x in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)


turtle.done()

