from graphics import*
import random

def bulleye(ra,ran, pos,pos2,spac, rad, red,green,blue):#bullseyes function
    for ra in range(ran):
        randnum = random.randint(1,3)
        circle(pos,pos2,spac, ra, rad, red,green,blue)
        if randnum == 1:
            red += 20
        elif randnum == 2:
            green += 20
        elif randnum == 3:
            blue += 20
        

def circle(pos, pos2,spac, ran, rad, red,green,blue):#circle function
    c = Circle(Point(pos, pos2), rad-(spac*(ran+1)))
    c.setFill(color_rgb(red,green,blue))
    c.draw(wind)
check = False    
#window size
winX = 800
#color for red and black

swap = {0: 244, 244:0}
#create window
wind = GraphWin("checker", winX, winX)
wind.setCoords(0, 0, 800, 800)
while check == False:
    try:
        hm = int(input("how many bullseyes"))
        if 0 < hm :
            check = True
        else:
            print("please input a postive whole number")
    except ValueError:
        print("please input a number")
    
    
for j in range(hm):
    bulleye(0,10, random.randint(0,800),random.randint(0,800),random.randint(10,30), random.randint(150,300), 0,0,0)
