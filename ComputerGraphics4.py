from tkinter import *
import time
import random
import threading


root = Tk()

colors = ["red", "purple", "blue", "green", "gold", "pink", "light green", "grey", "tan", "yellow", "orange", "brown"]
canvas_width = 800
canvas_height = 700
c = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
c.pack()

A, B, C, D = [100, 100], [280, 100], [140, 140], [320, 140]
A1, B1, C1, D1 = [100, 240], [280, 240], [140, 280], [320, 280]

upCoord = [A[0], A[1], B[0], B[1], C[0], C[1], D[0], D[1]]
leftCoord = [A[0], A[1], C[0], C[1], A1[0], A1[1], C1[0], C1[1]]
frontCoord = [C[0], C[1], C1[0], C1[1], D[0], D[1], D1[0], D1[1]]
downCoord = [A1[0], A1[1], B1[0], B1[1], D1[0], D1[1], C1[0], C1[1]]
rightCoord = [B[0], B[1], D[0], D[1], D1[0], D1[1], B1[0], B1[1]]
rearCoord = [A[0], A[1], B[0], B[1], B1[0], B1[1], A1[0], A1[1]]

pixels = [[100, 140, 100, 140], [100, 280, 100, 100], [280, 320, 100, 140], [140, 320, 140, 140],
          [100, 100, 100, 240], [140, 140, 140, 280], [280, 280, 100, 240], [320, 320, 140, 280],
          [100, 140, 240, 280], [100, 280, 240, 240], [280, 320, 240, 280], [140, 320, 280, 280]]

listOfPixels = []


def paral():
	StopBlinking()

	# drawing a line
	def raster(x0, x1, y0, y1):
		dx = abs(x1 - x0)
		dy = abs(y1 - y0)
		x, y = x0, y0
		sx = -1 if x0 > x1 else 1
		sy = -1 if y0 > y1 else 1
		if dx > dy:
			err = dx / 2
			while x!=x1:
				listOfPixels.append(c.create_rectangle(x, y, x + 1, y + 1))
				err -= dy
				if err < 0:
					y += sy
					err += dx
				x += sx
		else:
			err = dy / 2
			while y!=y1:
				listOfPixels.append(c.create_rectangle(x, y, x + 1, y + 1))
				err -= dx
				if err < 0:
					x += sx
					err += dy
				y += sy
		listOfPixels.append(c.create_rectangle(x, y, x + 1, y + 1))

	for i in pixels:
		raster(*i)


def paralChangeColor():
	pixelsChangeColor = [[100, 140, 100, 140], [100, 280, 100, 100], [280, 320, 100, 140], [140, 320, 140, 140],
	                     [100, 100, 100, 240], [140, 140, 140, 280], [320, 320, 140, 280],
	                     [100, 140, 240, 280], [140, 320, 280, 280]]

	def raster(x0, x1, y0, y1):
		dx = abs(x1 - x0)
		dy = abs(y1 - y0)
		x, y = x0, y0
		sx = -1 if x0 > x1 else 1
		sy = -1 if y0 > y1 else 1
		if dx > dy:
			err = dx / 2
			while x!=x1:
				listOfPixels.append(c.create_rectangle(x, y, x + 1, y + 1))
				err -= dy
				if err < 0:
					y += sy
					err += dx
				x += sx
		else:
			err = dy / 2
			while y!=y1:
				listOfPixels.append(c.create_rectangle(x, y, x + 1, y + 1))
				err -= dx
				if err < 0:
					x += sx
					err += dy
				y += sy
		listOfPixels.append(c.create_rectangle(x, y, x + 1, y + 1))

	for i in pixelsChangeColor:
		raster(*i)


