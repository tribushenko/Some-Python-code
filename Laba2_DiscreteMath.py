from tkinter import *
from tkinter import messagebox
import pickle
import os

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
    if M == "ІО":
        Number += 2
    messagebox.showinfo("Варіант", "Мій варіант: " + str((Number + Group % 60) % 30 + 1))


def window2():
    global set_A, set_B
    set_A, set_B = set(), set()
    win2 = Toplevel(root)
    win2.title("Друге вікно")

    def add_toSet_woman(event):
        if var.get() == 0:
            try:
                set_A.add(women[event.widget.curselection()[0]])
            except IndexError:
                pass
        if var.get() == 1:
            try:
                set_B.add(women[event.widget.curselection()[0]])
            except IndexError:
                pass
        label['text'] = 'set A = {}\nset B = {}\n'.format(set_A, set_B)

    def add_toSet_men(event):
        if var.get() == 0:
            try:
                set_A.add(men[event.widget.curselection()[0]])
            except IndexError:
                pass
        if var.get() == 1:
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
    women = ["Anastasia", "Irina", "Regina", "Katherine", "Larisa", "Helga", "Diana", "Lily", "Marina", "Helen",
             "Maryanna"]
    men = ["Sergei", "Vladimir", "Michael", "Danila", "Andrew", "Tom", "Artemis", "Bob", "Mikol", "Pedro",
           "Alexei"]
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
    # function clear BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
    button_clearB.grid(row=7, column=2)
    button_show_elements = Button(win2, text="Зчитати множини з файлу", command=show_from_file, font="Arial 13 bold",
                                  width=25, height=1)
    button_show_elements.grid(row=8, column=1)
    label = Label(win2, text="Множини А та В", font="Arial 13 bold", height=5)
    label.grid(row=9, column=0, columnspan=13)


def window3():
    pass


def window4():
    pass


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
root.mainloop()
