from tkinter import *
from tkinter import messagebox
import networkx as nx
import pylab as plt
from random import randint



root = Tk()


class Graph: #graphs and prim's algorithm
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
	def printMST(self, parent):
		print("Edge \tWeight")
		for i in range(1, self.V):
			print(i + 1, "-", parent[i] + 1, "\t", self.graph[i][parent[i]])

	def drawMST(self, parent):
		self.g = nx.DiGraph()
		self.listing = []
		self.old_edges = []
		for i in range(1, self.V + 1):
			for j in range(1, self.V + 1):
				self.old_edges.append((i, j))
		for i in range(1, self.V):
			self.g.add_node(i + 1)
			self.g.add_edge(i + 1, parent[i] + 1)
			self.listing.append((i + 1, parent[i] + 1))
		nx.draw(self.g, pos=nx.shell_layout(self.g), with_labels=True, font_weight='bold')
		nx.draw_networkx_edges(self.g, pos=nx.shell_layout(self.g), edgelist=self.old_edges, edge_color='b',
			with_labels=True)
		nx.draw_networkx_edges(self.g, pos=nx.shell_layout(self.g), edgelist=self.listing, edge_color='r',
			with_labels=True)
		plt.show()
	def minKey(self, key, mstSet):
		# Initilaize min value
		min = 1000000
		for v in range(self.V):
			if key[v] < min and mstSet[v]==False:
				min = key[v]
				min_index = v
		return min_index

	def primMST(self):
		key = [1000000] * self.V
		parent = [None] * self.V
		key[0] = 0
		mstSet = [False] * self.V
		parent[0] = -1
		for cout in range(self.V):
			u = self.minKey(key, mstSet)
			mstSet[u] = True
			for v in range(self.V):
				if self.graph[u][v] > 0 and mstSet[v]==False and key[v] > self.graph[u][v]:
					key[v] = self.graph[u][v]
					parent[v] = u
		self.printMST(parent)
		self.drawMST(parent)


def win_search(event):
	def prim_algorithm(event):
		g = Graph(int(entry_quantity.get()))
		g.graph = table
		g.primMST()

	def draw_graph(event):
		graph = nx.DiGraph()
		graph.add_nodes_from(i for i in range(1, int(entry_quantity.get()) + 1))
		for i in range(1, int(entry_quantity.get()) + 1):
			for j in range(1, int(entry_quantity.get()) + 1):
				graph.add_edge(i, j)
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
						row=5, column=int(entry_quantity.get()) + 1)
				else:
					table[i].append(int(entry_toplevel[i][j].get()))
		print(table)
		button_search = Button(toplevel, text="Почати пошук мінімального остовного дерева", font="Arial 12 bold")
		button_search.bind("<Button-1>", prim_algorithm)
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
		table = [[randint(1, 20) for i in range(number)] for j in range(number)]
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


def win2():
	pass


def win3():
	pass


def win1():
	global entry_quantity
	root.title("Головне вікно")
	root.geometry("300x150")
	main_menu = Menu(root)
	root.config(menu=main_menu)
	file_menu = Menu(main_menu, tearoff=0)
	file_menu.add_command(label="Матриця суміжності", command=win2)
	file_menu.add_command(label="Матриця інцидентності", command=win3())
	main_menu.add_cascade(label="Усі вікна", menu=file_menu)
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