def appearAndSlake():
	StopChangingColor()
	up = c.create_polygon(*upCoord, fill="white", outline="white")
	left = c.create_polygon(*leftCoord, fill="white", outline="white")
	front = c.create_polygon(*frontCoord, fill="white", outline="white")
	down = c.create_polygon(*downCoord, fill="white", outline="white")
	right = c.create_polygon(*rightCoord, fill="white", outline="white")
	rear = c.create_polygon(*rearCoord, fill="white", outline="white")

	def white_line(x0, x1, y0, y1):
		# drawing a line
		dx = abs(x1 - x0)
		dy = abs(y1 - y0)
		x, y = x0, y0
		sx = -1 if x0 > x1 else 1
		sy = -1 if y0 > y1 else 1
		if dx > dy:
			err = dx / 2
			while x!=x1:
				listOfPixels.append(c.create_rectangle(x, y, x + 1, y + 1, fill='white', outline='white'))
				err -= dy
				if err < 0:
					y += sy
					err += dx
				x += sx
		else:
			err = dy / 2
			while y!=y1:
				listOfPixels.append(c.create_rectangle(x, y, x + 1, y + 1, fill='white', outline='white'))
				err -= dx
				if err < 0:
					x += sx
					err += dy
				y += sy
		listOfPixels.append(c.create_rectangle(x, y, x + 1, y + 1, fill='white', outline='white'))

	def black_line(x0, x1, y0, y1):
		# drawing a line
		dx = abs(x1 - x0)
		dy = abs(y1 - y0)
		x, y = x0, y0
		sx = -1 if x0 > x1 else 1
		sy = -1 if y0 > y1 else 1
		if dx > dy:
			err = dx / 2
			while x!=x1:
				listOfPixels.append(c.create_rectangle(x, y, x + 1, y + 1))
				err -= dy
				if err < 0:
					y += sy
					err += dx
				x += sx
		else:
			err = dy / 2
			while y!=y1:
				listOfPixels.append(c.create_rectangle(x, y, x + 1, y + 1))
				err -= dx
				if err < 0:
					x += sx
					err += dy
				y += sy
		listOfPixels.append(c.create_rectangle(x, y, x + 1, y + 1))

	global flag
	flag = True
	while flag:
		for pixel in pixels:
			white_line(*pixel)
		listOfPixels.clear()
		time.sleep(0.3)
		for pixel in pixels:
			black_line(*pixel)
		time.sleep(0.3)
		listOfPixels.clear()


def StopBlinking():
	global flag
	flag = False


def StartBlinking():
	t1 = threading.Thread(target=appearAndSlake)
	t1.start()


def ChangeColor():
	global flagColor
	flagColor = True
	rand = random.choice(colors)
	up = c.create_polygon(*upCoord, fill=rand, outline=rand)
	up1 = c.create_polygon(210, 120, 100, 100, 140, 140, fill=rand, outline=rand)
	up2 = c.create_polygon(210, 120, 280, 100, 320, 140, fill=rand, outline=rand)
	rand = random.choice(colors)
	left = c.create_polygon(*leftCoord, fill=rand, outline=rand)
	left1 = c.create_polygon(120, 190, 100, 100, 100, 240, fill=rand, outline=rand)
	left2 = c.create_polygon(120, 190, 140, 140, 140, 280, fill=rand, outline=rand)
	rand = random.choice(colors)
	front = c.create_polygon(*frontCoord, fill=rand, outline=rand)
	front1 = c.create_polygon(230, 210, 140, 140, 320, 140, fill=rand, outline=rand)
	front2 = c.create_polygon(230, 210, 140, 280, 320, 280, fill=rand, outline=rand)
	while flagColor:
		paralChangeColor()
		rand = random.choice(colors)
		c.itemconfig(front, fill=rand, outline=rand)
		c.itemconfig(front1, fill=rand, outline=rand)
		c.itemconfig(front2, fill=rand, outline=rand)
		rand = random.choice(colors)
		c.itemconfig(left, fill=rand, outline=rand)
		c.itemconfig(left1, fill=rand, outline=rand)
		c.itemconfig(left2, fill=rand, outline=rand)
		rand = random.choice(colors)
		c.itemconfig(up, fill=rand, outline=rand)
		c.itemconfig(up1, fill=rand, outline=rand)
		c.itemconfig(up2, fill=rand, outline=rand)
		time.sleep(0.2)
		rand = random.choice(colors)
		c.itemconfig(front, fill=rand, outline=rand)
		c.itemconfig(front1, fill=rand, outline=rand)
		c.itemconfig(front2, fill=rand, outline=rand)
		rand = random.choice(colors)
		c.itemconfig(left, fill=rand, outline=rand)
		c.itemconfig(left1, fill=rand, outline=rand)
		c.itemconfig(left2, fill=rand, outline=rand)
		rand = random.choice(colors)
		c.itemconfig(up, fill=rand, outline=rand)
		c.itemconfig(up1, fill=rand, outline=rand)
		c.itemconfig(up2, fill=rand, outline=rand)
		time.sleep(0.2)
		paralChangeColor()
		rand = random.choice(colors)
		c.itemconfig(front, fill=rand, outline=rand)
		c.itemconfig(front1, fill=rand, outline=rand)
		c.itemconfig(front2, fill=rand, outline=rand)
		rand = random.choice(colors)
		c.itemconfig(left, fill=rand, outline=rand)
		c.itemconfig(left1, fill=rand, outline=rand)
		c.itemconfig(left2, fill=rand, outline=rand)
		rand = random.choice(colors)
		c.itemconfig(up, fill=rand, outline=rand)
		c.itemconfig(up1, fill=rand, outline=rand)
		c.itemconfig(up2, fill=rand, outline=rand)


