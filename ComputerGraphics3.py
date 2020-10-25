from tkinter import *
import time
import random
import threading

root = Tk()

canvas_width = 800
canvas_height = 700
w = Canvas(root, width=canvas_width, height=canvas_height)
w.pack()

A, B, C, D = [100, 100], [280, 100], [140, 140], [320, 140]
A1, B1, C1, D1 = [100, 240], [280, 240], [140, 280], [320, 280]
colors = ["red", "purple", "blue", "green", "gold", "pink", "light green", "grey", "tan", "yellow", "orange", "brown"]

upCoord = [A[0], A[1], B[0], B[1], C[0], C[1], D[0], D[1]]
leftCoord = [A[0], A[1], C[0], C[1], A1[0], A1[1], C1[0], C1[1]]
frontCoord = [C[0], C[1], C1[0], C1[1], D[0], D[1], D1[0], D1[1]]
downCoord = [A1[0], A1[1], B1[0], B1[1], D1[0], D1[1], C1[0], C1[1]]
rightCoord = [B[0], B[1], D[0], D[1], D1[0], D1[1], B1[0], B1[1]]
rearCoord = [A[0], A[1], B[0], B[1], B1[0], B1[1], A1[0], A1[1]]

up = w.create_polygon(*upCoord, fill="white", outline="black")
left = w.create_polygon(*leftCoord, fill="white", outline="black")
front = w.create_polygon(*frontCoord, fill="white", outline="black")
down = w.create_polygon(*downCoord, fill="white", outline="black")
right = w.create_polygon(*rightCoord, fill="white", outline="black")
rear = w.create_polygon(*rearCoord, fill="white", outline="black")


def MoveTread():
	global flag1
	flag1 = True
	while flag1:
		k = random.randrange(-20, 350)
		w.coords(up, A[0] + k, A[1] + k, B[0] + k, B[1] + k, C[0] + k, C[1] + k, D[0] + k, D[1] + k)
		w.coords(left, A[0] + k, A[1] + k, C[0] + k, C[1] + k, A1[0] + k, A1[1] + k, C1[0] + k, C1[1] + k)
		w.coords(front, C[0] + k, C[1] + k, C1[0] + k, C1[1] + k, D[0] + k, D[1] + k, D1[0] + k, D1[1] + k)
		w.coords(down, A1[0] + k, A1[1] + k, B1[0] + k, B1[1] + k, D1[0] + k, D1[1] + k, C1[0] + k, C1[1] + k)
		w.coords(right, B[0] + k, B[1] + k, D[0] + k, D[1] + k, D1[0] + k, D1[1] + k, B1[0] + k, B1[1] + k)
		w.coords(rear, A[0] + k, A[1] + k, B[0] + k, B[1] + k, B1[0] + k, B1[1] + k, A1[0] + k, A1[1] + k)
		time.sleep(0.7)
		k = random.randrange(-20, 350)
		w.coords(up, A[0] + k, A[1] + k, B[0] + k, B[1] + k, C[0] + k, C[1] + k, D[0] + k, D[1] + k)
		w.coords(left, A[0] + k, A[1] + k, C[0] + k, C[1] + k, A1[0] + k, A1[1] + k, C1[0] + k, C1[1] + k)
		w.coords(front, C[0] + k, C[1] + k, C1[0] + k, C1[1] + k, D[0] + k, D[1] + k, D1[0] + k, D1[1] + k)
		w.coords(down, A1[0] + k, A1[1] + k, B1[0] + k, B1[1] + k, D1[0] + k, D1[1] + k, C1[0] + k, C1[1] + k)
		w.coords(right, B[0] + k, B[1] + k, D[0] + k, D[1] + k, D1[0] + k, D1[1] + k, B1[0] + k, B1[1] + k)
		w.coords(rear, A[0] + k, A[1] + k, B[0] + k, B[1] + k, B1[0] + k, B1[1] + k, A1[0] + k, A1[1] + k)
		time.sleep(0.7)
		k = random.randrange(-20, 350)
		w.coords(up, A[0] + k, A[1] + k, B[0] + k, B[1] + k, C[0] + k, C[1] + k, D[0] + k, D[1] + k)
		w.coords(left, A[0] + k, A[1] + k, C[0] + k, C[1] + k, A1[0] + k, A1[1] + k, C1[0] + k, C1[1] + k)
		w.coords(front, C[0] + k, C[1] + k, C1[0] + k, C1[1] + k, D[0] + k, D[1] + k, D1[0] + k, D1[1] + k)
		w.coords(down, A1[0] + k, A1[1] + k, B1[0] + k, B1[1] + k, D1[0] + k, D1[1] + k, C1[0] + k, C1[1] + k)
		w.coords(right, B[0] + k, B[1] + k, D[0] + k, D[1] + k, D1[0] + k, D1[1] + k, B1[0] + k, B1[1] + k)
		w.coords(rear, A[0] + k, A[1] + k, B[0] + k, B[1] + k, B1[0] + k, B1[1] + k, A1[0] + k, A1[1] + k)


def ChangeColourThread():
	global flag2
	flag2 = True
	while flag2:
		w.itemconfig(right, fill=random.choice(colors))
		w.itemconfig(rear, fill=random.choice(colors))
		w.itemconfig(down, fill=random.choice(colors))
		time.sleep(0.7)
		w.itemconfig(right, fill=random.choice(colors))
		w.itemconfig(rear, fill=random.choice(colors))
		w.itemconfig(down, fill=random.choice(colors))
		time.sleep(0.7)
		w.itemconfig(right, fill=random.choice(colors))
		w.itemconfig(rear, fill=random.choice(colors))
		w.itemconfig(down, fill=random.choice(colors))


def Move():
	k = random.randrange(-20, 350)
	w.coords(up, A[0] + k, A[1] + k, B[0] + k, B[1] + k, C[0] + k, C[1] + k, D[0] + k, D[1] + k)
	w.coords(left, A[0] + k, A[1] + k, C[0] + k, C[1] + k, A1[0] + k, A1[1] + k, C1[0] + k, C1[1] + k)
	w.coords(front, C[0] + k, C[1] + k, C1[0] + k, C1[1] + k, D[0] + k, D[1] + k, D1[0] + k, D1[1] + k)
	w.coords(down, A1[0] + k, A1[1] + k, B1[0] + k, B1[1] + k, D1[0] + k, D1[1] + k, C1[0] + k, C1[1] + k)
	w.coords(right, B[0] + k, B[1] + k, D[0] + k, D[1] + k, D1[0] + k, D1[1] + k, B1[0] + k, B1[1] + k)
	w.coords(rear, A[0] + k, A[1] + k, B[0] + k, B[1] + k, B1[0] + k, B1[1] + k, A1[0] + k, A1[1] + k)


def ChangeColour():
	w.itemconfig(right, fill=random.choice(colors))
	w.itemconfig(rear, fill=random.choice(colors))
	w.itemconfig(down, fill=random.choice(colors))


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


buttonColor = Button(text="Change colour", width=20, font="Arial 12 bold", command=ChangeColour)
buttonColor.place(x=40, y=0)
buttonMove = Button(text="Move", width=20, font="Arial 12 bold", command=Move)
buttonMove.place(x=280, y=0)
buttonMoveAndColor = Button(text="Move And Change color", width=20, font="Arial 12 bold", command=ChangeColorAndMove)
buttonMoveAndColor.place(x=550, y=0)
buttonStop = Button(text="Stop moving and changing color at the same time", width=50, font="Arial 12 bold",command=Stop)
buttonStop.place(x=250, y=40)


mainloop()
