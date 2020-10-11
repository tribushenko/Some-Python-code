from tkinter import *
import numpy as np

root = Tk()
canvas = Canvas(root, width=1000, height=1000, bg="white")
coordinatesWithProportions = [[200, 200, 1], [300, 100, 1], [400, 200, 1], [350, 300, 1], [250, 300, 1]]


def buttonDraw():
	canvas.create_polygon(draw(coordinatesWithProportions), fill='', outline="black")

def buttonZoom():
	canvas.create_polygon(draw(zoom(coordinatesWithProportions, int(entry.get()))), fill='', outline="black")

def buttonMoveDraw():
	for i in range(3, 7):
		mass2 = draw(move(coordinatesWithProportions, 50 + i * 10, 0))
		canvas.create_polygon(mass2, fill='', outline="black")
	for i in range(3, 7):
		mass2 = draw(move(coordinatesWithProportions, 0, 50 + i * 10))
		canvas.create_polygon(mass2, fill='', outline="black")
	for i in range(3, 7):
		mass2 = draw(move(coordinatesWithProportions, 0 - i * 16.65, 0))
		canvas.create_polygon(mass2, fill='', outline="black")
	for i in range(3, 7):
		mass2 = draw(move(coordinatesWithProportions, 0, 0 - i * 21))
		canvas.create_polygon(mass2, fill='', outline="black")


def draw(coordinatesWithProportions):
	new_arr = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
	for i in range(5):
		for j in range(2):
			new_arr[i][j] = coordinatesWithProportions[i][j] / coordinatesWithProportions[i][2]
	return new_arr


def move(x, x1, y):
	global coordinatesWithProportions
	list3 = []
	list2 = np.array([[1, 0, 0], [0, 1, 0], [x1, y, 1]])
	for i in range(5):
		list1 = np.array(x[i])
		list3.append(list(list1.dot(list2)))
	coordinatesWithProportions = list3
	return list3


def zoom(x, factor):
	global coordinatesWithProportions
	list3 = []
	list2 = np.array([[factor, 0, 0], [0, factor, 0], [0, 0, 1]])
	for i in range(5):
		list1 = np.array(x[i])
		list3.append(list(list1.dot(list2)))
	coordinatesWithProportions = list3
	print(coordinatesWithProportions)
	return list3


Button(root, command=buttonDraw, font="Ariel 14", text="Draw a pentagon", width=15).place(x=20, y=20)
Button(root, command=buttonMoveDraw, font="Ariel 14", text="Move and Draw", width=15).place(x=20, y=80)
Button(root, command=buttonZoom, font="Ariel 14", text="Zoom in x times", width=15).place(x=20, y=140)
entry = Entry(root, width=29, bg="pink")
entry.place(x=23, y=180, height=29)
Label(root, text="x=", font="Ariel 14").place(x=0, y=180)
canvas.create_polygon(draw(zoom(coordinatesWithProportions, 1.5)), fill='', outline="black")
canvas.pack()
root.mainloop()
