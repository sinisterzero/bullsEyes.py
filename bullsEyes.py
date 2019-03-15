from graphics import*
import random

def bulleye(ra,ran, pos,pos2, rad, red,green,blue):#bullseyes function
    for ra in range(ran):
        randnum = random.randint(1,3)
        circle(pos,pos2,rad/10, ra, rad, red,green,blue)
        #random rgb 
        if randnum == 1:
            red += 25
        elif randnum == 2:
            green += 25
        elif randnum == 3:
            blue += 25
        

def circle(pos, pos2,spac, ran, rad, red,green,blue):#circle function
    c = Circle(Point(pos, pos2), rad-(spac*(ran+1)))
    c.setFill(color_rgb(red,green,blue))
    c.draw(wind)
check = False    
#window size
winX = 800
radi = random.randint(0,800)
#create window
wind = GraphWin("checker", winX, winX)
wind.setCoords(0, 0, 800, 800)
#user input/protection from bad input
while check == False:
    try:
        hm = int(input("how many bullseyes"))
        if 0 < hm :
            check = True
        else:
            print("please input a postive whole number")
    except ValueError:
        print("please input a number")
    
#spawn bullseyes    
for j in range(hm):
    bulleye(0,10, random.randint(0,800),radi, random.randint(150,300), 0,0,0)
