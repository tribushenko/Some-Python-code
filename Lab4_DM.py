from tkinter import *
from tkinter import messagebox
import networkx as nx
import pylab as plt
from random import randint
from random import *

root = Tk()


def win_search(event):
	def heuristic_drawing(event):
		color_list = ["green", "red", "blue", "magenta", "yellow", "orange", "purple", "pink", "brown"]
		curcol = 1
		colarr = [0 for i in range(int(entry_quantity.get()))]
		def degforming():
			def getkey(item):
				return item[0]
			def degcount(d):
				degnum = 0
				for k in range(int(entry_quantity.get())):
					degnum += table[k][d]
				return degnum
			degarr = [[0 for i in range(2)] for j in range(int(entry_quantity.get()))]
			for j in range(int(entry_quantity.get())):
				degarr[j][0] = degcount(j) * 100
				degarr[j][1] = j
				for i in range(int(entry_quantity.get())):
					if table[i][j] == 1:
						degarr[j][0] += degcount(i)
			degarr.sort(key=getkey, reverse=True)
			return degarr
		def dyer(curcol, node):
			for k in range(int(entry_quantity.get())):
				if table[node][k] == 0:
					if colarr[k] == 0:
						colarr[k] = curcol
		sortarr = degforming()
		for i in range(int(entry_quantity.get())):
			if not colarr[sortarr[i][1]]:
				colarr[sortarr[i][1]] = curcol
				dyer(curcol, sortarr[i][1])
				curcol += 1
		for i in range(int(entry_quantity.get())):
			print(table[i])
		print(sortarr)
		print(colarr)
		graph = nx.DiGraph()
		graph.add_nodes_from(i for i in range(1, int(entry_quantity.get()) + 1))
		for i in range(int(entry_quantity.get())):
			for j in range(len(table[i])):
				if table[i][j]!=0:
					graph.add_edge(j + 1, i + 1)
		node_color = []
		for i in colarr:
			node_color.append(color_list[i])
		nx.draw_circular(graph, node_color=node_color, with_labels=True)
		plt.show()




	def draw_graph(event):
		graph = nx.DiGraph()
		graph.add_nodes_from(i for i in range(1, int(entry_quantity.get()) + 1))
		for i in range(int(entry_quantity.get())):
			for j in range(len(table[i])):
				if table[i][j] != 0:
					graph.add_edge(j + 1, i + 1)
		nx.draw_circular(graph, with_labels=1)
		plt.show()

	def start(event):
		global table
		table = []
		for i in range(len(entry_toplevel)):
			table.append([])
			for j in range(len(entry_toplevel[i])):
				if i==j and int(entry_toplevel[i][j].get())!=0:
					table[i].append(0)
					Label(toplevel,
						text="Перевірте таблицю! Вершина, \nяка йде із самої себе в себе має вагу 0, \nтому "
						     "буде 0 \nзадля коректної роботи алгоритму.", fg="red").grid(
						row=6, column=int(entry_quantity.get()) + 1)
				else:
					table[i].append(int(entry_toplevel[i][j].get()))
		button_search = Button(toplevel, text="Почати модифіковане евристичне розфарбування графа", font="Arial 12 bold")
		button_search.bind("<Button-1>", heuristic_drawing)
		button_search.grid(row=5, column=int(entry_quantity.get()) + 1)


	def warn(event):
		messagebox.showinfo("Warning", "Щоб краще розгледіти графи при натисканні кнопки <Створити граф>,\nвикорист"
		                               "овуйте кнопку <лупа> для більшого масштабу зображення та стрілочку "
		                               "вліво, аби повернутися до початкового масштабу. "
		                               "Після вибору даної кнопки виділяйте зону, яка Вас цікавить в прямокутник і "
		                               "приближення об'єкту спрацює.")
		button_help["text"] = "Відкрито"
		button_help["state"] = DISABLED

	def create_table(number):
		global table
		table = [[randint(0, 1) for i in range(number)] for j in range(number)]
		for i in range(number):
			for j in range(number):
				if i==j:
					table[i][j] = 0
				else:
					table[i][j] = table[j][i]
		print(table)
		return table

	def random_weight(event):
		element = create_table(int(entry_quantity.get()))
		for i in range(int(entry_quantity.get())):
			for j in range(int(entry_quantity.get())):
				entry_toplevel[i][j].insert(END, element[i][j])

	if not entry_quantity.get():
		messagebox.showinfo("Error occurred", "Спочатку задайте кількість вершин")
		return
	elif int(entry_quantity.get()) <= 0 or int(entry_quantity.get()) > 20:
		messagebox.showinfo("Error occurred", "Введіть допустиму кількість ребер")
		return
	toplevel = Toplevel(root)
	for i in range(int(entry_quantity.get()) + 1):
		for j in range(int(entry_quantity.get()) + 1):  # кількість вершин в графі
			if i==0:
				Label(toplevel, text='{}'.format(j), font='Arial 16 bold', width=3).grid(column=j, row=i, sticky=W)
			elif j==0:
				Label(toplevel, text='{}'.format(i), font='Arial 16 bold', width=3).grid(column=j, row=i, sticky=W)
			elif i==0 and j==0:
				Label(toplevel, text=' ', width=3).grid(column=j, row=i, sticky=W)
	entry_toplevel = []
	for i in range(int(entry_quantity.get())):
		entry_toplevel.append([])
		for j in range(int(entry_quantity.get())):
			entry_toplevel[i].append(Entry(toplevel, font='Arial 14', width=3))
			entry_toplevel[i][j].grid(row=i + 1, column=j + 1, sticky=W)
	button_random = Button(toplevel, text="Згенерувати вагу для ребер випадково", font="Arial 12 bold")
	button_random.grid(row=1, column=int(entry_quantity.get()) + 1)
	button_random.bind("<Button-1>", random_weight)
	button_help = Button(toplevel, text="Додаткова інформація перед переглядом графів", font="Arial 10 bold")
	button_help.bind("<Button-1>", warn)
	button_help.grid(row=3, column=int(entry_quantity.get()) + 1)
	draw_graph_but = Button(toplevel, text="Створити граф", font="Arial 12 bold")
	draw_graph_but.bind("<Button-1>", draw_graph)
	draw_graph_but.grid(row=2, column=int(entry_quantity.get()) + 1)
	button_start = Button(toplevel, text="Зчитати дані з таблиці", font="Arial 13 bold")
	button_start.bind("<Button-1>", start)
	button_start.grid(row=4, column=int(entry_quantity.get()) + 1)


