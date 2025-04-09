import turtle

t = turtle.Turtle()
t.penup()
t.color("LawnGreen")
#This changes the background color
turtle.Screen().bgcolor("Black")
t.pendown()

#This selects the colors that will be displayed
colors = ["LawnGreen","Teal","Orange"]
#This shows how many times it will be repeated
for i in range(500):
    t.color( colors[i % 3] )
    t.speed(10 + 1)
    t.forward(100 + i)
    t.left(220)
    t.forward(100)
    t.right(20)

turtle.exitonclick()