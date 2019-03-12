from graphics import*
import random

def bulleye(ra,ran, pos,pos2, rad, color):#bullseyes function
    for ra in range(ran):
        circle(pos,pos2, ra, rad, color)
        color += 25

def circle(pos, pos2, ran, rad, color):#circle function
    c = Circle(Point(pos, pos2), rad-(20*(ran+1)))
    c.setFill(color_rgb(color,0,color))
    c.draw(wind)
    
#window size
winX = 800
#color for red and black
col = 0
swap = {0: 244, 244:0}
#create window
wind = GraphWin("checker", winX, winX)
wind.setCoords(0, 0, 800, 800)
i = 0
print("how many bullseyes")
hm = int(input())
for j in range(hm):
    bulleye(i,9, random.randint(0,800),random.randint(0,800), 200, col)
