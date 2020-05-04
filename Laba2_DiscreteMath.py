from tkinter import *
from tkinter import messagebox
import networkx as nx
import os
from random import choice, randint
import matplotlib.pyplot as plt

root = Tk()
root.title("Головне вікно")
root.geometry("400x250")


def give_info_about_student():
	Number = 29
	Group = 93
	M = "IB"
	messagebox.showinfo("ПІБ та Група студента",
		"Моя група: " + M + "-" + str(Group) + "\n" + "Мій номер у групі: " + str(Number) + "\n" +
		"ПІБ студента: Трибушенко Артем Сергійович")


def display_variant():
	Group = 93
	Number = 29
	M = "IB"
	if M=="ІО":
		Number += 2
	messagebox.showinfo("Варіант", "Мій варіант: " + str((Number + Group % 60) % 30 + 1))


def window2():
	global set_A, set_B, women, men
	set_A, set_B = set(), set()
	win2 = Toplevel(root)
	win2.title("Друге вікно")

	def add_toSet_woman(event):
		if var.get() == 0:
			try:
				set_A.add(women[event.widget.curselection()[0]])
			except IndexError:
				pass
		if var.get()==1:
			try:
				set_B.add(women[event.widget.curselection()[0]])
			except IndexError:
				pass
		label['text'] = 'set A = {}\nset B = {}\n'.format(set_A, set_B)

	def add_toSet_men(event):
		if var.get()==0:
			try:
				set_A.add(men[event.widget.curselection()[0]])
			except IndexError:
				pass
		if var.get()==1:
			try:
				set_B.add(men[event.widget.curselection()[0]])
			except IndexError:
				pass
		label['text'] = 'set A = {}\nset B = {}\n'.format(set_A, set_B)

	def clear_set_A():
		set_A.clear()
		label['text'] = 'set A = {}\nset B = {}\n'.format(set_A, set_B)

	def clear_set_B():
		set_B.clear()
		label['text'] = 'set A = {}\nset B = {}\n'.format(set_A, set_B)

	def save_set_A(event):
		try:
			os.mkdir(r"C:\Laboratorna#2")
		except FileExistsError:
			pass
		with open(r"C:\Laboratorna#2\set_A.txt", mode="w") as iv:
			iv.write(str(set_A))

	def save_set_B(event):
		try:
			os.mkdir(r"C:\Laboratorna#2")
		except FileExistsError:
			pass
		with open(r"C:\Laboratorna#2\set_B.txt", mode="w") as iv:
			iv.write(str(set_B))

	def show_from_file():
		show = Toplevel(win2)
		show.minsize(300, 100)
		f_set_A = open(r"C:\Laboratorna#2\set_A.txt", mode="r")
		f_set_B = open(r"C:\Laboratorna#2\set_B.txt", mode="r")
		f_set_A_read = f_set_A.read()
		f_set_B_read = f_set_B.read()
		f_set_A.close()
		f_set_B.close()
		Label(show, text=f"set A = {f_set_A_read}" + "\n" + f"set B = {f_set_B_read}", font="Arial 14").pack(
			fill=BOTH)

	Label(win2, text="Оберіть елементи для множин А та В", font="Arial 17 bold").grid(row=0, column=0, columnspan=5)
	var = IntVar()
	var.set(0)
	radiobutton0 = Radiobutton(win2, variable=var, text="Множина А", font="Arial 13", value=0)
	radiobutton1 = Radiobutton(win2, variable=var, text="Множина B", font="Arial 13", value=1)

	lf1 = LabelFrame(win2, text="Жіночі імена", font="Arial 13 bold")
	lf1.grid(row=3, column=0, columnspan=1)
	women = ["Anastasia", "Irina", "Regina", "Katherine", "Larisa", "Helga", "Diana", "Lily", "Marina"]
	men = ["Sergei", "Vladimir", "Michael", "Danila", "Andrew", "Tom", "Artemis", "Bob", "Mikol"]
	listbox1 = Listbox(lf1, selectmode=SINGLE, font="Arial 14")
	listbox1.focus_set()
	listbox1.bind("<<ListboxSelect>>", add_toSet_woman)
	listbox1.grid(row=3, column=0)
	for i in women:
		listbox1.insert(END, i)
	scrollbar1 = Scrollbar(lf1, command=listbox1.yview)
	listbox1.configure(yscrollcommand=scrollbar1.set)
	scrollbar1.grid(row=3, column=1, sticky=W)
	radiobutton0.grid(column=0, row=4, sticky=W)
	radiobutton1.grid(column=2, row=4, sticky=W)

	labelframe2 = LabelFrame(win2, text="Чоловічі імена", font="Arial 13 bold")
	labelframe2.grid(row=3, column=2, columnspan=2)
	listbox2 = Listbox(labelframe2, selectmode=SINGLE, font="Arial 14")
	listbox2.focus_set()
	listbox2.bind("<<ListboxSelect>>", add_toSet_men)
	listbox2.grid(row=3, column=2)
	for i in men:
		listbox2.insert(END, i)
	scrollbar2 = Scrollbar(labelframe2, command=listbox2.yview)
	listbox2.configure(yscrollcommand=scrollbar2.set)
	scrollbar2.grid(row=3, column=3, sticky=W)
	buttonA_save = Button(win2, text="Зберегти множину А", font="Arial 13 bold", width=20, height=1)
	buttonA_save.bind("<Button-1>", save_set_A)
	buttonA_save.grid(row=6, column=0)
	button_clearA = Button(win2, text="Очистити множину А", command=clear_set_A, font="Arial 13 bold", width=20,
		height=1)
	button_clearA.grid(row=7, column=0)
	buttonB_save = Button(win2, text="Зберегти множину В", font="Arial 13 bold", width=20, height=1)
	buttonB_save.bind("<Button-1>", save_set_B)
	buttonB_save.grid(row=6, column=2)
	button_clearB = Button(win2, text="Очистити множину В", command=clear_set_B, font="Arial 13 bold", width=20,
		height=1)
	button_clearB.grid(row=7, column=2)
	button_show_elements = Button(win2, text="Зчитати множини з файлу", command=show_from_file, font="Arial 13 bold",
		width=25, height=1)
	button_show_elements.grid(row=8, column=1)
	label = Label(win2, text="Множини А та В", font="Arial 13 bold", height=5)
	label.grid(row=9, column=0, columnspan=13)


