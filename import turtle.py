import turtle
my_turtle = turtle.Turtle()
my_turtle.color('purple')
my_turtle.penup()
my_turtle.goto(0, 0)
my_turtle.pendown()
for i in range(5):
    my_turtle.forward(100)
    my_turtle.left(72)
turtle.done()