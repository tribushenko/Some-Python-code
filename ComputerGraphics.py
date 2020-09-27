from graphics import *
import pylab
import numpy as np
import math
import turtle



colors = ["red", "purple", "blue", "green", "gold"]
# first 4 lines are outter triangle, second 4 - inner
for t in range(2):
    command = input("Write down the name of the library(turtle, graphics) you want to use: ")
    if command == "graphics":
        win = GraphWin("title", 1500, 1500)
        listOfLinesTriangle = [Line(Point(450, 200), Point(50, 200)), Line(Point(50, 200), Point(250, 50)),
                               Line(Point(250, 50), Point(450, 200)), Line(Point(400, 180), Point(100, 180)),
                               Line(Point(100, 180), Point(250, 70)), Line(Point(250, 70), Point(400, 180)),
                               Line(Point(350, 160), Point(150, 160)), Line(Point(150, 160), Point(250, 90)),
                               Line(Point(250, 90), Point(350, 160)), Line(Point(300, 140), Point(200, 140)),
                               Line(Point(200, 140), Point(250, 110)), Line(Point(250, 110), Point(300, 140))]
        counter = 0
        for i in listOfLinesTriangle:
            if listOfLinesTriangle.index(i) % 3 == 0:
                counter += 1
            i.setOutline(colors[counter - 1])
            i.draw(win)
        centerOfTheCircle = Point(600, 110)
        listOfCircles = [Circle(centerOfTheCircle, 100), Circle(centerOfTheCircle, 85), Circle(centerOfTheCircle, 70),
                         Circle(centerOfTheCircle, 55), Circle(centerOfTheCircle, 40)]
        counter = 0
        for i in listOfCircles:
            i.setOutline(colors[counter])
            counter += 1
            i.draw(win)
        try:
            win.getMouse()
        except GraphicsError:
            pass
        win.close()
    elif command == "turtle":
        # declaring window, turtle and setting it at the certain place
        window = turtle.Screen()
        turtle.shape("turtle")
        turtle.penup()
        turtle.goto(-300, 100)
        turtle.pendown()
        index = 0
        turtle.color(colors[index])
        index += 1
        # first triangle
        turtle.forward(255)
        turtle.left(130)
        turtle.forward(200)
        turtle.left(100)
        turtle.forward(200)
        turtle.penup()
        turtle.goto(-270, 115)
        turtle.pendown()
        turtle.left(130)
        turtle.color(colors[index])
        index += 1
        # second triangle
        turtle.forward(190)
        turtle.left(130)
        turtle.forward(150)
        turtle.left(101)
        turtle.forward(150)
        turtle.penup()
        turtle.goto(-240, 130)
        turtle.pendown()
        turtle.left(129)
        turtle.color(colors[index])
        index += 1
        # third triangle
        turtle.forward(130)
        turtle.left(130)
        turtle.forward(100)
        turtle.left(100)
        turtle.forward(100)
        turtle.penup()
        turtle.goto(-210, 145)
        turtle.pendown()
        turtle.left(130)
        turtle.color(colors[index])
        index += 1
        # fourth triangle
        turtle.forward(75)
        turtle.left(130)
        turtle.forward(60)
        turtle.left(100)
        turtle.forward(62)
        turtle.penup()
        # heading to drawing circles
        turtle.goto(150, 100)
        turtle.pendown()
        turtle.left(130)
        index = 0
        # first circle
        turtle.color(colors[index])
        index += 1
        turtle.circle(100)
        # second circle
        turtle.penup()
        turtle.goto(150, 115)
        turtle.pendown()
        turtle.color(colors[index])
        index += 1
        turtle.circle(85)
        # third circle
        turtle.penup()
        turtle.goto(150, 130)
        turtle.pendown()
        turtle.color(colors[index])
        index += 1
        turtle.circle(70)
        # fourth circle
        turtle.penup()
        turtle.goto(150, 145)
        turtle.pendown()
        turtle.color(colors[index])
        index += 1
        turtle.circle(55)
        # fifth circle
        turtle.penup()
        turtle.goto(150, 160)
        turtle.pendown()
        turtle.color(colors[index])
        index += 1
        turtle.circle(40)
        # to the starting point
        turtle.color("black")
        turtle.penup()
        turtle.goto(0, 0)
        break
    else:
        print("Invalid argument")

win = GraphWin("title", 1500, 1500)
listOfPolygons = [Polygon(Point(300, 420), Point(360, 360), Point(420, 420), Point(360, 480)),
                  Polygon(Point(420, 400), Point(360, 460), Point(420, 520), Point(480, 460)),
                  Polygon(Point(420, 320), Point(360, 380), Point(420, 440), Point(480, 380)),
                  Polygon(Point(410, 420), Point(470, 480), Point(530, 420), Point(470, 360))]
counter = 0
for i in listOfPolygons:
    i.setFill(colors[counter])
    counter += 1
    i.draw(win)
ListOfLinesPolygons = [Line(Point(600, 420), Point(660, 360)), Line(Point(660, 360), Point(720, 420)),
                       Line(Point(720, 420), Point(660, 480)), Line(Point(660, 480), Point(600, 420)),
                       Line(Point(720, 320), Point(780, 380)), Line(Point(780, 380), Point(720, 440)),
                       Line(Point(720, 440), Point(660, 380)), Line(Point(660, 380), Point(720, 320)),
                       Line(Point(720, 400), Point(780, 460)), Line(Point(780, 460), Point(720, 520)),
                       Line(Point(720, 520), Point(660, 460)), Line(Point(660, 460), Point(720, 400)),
                       Line(Point(710, 420), Point(770, 360)), Line(Point(770, 360), Point(830, 420)),
                       Line(Point(830, 420), Point(770, 480)), Line(Point(770, 480), Point(710, 420))]
length = len(colors) - 1
for i in ListOfLinesPolygons:
    if ListOfLinesPolygons.index(i) % 4 == 0:
        length -= 1
    i.setOutline(colors[length])
    i.draw(win)
try:
    win.getMouse()
except GraphicsError:
    pass
win.close()

def sinx(x):
    return 0.81 * math.sin(x)

def cosx(x):
    return 0.81 * math.cos(x)

def tgx(x):
    return 0.81 * math.tan(x)
xmin = -20
xmax = 20
xlist = np.arange(-20, 20, 0.01)

ylistsin = [sinx(x) for x in xlist]
ylistcos = [cosx(x) for x in xlist]
ylisttan = [tgx(x) for x in xlist]

pylab.figure(1)
pylab.plot(xlist, ylistsin, label="f(x) = (3 * 27 * 0.01)*sin(x)")
pylab.legend()

pylab.figure(2)
pylab.plot(xlist, ylistcos, label="g(x) = (3 * 27 * 0.01)*cos(x)")
pylab.legend()

pylab.figure(3)
pylab.plot(xlist, ylisttan, label="t(x) = (3 * 27 * 0.01)tan(x)")
pylab.legend()

pylab.figure(4)
pylab.plot(xlist, ylistsin, label="f(x) = (3 * 27 * 0.01)*sin(x)")
pylab.plot(xlist, ylistcos, label="g(x) = (3 * 27 * 0.01)*cos(x)")
pylab.plot(xlist, ylisttan, label="t(x) = (3 * 27 * 0.01)tan(x)")
pylab.legend()

pylab.show()


