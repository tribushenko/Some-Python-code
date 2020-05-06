from tkinter import *
from tkinter import messagebox
import networkx as nx
import pylab as plt
from random import randint

root = Tk()


def win_search(event):
	def main_algorithm(event):
		pass

	def draw_graph(event):
		graph = nx.DiGraph()
		graph.add_nodes_from(i for i in range(1, int(entry_quantity.get()) + 1))
		for i in range(1, int(entry_quantity.get()) + 1):
			for j in range(1, int(entry_quantity.get()) + 1):
				graph.add_edge(i, j)
		nx.draw_circular(graph, with_labels=1)
		plt.show()

	def warn(event):
		messagebox.showinfo("Warning", "Щоб краще розгледіти графи при натисканні кнопки <Створити граф>,\nвикорист"
		                               "овуйте кнопку <лупа> для більшого масштабу зображення та стрілочку "
		                               "вліво, аби повернутися до початкового масштабу. "
		                               "Після вибору даної кнопки виділяйте зону, яка Вас цікавить в прямокутник і "
		                               "приближення об'єкту спрацює.")
		button_help["text"] = "Відкрито"
		button_help["state"] = DISABLED

	def create_table(number):
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
		Label(toplevel, text="Введіть дві вершини, між якими треба знайти найкоротшу відстань: ", font="Arial 12").grid(
			row=4, column=int(entry_quantity.get()) + 1)
		Label(toplevel, text=" Перша вершина", font="Arial 12 bold").grid(row=5, column=int(entry_quantity.get()) + 1)
		entry_first_vertex = Entry(toplevel)
		entry_first_vertex.grid(row=6, column=int(entry_quantity.get()) + 1)
		Label(toplevel, text=" Друга вершина", font="Arial 12 bold").grid(row=7, column=int(entry_quantity.get()) + 1)
		entry_second_vertex = Entry(toplevel)
		entry_second_vertex.grid(row=8, column=int(entry_quantity.get()) + 1)
		button_draw_graph = Button(toplevel, text="Знайти найкоротшу відстань", font="Arial 12 bold", fg="purple")
		button_draw_graph.bind("<Button-1>", main_algorithm)
		button_draw_graph.grid(row=9, column=int(entry_quantity.get()) + 1)

	if not entry_quantity.get():
		messagebox.showinfo("Error occurred", "Спочатку задайте кількість вершин")
		return
	elif int(entry_quantity.get()) <= 0 or int(entry_quantity.get()) > 20:
		messagebox.showinfo("Error occurred", "Введіть допустиму кількість ребер")
		return
	toplevel = Toplevel(root)
	for i in range(int(entry_quantity.get()) + 1):
		for j in range(int(entry_quantity.get()) + 1):  # кількість вершин в графі
			if i == 0:
				Label(toplevel, text='{}'.format(j), font='Arial 16 bold', width=3).grid(column=j, row=i, sticky=W)
			elif j == 0:
				Label(toplevel, text='{}'.format(i), font='Arial 16 bold', width=3).grid(column=j, row=i, sticky=W)
			elif i == 0 and j == 0:
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
