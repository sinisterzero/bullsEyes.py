from graphics import*
import random

def bulleye(ra,ran, pos,pos2, rad, red,green,blue):#bullseyes function
    for ra in range(ran):
        randnum = random.randint(1,3)
        circle(pos,pos2,rad/ran, ra, rad, red,green,blue)
        #random rgb
        if randnum == 1:
            red += 25
        elif randnum == 2:
            green += 25
        elif randnum == 3:
            blue += 25
        #rgb dont go over 255
        if red > 255:
            red -= 255
        if blue > 255:
            blue -= 255
        if green > 255:
            green -= 255
        
        

def circle(pos, pos2,spac, ran, rad, red,green,blue):#circle function
    c = Circle(Point(pos, pos2), rad-(spac*(ran+1)))
    c.setFill(color_rgb(red,green,blue))
    c.draw(wind)
check = False    
#window size
winX = 800
random.randint(0,800)
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
    bulleye(0,random.randint(10,25), random.randint(0,800),random.randint(0,800),random.randint(0,600), 0,0,0)
