# Beginning:
smrt_points = 0
dum_points = 0


# Middle:
answer = input("how many colors of the alphabet does it take to taste math? A) the sahara ocean B) thermonuclear orange juice-infused corncobs")
if answer.lower() == "a":
    dum_points +=1
elif answer.lower() == "b":
    smrt_points +=1


answer = input("what is a microwave? A) true B) do not the fish")
if answer.lower() == "a":
    dum_points +=1
elif answer.lower() == "b":
    smrt_points +=1


answer = input("if you're going down a hill in a submarine with all the screen doors open, how many pancakes does it take to shingle a doghouse? A) two and a half chocolate cows B) yes")
if answer.lower() == "a":
    smrt_points +=1
elif answer.lower() == "b":
    dum_points +=1


answer = input("i stole one of your socks A) the DISTURBING truth behind the wood industry B) closed captions")
if answer.lower() == "a":
    dum_points +=1
elif answer.lower() == "b":
    smrt_points +=1


answer = input("yesn't the elevator open with closed belly button A) 37 billion beans B) stop doing the bad")
if answer.lower() == "a":
    smrt_points +=1
elif answer.lower() == "b":
    dum_points +=1


answer = input("there are two very fast unicycles that aren't fast heading away from you, what do you eat in Canadia? A) skatebord B) threnty fiven")
if answer.lower() == "a":
    dum_points +=1
elif answer.lower() == "b":
    smrt_points +=1



answer = input("there is tow truck on your alarm block, so when do you eat the water? A) the color of 237.098 B) scary bowl!! ")
if answer.lower() == "a":
    dum_points +=1
elif answer.lower() == "b":
    smrt_points +=1


answer = input("youy're sliding up a hole and then the clouds pour grass on the sun. what do you have in your seventh briefcase? A) two dirts B) pelicans")
if answer.lower() == "a":
    smrt_points +=1
elif answer.lower() == "b":
    dum_points +=1



answer = input("theres a flying meatball and then suddenly the pen sharpener creates a bunch of oldspapers! who do you book an appointment with for Junuember 64st, eleventy nine? A) ghonstbubsters B) the sound of spaghetti")
if answer.lower() == "a":
    smrt_points +=1
elif answer.lower() == "b":
    dum_points +=1

#End:
if smrt_points > dum_points:
    print("you're pretty bright! sometimes life is like a pretzel container-it smells like seven")
elif dum_points > smrt_points:
    print("youre not the brightest fish wheel in the elevator. evaporate your chickens next time?")