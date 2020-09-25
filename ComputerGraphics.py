from graphics import *


win = GraphWin("title", 1500, 1500)

# first 4 lines are outter triangle, second 4 - inner
listOfLinesTriangle = [Line(Point(450, 200), Point(50, 200)), Line(Point(50, 200), Point(250, 50)), Line(Point(250, 50),
	Point(450, 200)), Line(Point(400, 180), Point(100, 180)), Line(Point(100, 180), Point(250, 70)), Line(Point(250, 70),
	Point(400, 180)), Line(Point(350, 160), Point(150, 160)), Line(Point(150, 160), Point(250, 90)), Line(Point(250, 90),
	Point(350, 160)), Line(Point(300, 140), Point(200, 140)), Line(Point(200, 140), Point(250, 110)), Line(Point(250, 110),
	Point(300, 140))]

colors = ["red", "purple", "blue", "green", "gold"]
counter = 0
for i in listOfLinesTriangle:
	if listOfLinesTriangle.index(i) % 3 == 0:
		counter += 1
	i.setOutline(colors[counter - 1])
	i.draw(win)

centerOfTheCircle = Point(600, 110)
listOfCircles = [Circle(centerOfTheCircle, 100), Circle(centerOfTheCircle, 85), Circle(centerOfTheCircle, 70),
                 Circle(centerOfTheCircle, 55), Circle(centerOfTheCircle, 40)]
counter = len(colors) - 1
for i in listOfCircles:
	i.setOutline(colors[counter])
	counter -= 1
	i.draw(win)

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


win.getMouse()
win.close()
