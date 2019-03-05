from graphics import*

def circle(pos, rad, color):
    c = Circle(Point(pos, pos), rad-(20*(i+1)))
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
for i in range(9):
    circle(winX/2, 200, red)
    red = swap[red]