def window3():
	def aSb(event):  # а кум б Головною умовою даного алгоритму є те що змінна а повинна бути тільки чоловіком, а змінна
		# б може бути як чоловіком так і жінкою
		global S
		S = {}
		set_a_A = set(i for i in set_A if i in men)
		set_a_B = set(i for i in set_B if i in men)
		set_a = set_a_A.union(set_a_B)
		set_b = set_A.union(set_B)
		for i in range(len(set_a)):
			one = choice(list(set_a))
			for j in range(randint(0, len(set_b))):
				second = choice(tuple(set_b))
				S[one] = second
			set_a.remove(one)
		g1 = nx.DiGraph()
		g1.add_nodes_from(i[0] for i in S.items())
		g1.add_edges_from(S.items())
		nx.draw_networkx(g1, pos=nx.spring_layout(g1), arrows=True, with_labels=True, edges=g1.edges(),
			edge_color="b")
		plt.show()

	def aRb(event):
		# головною умовою даного алгоритму є те, що а повинен бути тільки чоловіком, а б - жінкою і тільки один раз
		# і після цього вони зникають з обох множин
		global R
		R = {}
		set_a_A = set(i for i in set_A if i in men)
		set_a_B = set(i for i in set_B if i in men)
		set_a = set_a_A.union(set_a_B)
		set_b_A = set(i for i in set_A if i in women)
		set_b_B = set(i for i in set_B if i in women)
		set_b = set_b_A.union(set_b_B)
		for i in range(min(len(set_a), len(set_b))):
			one = choice(list(set_a))
			second = choice(list(set_b))
			R[one] = second
			set_a.remove(one)
			set_b.remove(second)
		g1 = nx.DiGraph()
		g1.add_nodes_from(i[0] for i in R.items())
		g1.add_edges_from(R.items())
		nx.draw_networkx(g1, pos=nx.spring_layout(g1), arrows=True, with_labels=True, edges=g1.edges(),
			edge_color="b")
		plt.show()

	def warn(event):
		messagebox.showinfo("Warning", "Щоб краще розгледіти графи при натисканні будь-яких з кнопок нижче, "
		                               "використовуйте кнопку <лупа> для більшого масштабу зображення та стрілочку "
		                               "вліво, аби повернутися до початкового масштабу. "
		                               "Після вибору даної кнопки виділяйте зону, яка Вас цікавить в прямокутник і "
		                               "приближення об'єкту спрацює")
		button0["text"] = "Відкрито"
		button0["state"] = DISABLED

	try:
		list_zip_men = list(zip(men, [0 for i in range(len(men))]))
		list_zip_women = list(zip(women, [1 for j in range(len(women))]))
	except NameError:
		messagebox.showinfo("Warning", "Спочатку зайдіть у друге вікно і вкажіть множини А та В")
		pass
	else:
		win3 = Toplevel(root)
		win3.title("Третє вікно")
		win3.focus_set()
		Label(win3, text="Відображення множин А, В і алгоритми відповідно до варіанту", font="Arial 17 bold").grid(
			row=0, column=0, columnspan=5)
		lblfrm1 = LabelFrame(win3, text="Елементи множини А", font="Arial 13 bold")
		lblfrm1.grid(row=3, column=0, columnspan=1)
		listbox1 = Listbox(lblfrm1, selectmode=SINGLE, font="Arial 14")
		listbox1.focus_set()
		listbox1.grid(row=3, column=0)
		for i in set_A:
			listbox1.insert(END, i)
		scrollbar1 = Scrollbar(lblfrm1, command=listbox1.yview)
		listbox1.configure(yscrollcommand=scrollbar1.set)
		scrollbar1.grid(row=3, column=1, sticky=W)
		lblfrm2 = LabelFrame(win3, text="Елементи множини B", font="Arial 13 bold")
		lblfrm2.grid(row=3, column=2, columnspan=2)
		listbox2 = Listbox(lblfrm2, selectmode=SINGLE, font="Arial 14")
		listbox2.focus_set()
		listbox2.grid(row=3, column=4)
		for i in set_B:
			listbox2.insert(END, i)
		scrollbar2 = Scrollbar(lblfrm2, command=listbox2.yview)
		listbox2.configure(yscrollcommand=scrollbar2.set)
		scrollbar2.grid(row=3, column=3, sticky=W)
		button0 = Button(win3, text="Дізнатися додаткову інформацію перед переглядом графів", font="Arial 14 bold",
			fg="red")
		button0.bind("<Button-1>", warn)
		button0.grid(row=4, column=1)
		button1 = Button(win3, text="Показати зв'язок aSb, якщо а - кум b", font='Arial 14 bold')
		button1.bind("<Button-1>", aSb)
		button1.grid(row=5, column=1)
		button2 = Button(win3, text="Показати зв'язок aSb, якщо а - чоловік b", font='Arial 14 bold')
		button2.bind("<Button-1>", aRb)
		button2.grid(row=7, column=1)


