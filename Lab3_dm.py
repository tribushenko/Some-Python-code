from tkinter import *
from tkinter import messagebox
import networkx as nx
import pylab as plt
from random import randint, choice

root, vertexes = Tk(), {}


def draw_graph(event):
	local_vertexes = {}
	for k, v in vertexes.items():
		for i in range(len(v)):
			local_vertexes[k] = v.pop()
	print(local_vertexes)
	g1 = nx.DiGraph()
	g1.add_nodes_from(i[1] for i in local_vertexes.items())
	# g1.add_nodes_from(i[0] for i in local_vertexes0.items())
	g1.add_edges_from(i for i in local_vertexes.items())
	# g1.add_edges_from(i[::-1] for i in local_vertexes.items())
	# g1.add_edges_from(i for i in local_vertexes0.items())
	nx.draw_networkx(g1, pos=nx.spring_layout(g1), arrows=True, with_labels=True, edges=g1.edges(),
		edge_color="b")
	plt.show()


def warn(event):
	messagebox.showinfo("Warning", "Щоб краще розгледіти графи при натисканні кнопки <Створити граф>,\n"
	                               "використовуйте кнопку <лупа> для більшого масштабу зображення та стрілочку "
	                               "вліво, аби повернутися до початкового масштабу. "
	                               "Після вибору даної кнопки виділяйте зону, яка Вас цікавить в прямокутник і "
	                               "приближення об'єкту спрацює.")


def give_info_about_student():
	nzk = 9332
	variant = (nzk % 10) + 1
	top_level = Toplevel(root)
	Label(top_level, text="ПІБ: Трибушенко Артем Сергійович" + "\n" + "Група: ІВ-93" + "\n" + "Номер залікової книжки "
	                      + str(nzk) + "\n" + "Варіант: " + str(variant), font="Arial 13 bold").place(relx=0.09,
		rely=0.1)
	top_level.geometry("350x100")


def take_parameters_for_algorithm(event):
	if entry1_root.get() and entry2_root.get():
		vertex1 = entry1_root.get()
		vertex2 = entry2_root.get()
		get_vertexes(vertex1, vertex2)
	else:
		pass


def print_vertexes(event):
	toplevel = Toplevel(root)
	toplevel.title("Вершини")
	Label(toplevel, text=vertexes, font="Arial 12 bold ").place(relx=0, rely=0.1)
	toplevel.geometry("999x100")


def get_vertexes(vertex1, vertex2):
	if vertex1 not in vertexes.keys():
		vertexes[vertex1] = set(vertex2)
	elif vertex1 in vertexes.keys():
		vertexes[vertex1].add(vertex2)


def random_vertexes(event):
	quantity_of_vertex2 = randint(1, 10)
	for j in range(1, 11):
		vertexes.update({str(j): set(str(randint(1, 10)) for i in range(quantity_of_vertex2) if i != j)})


def win2():
	pass


def win3():
	pass


root.title("Головне вікно")
root.geometry("500x400")
main_menu = Menu(root)
root.config(menu=main_menu)
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Дізнатися інформацію про студента", command=give_info_about_student)
file_menu.add_command(label="Матриця суміжності", command=win2)
file_menu.add_command(label="Матриця інцидентності", command=win3())
main_menu.add_cascade(label="Усі вікна", menu=file_menu)
entry1_root = Entry(root, width=23)
entry1_root.place(relx=0.1, rely=0.07)
entry2_root = Entry(root, width=23)
entry2_root.place(relx=0.5, rely=0.07)
Label(root, text="Введіть дані для графа, щоб знайти найкоротший шлях", font="Arial 13 bold").place(
	relx=0.04, rely=0.01)
button1 = Button(root, text="Зчитати обидва параметри", font="Arial 13 bold")
button1.bind("<Button-1>", take_parameters_for_algorithm)
button1.place(relx=0.27, rely=0.13)
Label(root, text="Щоб коректно зчитувати дані з поля вводу вершин, \nвводьте відразу дві вершини, "
                 "а інакше зчитування не буде праюцювати.", fg="red", font="Arial 11 ").place(relx=0.009, rely=0.21)
button_random = Button(root, text="Сформувати граф випадковим способом", font="Arial 13 bold")
button_random.place(relx=0.15, rely=0.3)
button_random.bind("<Button-1>", random_vertexes)
button2 = Button(root, text="Переглянути вершини", font="Arial 12 bold")
button2.place(relx=0.32, rely=0.4)
button2.bind("<Button-1>", print_vertexes)
button0 = Button(root, text="Додаткова інформація перед переглядом графу", font="Arial 11 bold", fg="red")
button0.bind("<Button-1>", warn)
button0.place(relx=0.1, rely=0.5)
button_draw = Button(root, text="Створити граф", font="Arial 13 bold")
button_draw.place(relx=0.32, rely=0.6)
button_draw.bind("<Button-1>", draw_graph)

root.mainloop()
