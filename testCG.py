from tkinter import *
import time
import random
import threading

root = Tk()

canvas_width = 800
canvas_height = 700
w = Canvas(root, width=canvas_width, height=canvas_height)
w.pack()

colors = ["red", "purple", "blue", "green", "gold", "pink", "light green", "grey", "tan", "yellow", "orange", "brown"]

A, B, C, D = [300, 300], [460, 300], [420, 360], [380, 100]

coordinates = [[A[0], A[1], 1], [B[0], B[1], 1], [C[0], C[1], 1], [D[0], D[1], 1]]

DBC = [D[0], D[1], B[0], B[1], C[0], C[1]]
ADC = [A[0], A[1], D[0], D[1], C[0], C[1]]

left = w.create_polygon(*ADC, fill="white", outline="black")
right = w.create_polygon(*DBC, fill="white", outline="black")


def MoveTread():
	global flag1
	flag1 = True
	while flag1:
		k = random.randrange(-20, 300)
		w.coords(left, A[0] + k, A[1] + k, D[0] + k, D[1] + k, C[0] + k, C[1] + k)
		w.coords(right, B[0] + k, B[1] + k, D[0] + k, D[1] + k, C[0] + k, C[1] + k)
		time.sleep(0.7)
		k = random.randrange(-20, 350)
		w.coords(left, A[0] + k, A[1] + k, D[0] + k, D[1] + k, C[0] + k, C[1] + k)
		w.coords(right, B[0] + k, B[1] + k, D[0] + k, D[1] + k, C[0] + k, C[1] + k)
		time.sleep(0.7)
		k = random.randrange(-20, 350)
		w.coords(left, A[0] + k, A[1] + k, D[0] + k, D[1] + k, C[0] + k, C[1] + k)
		w.coords(right, B[0] + k, B[1] + k, D[0] + k, D[1] + k, C[0] + k, C[1] + k)


def ChangeColourThread():
	global flag2
	flag2 = True
	while flag2:
		w.itemconfig(right, fill=random.choice(colors))
		w.itemconfig(left, fill=random.choice(colors))
		time.sleep(0.7)
		w.itemconfig(right, fill=random.choice(colors))
		w.itemconfig(left, fill=random.choice(colors))
		time.sleep(0.7)
		w.itemconfig(right, fill=random.choice(colors))
		w.itemconfig(left, fill=random.choice(colors))


def Move():
	k = random.randrange(-20, 350)
	w.coords(left, A[0] + k, A[1] + k, D[0] + k, D[1] + k, C[0] + k, C[1] + k)
	w.coords(right, B[0] + k, B[1] + k, D[0] + k, D[1] + k, C[0] + k, C[1] + k)


def ChangeColour():
	w.itemconfig(right, fill=random.choice(colors))
	w.itemconfig(left, fill=random.choice(colors))


def ChangeColorAndMove():
	global t1, t2
	t1 = threading.Thread(target=MoveTread)
	t2 = threading.Thread(target=ChangeColourThread)
	t1.start()
	t2.start()


def Stop():
	global flag1, flag2
	flag1 = False
	flag2 = False


def ZoomOut():
	for i in [A, B, C, D]:
		i[0] *= 0.95
		i[1] *= 0.95
	w.coords(left, A[0], A[1], D[0], D[1], C[0], C[1])
	w.coords(right, B[0], B[1], D[0], D[1], C[0], C[1])
	ChangeColour()


def ZoomIn():
	for i in [A, B, C, D]:
		i[0] *= 1.1
		i[1] *= 1.1
	w.coords(left, A[0], A[1], D[0], D[1], C[0], C[1])
	w.coords(right, B[0], B[1], D[0], D[1], C[0], C[1])
	ChangeColour()


buttonColor = Button(text="Change colour", width=20, font="Arial 12 bold", command=ChangeColour)
buttonColor.place(x=40, y=0)
buttonMove = Button(text="Move", width=20, font="Arial 12 bold", command=Move)
buttonMove.place(x=280, y=0)
buttonMoveAndColor = Button(text="Move And Change color", width=20, font="Arial 12 bold", command=ChangeColorAndMove)
buttonMoveAndColor.place(x=550, y=0)
buttonStop = Button(text="Stop moving & changing color at the same time", width=50, font="Arial 12 bold", command=Stop)
buttonStop.place(x=250, y=40)
buttonZoomIn = Button(text="Zoom in & change color", width=20, font="Arial 12 bold", command=ZoomIn)
buttonZoomIn.place(x=550, y=75)
buttonZoomOut = Button(text="Zoom out & change color", width=20, font="Arial 12 bold", command=ZoomOut)
buttonZoomOut.place(x=550, y=110)

mainloop()
