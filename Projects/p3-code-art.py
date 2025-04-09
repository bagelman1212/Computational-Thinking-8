import turtle

t = turtle.Turtle()
t.penup()
t.color("LawnGreen")
turtle.Screen().bgcolor("Black")
t.pendown()

colors = ["LawnGreen","Teal","Orange"]
for i in range(500):
    t.color( colors[i % 3] )
    t.speed(10 + 1)
    t.forward(100 + i)
    t.left(276)
    t.forward(100)
    t.right(76)

turtle.exitonclick()