def window4():
	def buttonUnionfunc(event):
		g1 = nx.DiGraph()
		g1.add_nodes_from(i[0] for i in S.items())
		g1.add_nodes_from([i[0] for i in R.items()])
		g1.add_edges_from(S.items())
		g1.add_edges_from(R.items())
		nx.draw_networkx(g1, pos=nx.spring_layout(g1), arrows=True, with_labels=True, edges=g1.edges(),
			edge_color="b")
		plt.show()

	def buttonIntersectionfunc(event):
		Intersection = set(R.keys()) & set(S.keys())
		g1 = nx.DiGraph()
		g1.add_nodes_from(Intersection)
		g1.add_edges_from(i for i in S.items() if i[0] in Intersection)
		g1.add_edges_from(i for i in R.items() if i[0] in Intersection)
		nx.draw_networkx(g1, pos=nx.spring_layout(g1), arrows=True, with_labels=True, edges=g1.edges(),
			edge_color="b")
		plt.show()

	def buttonMinusfunc(event):
		c = list(R)
		for i in S:
			for j in R:
				if i==j:
					c.remove(j)
		g = nx.DiGraph()
		g.add_nodes_from(list(set_A | set_B))
		g.add_edges_from(c)
		nx.draw_networkx(g, pos=nx.spring_layout(g), arrows=True, with_labels=True, edges=g.edges())
		plt.show()

	def buttonUminusRfunc(event):
		c = list()
		for i in set_A:
			for j in set_B:
				if (i, j) not in R:
					c.append([i, j])
		g = nx.DiGraph()
		g.add_nodes_from(list(set_A | set_B))
		g.add_edges_from(c)
		nx.draw_networkx(g, pos=nx.spring_layout(g), arrows=True, with_labels=True, edges=g.edges())
		plt.show()

	def buttonSreversefunc(event):
		c = list()
		for i in S.items():
			c.append(i[::-1])
		g = nx.DiGraph()
		g.add_nodes_from(i[1] for i in S.items())
		g.add_edges_from(c)
		nx.draw_networkx(g, pos=nx.spring_layout(g), arrows=True, with_labels=True, edges=g.edges())
		plt.show()

	try:
		print(S, R, sep="\n")
	except NameError:
		messagebox.showinfo("Warning", "Спочатку зайдіть у вікна 2, 3, щоб сформувати множини і отримати відношення R "
		                               "i S")
	else:
		win4 = Toplevel(root)
		win4.title("Четверте вікно")
		win4.minsize(200, 200)
		buttonUnion = Button(win4, text="Відношення R∪S", font="Arial 14 bold", width=15)
		buttonUnion.bind("<Button-1>", buttonUnionfunc)
		buttonUnion.grid(row=1, column=1)
		buttonIntersection = Button(win4, text="Відношення R∩S", font="Arial 14 bold", width=15)
		buttonIntersection.bind("<Button-1>", buttonIntersectionfunc)
		buttonIntersection.grid(row=2, column=1)
		buttonMinus = Button(win4, text="Відношення R\\S", font="Arial 14 bold", width=15)
		buttonMinus.bind("<Button-1>", buttonMinusfunc)
		buttonMinus.grid(row=3, column=1)
		buttonUminusR = Button(win4, text="Відношення U\\R", font="Arial 14 bold", width=15)
		buttonUminusR.bind("<Button-1>", buttonUminusRfunc)
		buttonUminusR.grid(row=4, column=1)
		buttonSreverse = Button(win4, text="Відношення S^(-1)", font="Arial 14 bold", width=15)
		buttonSreverse.bind("<Button-1>", buttonSreversefunc)
		buttonSreverse.grid(row=5, column=1)


def win1():
	info_button = Button(root, text="Отримати відомості про студента", font="Arial 13",
		command=give_info_about_student).place(relx=0.17, rely=0.01)
	variant_button = Button(root, text="Дізнатися варіант студента", font="Arial 13", command=display_variant).place(
		relx=0.22, rely=0.17)
	window2_button = Button(root, text="Виклик другого вікна", font="Arial 13", command=window2).place(
		relx=0.28, rely=0.33)
	window3_button = Button(root, text="Виклик третього вікна", font="Arial 13", command=window3).place(
		relx=0.27, rely=0.49)
	window4_button = Button(root, text="Виклик четвертого вікна", font="Arial 13", command=window4).place(
		relx=0.25, rely=0.65)
	python_4ever = Label(root, text="Python 4ever!)", font="Arial 11", width=10, height=10).place(
		relx=0.01, rely=0.6)


win1()
root.mainloop()