def give_info_about_student(event):
	nzk = 9332
	variant = (nzk % 10) + 1
	top_level = Toplevel(root)
	Label(top_level, text="ПІБ: Трибушенко Артем Сергійович" + "\n" + "Група: ІВ-93" + "\n" + "Номер залікової книжки "
	                      + str(nzk) + "\n" + "Варіант: " + str(variant), font="Arial 13 bold").place(relx=0.09,
		rely=0.1)
	top_level.geometry("350x100")


def win1():
	global entry_quantity
	root.title("Головне вікно")
	root.geometry("300x150")
	entry_quantity = Entry(root, width=23)
	entry_quantity.place(relx=0.25, rely=0.17)
	Label(root, text="Введіть кількість вершин графа.", font="Arial 13 bold").place(
		relx=0.05, rely=0)
	button_variant = Button(root, text="Інформація про студента", font="Arial 12 bold")
	button_variant.place(relx=0.13, rely=0.7)
	button_variant.bind("<Button-1>", give_info_about_student)
	Label(root, text="Перейти до побудови матриці вагів", font="Arial 10 bold", fg="purple").place(relx=0.1, rely=0.3)
	button_matrix = Button(root, text="Перейти до побудови", font="Arial 11 bold")
	button_matrix.place(relx=0.2, rely=0.47)
	button_matrix.bind("<Button-1>", win_search)


win1()
root.mainloop()
