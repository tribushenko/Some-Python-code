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
				 Circle(centerOfTheCircle, 55),  Circle(centerOfTheCircle, 40)]
counter = len(colors) - 1
for i in listOfCircles:
	i.setOutline(colors[counter])
	counter -= 1
	i.draw(win)

win.getMouse()

win.close()
