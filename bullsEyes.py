from graphics import*


def bulleye(ra,ran, pos, rad, color):
    for ra in range(ran):
        circle(pos, ra, rad, color)
        color = swap[color]

def circle(pos, ran, rad, color):
    c = Circle(Point(pos, pos), rad-(20*(ran+1)))
    c.setFill(color_rgb(color,0,0))
    c.draw(wind)
    
#window size
winX = 800
#color for red and black
red = 244
swap = {0: 244, 244:0}
#create window
wind = GraphWin("checker", winX, winX)
wind.setCoords(0, 0, 800, 800)
i = 0
bulleye(i,9, winX/2, 200, red)
