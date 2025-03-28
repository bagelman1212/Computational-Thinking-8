###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("winter")

q1 = codesters.Square(100, 100, 200, 'DarkGreen')
q2 = codesters.Square(-100, 100, 200, 'DarkSlateGray')
q3 = codesters.Square(-100, -100, 200, 'ForestGreen')
q4 = codesters.Square(100, -100, 200, 'LightSlateGray')

s1 = codesters.Sprite("supramk45", 100, 100)
s1.set_size(0.33)
s2 = codesters.Sprite("justacat", -100, 100)
s2.set_size(0.33)
s3 = codesters.Sprite("sushi1", -100, -100)
s3.set_size(0.30)
s4 = codesters.Sprite("videogame1", 100, -100)
s4.set_size(0.22)

message1 = codesters.Text("Brian Sanford",0,220,"Green")
message2 = codesters.Text("my cat only lives for food",0,-220,"Green")
