from graphics import *

def base():
    base = Polygon(Point(175,525),Point(175,125),Point(575,125),Point(575,275),Point(700,275),Point(700,275),Point(925,275),Point(925,525))
    base.setFill(color_rgb(88,105,112))
    base.draw(win)

def windows(point1,point2):
    window = Rectangle(point1,point2)
    window.setFill(color_rgb(143,177,232))
    window.setWidth(3)
    window.draw(win)

def allwindows():
    windows(Point(225, 150), Point(275, 225))
    windows(Point(275, 150), Point(325, 225))
    windows(Point(425, 150), Point(475, 225))
    windows(Point(475, 150), Point(525, 225))
    windows(Point(725, 325), Point(775, 450))
    windows(Point(775, 325), Point(850, 450))
    windows(Point(850, 325), Point(900, 450))

def garage():
    garage = Rectangle(Point(250, 325), Point(525, 525))
    garage.setFill(color_rgb(215,219,226))
    garage.setWidth(2)
    garage.draw(win)

def door():
    door = Rectangle(Point(625,350),Point(675,475))
    door.setWidth(8)
    door.setOutline(color_rgb(114,68,53))
    door.setFill(color_rgb(193,11,11))
    door.draw(win)
    handle = Circle(Point(675, 400), 3)
    handle.setFill(color_rgb(0,0,0))
    handle.draw(win)

def chimney():
    chimney = Rectangle(Point(525,75),Point(550,125))
    chimney.setFill(color_rgb(114,68,53))
    chimney.draw(win)

def lights():
    light1 = Rectangle(Point(200,325),Point(225,375))
    light1.setFill(color_rgb(76,40,9))
    light1.setWidth(3)
    inner1 = Circle(Point(212, 355), 7)
    inner1.setFill(color_rgb(219, 219, 17))
    light2 = Rectangle(Point(550, 325), Point(575, 375))
    light2.setFill(color_rgb(76, 40, 9))
    light2.setWidth(3)
    inner2 = Circle(Point(562, 355), 7)
    inner2.setFill(color_rgb(219, 219, 17))
    light1.draw(win)
    inner1.draw(win)
    light2.draw(win)
    inner2.draw(win)

def roofs():
    roof1 = Polygon(Point(125,125),Point(375,25),Point(625,125))
    roof1.setFill(color_rgb(99,50,6))
    roof2 = Polygon(Point(650,300),Point(825,225),Point(975,300))
    roof2.setFill(color_rgb(99,50,6))
    roof3 = Polygon(Point(125,275), Point(450,175), Point(700,275))
    roof3.setFill(color_rgb(99,50,6))
    roof1.draw(win)
    roof2.draw(win)
    roof3.draw(win)

def finneseLines():
    line1 = Line(Point(600,275),Point(600,525))
    line2 = Line(Point(700,300), Point(700,525))
    line1.setWidth(3)
    line2.setWidth(3)
    line1.draw(win)
    line2.draw(win)
    line3 = Line(Point(260,325), Point(515,325))
    line4 = Line(Point(260, 350),Point(515,350))
    line5 = Line(Point(260,375), Point(515,375))
    line6 = Line(Point(260,400), Point(515,400))
    line7 = Line(Point(260,425), Point(515,425))
    line8 = Line(Point(260,450), Point(515,450))
    line9 = Line(Point(260,475), Point(515,475))
    line3.draw(win)
    line4.draw(win)
    line5.draw(win)
    line6.draw(win)
    line7.draw(win)
    line8.draw(win)
    line9.draw(win)

def driveway():
    driveway = Polygon(Point(75,649), Point(175,525), Point(525,525), Point(450,649))
    driveway.setFill(color_rgb(206,206,206))
    driveway.draw(win)

def lawn():
    lawnRight = Polygon(Point(450,649), Point(525,525),Point(925,525),Point(925,400), Point(999,400), Point(999,649))
    lawnLeft = Polygon(Point(175,525), Point(75,649), Point(0,649),Point(0,400), Point(175,400))
    lawnRight.setFill(color_rgb(30,109,25))
    lawnLeft.setFill(color_rgb(30,109,25))
    lawnRight.draw(win)
    lawnLeft.draw(win)

def moon():
    moon = Circle(Point(900,125), 50)
    moon.setFill(color_rgb(30,58,112))
    moon.draw(win)



# create your functions for each part of your house

def main():
    base()
    allwindows()
    garage()
    door()
    chimney()
    lights()
    roofs()
    finneseLines()
    driveway()
    lawn()
    moon()


    # put your function calls here for your drawing

    win.getMouse()  # wait for mouse click before closing
    win.close()


win = GraphWin("My House", 1000, 650)
win.setBackground("black")
main()