def ColorThread():
	def white_line(x0, x1, y0, y1):
		# drawing a line
		dx = abs(x1 - x0)
		dy = abs(y1 - y0)
		x, y = x0, y0
		sx = -1 if x0 > x1 else 1
		sy = -1 if y0 > y1 else 1
		if dx > dy:
			err = dx / 2
			while x!=x1:
				listOfPixels.append(c.create_rectangle(x, y, x + 1, y + 1, fill='white', outline='white'))
				err -= dy
				if err < 0:
					y += sy
					err += dx
				x += sx
		else:
			err = dy / 2
			while y!=y1:
				listOfPixels.append(c.create_rectangle(x, y, x + 1, y + 1, fill='white', outline='white'))
				err -= dx
				if err < 0:
					x += sx
					err += dy
				y += sy
		listOfPixels.append(c.create_rectangle(x, y, x + 1, y + 1, fill='white', outline='white'))

	for i in pixels:
		white_line(*i)
	t2 = threading.Thread(target=ChangeColor)
	t2.start()


def StopChangingColor():
	global flagColor
	flagColor = False


buttonBlink = Button(text="Старт мерцания", width=20, font="Arial 12 bold", command=StartBlinking)
buttonBlink.place(x=40, y=0)
buttonMove = Button(text="Стоп мерцания", width=20, font="Arial 12 bold", command=StopBlinking)
buttonMove.place(x=280, y=0)
Label(text="To slow down blinking of the figure press the <Stop blinking> as many times as you need untill it stops "
           "after finishing drawing the figure.", bg="white").place(x=10, y=30)
buttonDrawFigure = Button(text="Рисование фигуры", width=20, font="Arial 12 bold", command=paral)
buttonDrawFigure.place(x=550, y=0)
ButtonChangeColors = Button(text="Смена цветов фигуры", width=20, font="Arial 12 bold", command=ColorThread)
ButtonChangeColors.place(x=550, y=50)
buttonStopChanging = Button(text="Стоп смены цветов", width=20, font="Arial 12 bold", command=StopChangingColor)
buttonStopChanging.place(x=300, y=50)
Label(text="Чтобы не поломать программу выключайте функционал, который включили перед этим,",
	font="Arial 12 bold").place(
	x=40, y=500)
Label(text="то есть если включили смену цвета фигуры,", font="Arial 12 bold").place(x=40, y=520)
Label(text="то и выключите её, а после этого включайте другую функцию фигуры. Спасибо!", font="Arial 12 bold").place(
	x=40, y=540)
Label(text="Последующие функции после смены цвета некоторое время работают медленее.", font="Arial 12 bold",
	bg="green").place(x=40, y=560)
Label(text="Дождитесь, пока будут работать нормально. Спасибо за ожидание.", font="Arial 12 bold", bg="green").place(
	x=40, y=580)

mainloop()
