import turtle

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("Purple")
t.pendown()

for i in range(360):
    t.forward(1)
    t.left(1)
   


turtle.exitonclick()