# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
# TODO - create your player character
x1 = 0
y1 = -200
x2 = 0
y2 = 100
x3 = 0
y3 = -200
x4 = 0
y4 = 100
# TODO - set your background
set_background("castle")
s1 = create_sprite("wizard2",x1,y1)
s2 = create_sprite("witch2",x2,y2)
s3 = create_sprite("ball-lightning3",x3,y3)
# TODO - set the starting value for your variable
wizard_charge = 3
witch_charge = 3
wizard_lives = 3
witch_lives = 3
x1 = 0
y1 = -200
x2 = 0
y2 = 100
x3 = 0
y3 = -200
x4 = 0
y4 = 100


# Section 3: Controls
# TODO - define your controls
def move_up():
	global y1,  y3
	s1.setheading(90)
	s1.forward(10)
	s3.setheading(90)
	s3.hideturtle()
	y1 +=10
	y3 +=10
	
	

def move_up2():
	s2.setheading(90)
	s2.forward(10)
   	 
def move_down():
	global y1,  y3
	s1.setheading(270)
	s1.forward(10)
	s3.setheading(270)
	s3.hideturtle()
	y1 -=10
	y3 -=10
	

def move_down2():
	s2.setheading(270)
	s2.forward(10)
    
def move_left():
	global x1,  x3
	s1.setheading(180)
	s1.forward(10)
	s3.setheading(180)
	s3.hideturtle()
	x1 -=10
	x3 -=10
	
	
def move_left2():
	s2.setheading(180)
	s2.forward(10)
    
def move_right():    
	global x1,  x3
	s1.setheading(0)
	s1.forward(10)
	s3.setheading(0)
	s3.hideturtle()
	x1 +=10
	x3 +=10
	
	
def move_right2():    
	s2.setheading(0)
	s2.forward(10)
	
def wizard_spell():
	global x1, y1
	global x3, y3
	s3.showturtle()
	s3.forward(100)
	s3.goto
	


	

	



	
	
# TODO - pick keys for each control
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
window.onkeypress(wizard_spell, "e")

window.onkeypress(move_up2, "Up")
window.onkeypress(move_down2, "Down")
window.onkeypress(move_left2, "Left")
window.onkeypress(move_right2, "Right")

# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.1)
	timer += 1  
	 
    
 	# TODO - code for automatic actions
	if get_distance(s3,s2) < 20:
		witch_lives -=1

		
	






	window.update()

	# if :
	# 	break
	

print("Game Over")
