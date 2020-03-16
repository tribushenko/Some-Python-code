from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from random import randrange
import os

root = Tk()
root.title("Головне вікно")
root.geometry("1300x600")


def substraction(b, a):
    dif_set = b.difference(a)
    return dif_set


def union_of_sets(a, dif_set):
    union_set = a.union(dif_set)
    return union_set


def display_variant():
    Group = 93
    Number = 29
    M = "IB"
    if M == "ІО":
        Number += 2
    messagebox.showinfo("Варіант", "Мій варіант: " + str((Number + Group % 60) % 30 + 1))


def give_info_about_student():
    Number = 29
    Group = 93
    M = "IB"
    messagebox.showinfo("ПІБ та Група студента",
                        "Моя група: " + M + "-" + str(Group) + "\n" + "Мій номер у групі: " + str(Number) + "\n" +
                        "ПІБ студента: Трибушенко Артем Сергійович")


def get_power():
    global power_A, power_B, power_C
    try:
        power_A = int(entry_root1.get())
        power_B = int(entry_root2.get())
        power_C = int(entry_root3.get())
    except ValueError:
        messagebox.showinfo("Error occurred", "Трапилася помилка - введіть цілі натуральні числа")
    messagebox.showinfo("Потужності", "Ви ввели потужності множин: " + "\n" + "Потужність А = " + str(power_A) + "\n" +
                        "Потужність B = " + str(power_B) + "\n" + "Потужність C = " + str(power_C))


def random_filling():
    global set_A, set_B, set_C
    try:
        set_A = set([randrange(0, 256) for i in range(power_A)])
        set_B = set([randrange(0, 256) for i in range(power_B)])
        set_C = set([randrange(0, 256) for i in range(power_C)])
    except NameError:
        messagebox.showinfo("Error occurred", "Спочатку введіть потужність множин")


def solo():
    global set_A, set_B, set_C
    try:
        set_A = set(int(i) for i in entry_root4.get().split(","))
        set_B = set(int(i) for i in entry_root5.get().split(","))
        set_C = set(int(i) for i in entry_root6.get().split(","))
    except ValueError as err:
        print(err)


def universal_set():
    global uni_set
    try:
        low, high = int(entry_root7.get()), int(entry_root8.get())
        if low >= 0 and high <= 255:
            uni_set = set(i for i in range(low, high + 1))
    except ValueError:
        messagebox.showinfo("Error occurred", "Enter integers")


def window2():
    def result(event):
        global final_D
        act1 = substraction(set_B, set_A)
        act2 = union_of_sets(set_A, act1)
        final_D = substraction(act2, set_C)

        def first_step(event):
            def second_step(event):
                def third_step(event):
                    Label(win1, text="(A ∪ (B \\ A))\\C =  " + str(final_D),
                          font='Arial 14', justify=LEFT).grid(row=21, sticky=W)

                Label(win1, text="A ∪ (B \\ A) = " + str(act2), font='Arial 14', justify=LEFT).grid(
                    row=13, sticky=W)
                button4_win2 = Button(win1, text="Третій крок", width=30)
                button4_win2.bind("<Button-1>", third_step)
                button4_win2.grid(row=14, sticky=W)

            Label(win1, text="B \\ A = " + str(act1), font='Arial 14', justify=LEFT).grid(row=11, sticky=W)
            button3_win2 = Button(win1, text="Другий крок", width=30)
            button3_win2.bind("<Button-1>", second_step)
            button3_win2.grid(row=12, sticky=W)

        Label(win1, text="(A ∪ (B \\ A))\\C = " + str(final_D), font='Arial 14', justify=LEFT).grid(
            row=9, sticky=W)
        button2_win2 = Button(win1, text="Перший крок", width=30)
        button2_win2.bind("<Button-1>", first_step)
        button2_win2.grid(row=10, sticky=W)

    def save(event):
        try:
            os.mkdir(r"C:\Laboratorna#1")
        except FileExistsError:
            pass
        with open(r"C:\Laboratorna#1\file1.txt", mode="w") as iv:
            iv.write(str(final_D))

    win1 = Toplevel(root)
    win1.title("Вікно 2")
    Label(win1, text="Заданий вираз:", font='Arial 14', justify=LEFT, width=30).grid(
        sticky=W)
    Label(win1, text="(A ∪ (B \\ A))\\C = ", font='Arial 14', justify=LEFT, width=30).grid(
        row=1, column=0, sticky=W)
    try:
        Label(win1, text="A = " + str(set_A), font='Arial 14', justify=LEFT).grid(row=2, sticky=W)
        Label(win1, text="B = " + str(set_B), font='Arial 14', justify=LEFT).grid(row=3, sticky=W)
        Label(win1, text="C = " + str(set_C), font='Arial 14', justify=LEFT).grid(row=4, sticky=W)
        button_win2 = Button(win1, text="Результати", width=30)
        button_win2.bind("<Button-1>", result)
        button_win2.grid(row=6, sticky=W)
        button1_win2 = Button(win1, text="Зберегти", width=30)
        button1_win2.bind("<Button-1>", save)
        button1_win2.grid(row=7, column=0, sticky=W)
    except NameError:
        messagebox.showinfo("Error", "A, B або C не визначені. Тож Ви можете тільки подивитися умову (^_^)")


def window3():
    def result_wind3(event):
        global final_Z
        act1 = set_A.union(set_B)
        final_Z = substraction(act1, set_C)

        def first_step(event):
            def second_step(event):
                Label(win3, text="(A ∪ B)\\C =" + str(final_Z), font='Arial 14', justify=LEFT).grid(
                    row=16, sticky=W)

            Label(win3, text="A ∪ B " + str(act1), font='Arial 14', justify=LEFT).grid(row=12, sticky=W)
            button4_win3 = Button(win3, text="  Другий крок ", width=30)
            button4_win3.bind("<Button-1>", second_step)
            button4_win3.grid(row=13, column=0, sticky=W)

        Label(win3, text="(A ∪ B) \\ C = " + str(final_Z), font='Arial 14', justify=LEFT).grid(row=10, sticky=W)
        button3_win3 = Button(win3, text=" Перший крок ", width=30)
        button3_win3.bind("<Button-1>", first_step)
        button3_win3.grid(row=11, column=0, sticky=W)

    def save_wind3(event):
        try:
            os.mkdir(r"C:\Laboratorna#1")
        except FileExistsError:
            print("Yes")
        it = open(r"C:\Laboratorna#1\file2.txt", mode="w+")
        it.write(str(final_Z))
        it.close()

    win3 = Toplevel(root)
    win3.title("Вікно 3")
    Label(win3, text="Заданий вираз:", font='Arial 14', width=30).grid(sticky=W)
    Label(win3, text="(A ∪ (B \\ A))\\C =", font='Arial 14', justify=LEFT, width=30).grid(row=1, column=0, sticky=W)
    Label(win3, text="Спрощений =  (A ∪ B) \\ C", font='Arial 14', justify=LEFT, width=30).grid(row=2, column=0,
                                                                                                sticky=W)
    try:
        Label(win3, text="A = " + str(set_A), font='Arial 14', justify=LEFT).grid(row=4, sticky=W)
        Label(win3, text="B = " + str(set_B), font='Arial 14', justify=LEFT).grid(row=5, sticky=W)
        Label(win3, text="C = " + str(set_C), font='Arial 14', justify=LEFT).grid(row=6, sticky=W)
    except NameError:
        messagebox.showinfo("some error", "A, B або C не визначені. Тож Ви можете тільки подивитися умову (^_^)")
    button1_win3 = Button(win3, text="Результати", width=30)
    button1_win3.bind("<Button-1>", result_wind3)
    button1_win3.grid(row=8, sticky=W)
    button2_win3 = Button(win3, text="Зберегти", width=30)
    button2_win3.bind("<Button-1>", save_wind3)
    button2_win3.grid(row=9, column=0, sticky=W)


def window4():

    global X, Y
    try:
        X = set_A
        Y = set_C
    except NameError:
        messagebox.showinfo("Error", "Спочатку задайте множини А та В")

    def save_wind4(event):
        try:
            os.mkdir(r"C:\Laboratorna#1")
        except FileExistsError:
            print("File already exists")
        it = open(r"C:\Laboratorna#1\file3.txt", mode="w+")
        it.write(str(final_Z))
        it.close()

    def result_wind4(event):
        global Z
        Z = union_of_sets(X, Y)
        Label(win4, text="X ∪ Y = " + str(Z), font='Arial 14', justify=LEFT).grid(row=10, sticky=W)

    win4 = Toplevel(root)
    win4.title("Вікно 4")
    Label(win4, text="Заданий вираз:", font='Arial 14', width=30).grid(row=0, sticky=W)
    Label(win4, text="X = A; Y = C; Z = X ∪ Y", font='Arial 14', justify=LEFT).grid(row=1, sticky=W)
    Label(win4, text="X = " + str(X), font='Arial 14', justify=LEFT).grid(row=2, sticky=W)
    Label(win4, text="Y = " + str(Y), font='Arial 14', justify=LEFT).grid(row=3, sticky=W)
    button1_win4 = Button(win4, text="Результати", width=30)
    button1_win4.bind("<Button-1>", result_wind4)
    button1_win4.grid(row=4, sticky=W)
    button2_win4 = Button(win4, text="Зберегти", width=30)
    button2_win4.bind("<Button-1>", save_wind4)
    button2_win4.grid(row=5, column=0, sticky=W)


def window5():
    def read_D(event):
        global final_Dglobal
        with open(r"C:\Laboratorna#1\file1.txt", mode="r") as python:
            final_Dglobal = python.read()
        Label(win5, text="Неспрощена множина D=" + str(final_Dglobal), font='Arial 14').grid(row=3, column=1, sticky=W)

    def read_easy_D(event):
        global read_easy_Dglobal
        with open(r"C:\Laboratorna#1\file2.txt", mode="r") as python:
            read_easy_Dglobal = python.read()
        Label(win5, text="Спрощена множина D=" + str(read_easy_Dglobal), font="Arial 14").grid(
            row=3, column=1, sticky=W)

    def read_Z(event):
        global read_Zglobal
        with open(r"C:\Laboratorna#1\file3.txt", mode="r") as python:
            read_Zglobal = python.read()
        Label(win5, text="Множина Z =" + str(read_Zglobal), font='Arial 14').grid(row=3, column=1, sticky=W)

    def show_Z_easy(event):
        try:
            global show_Z_button
            show_Z_button = X.union(Y)
            Label(win5, text="Множина Z через вбудовані функції Python =" + str(show_Z_button), font='Arial 14').grid(
                row=3, column=1, sticky=W)
        except NameError:
            messagebox.showinfo("Спробуйте знову", "Немає множини А або В")

    def oneequalstwo(event):
        if final_Dglobal == read_easy_Dglobal:
            Label(win5, text="D: Дорівнює ", font='Arial 14').grid(row=6, column=1, sticky=W)
        else:
            Label(win5, text="Z: Не дорівнює ", font='Arial 14').grid(row=6, column=1, sticky=W)

    def threequalsfour(event):
        if str(Z) == str(show_Z_button):
            Label(win5, text="Z: Дорівнює ", font='Arial 14').grid(row=6, column=1, sticky=W)
        else:
            Label(win5, text="Z: Не дорівнює ", font='Arial 14').grid(row=6, column=1, sticky=W)

    win5 = Toplevel(root)
    win5.title("Вікно 5")
    button1_win5 = Button(win5, text="Зчитати множину D звичайну ", font='Arial 14', width=30)
    button1_win5.bind("<Button-1>", read_D)
    button1_win5.grid(sticky=W, row=1)
    button2_win5 = Button(win5, text="Зчитати множину D спрощену", font='Arial 14', width=30)
    button2_win5.bind("<Button-1>", read_easy_D)
    button2_win5.grid(sticky=W, row=2)
    button3_win5 = Button(win5, text="Зчитати множину Z", font='Arial 14', width=30)
    button3_win5.bind("<Button-1>", read_Z)
    button3_win5.grid(sticky=W, row=3)
    button4_win5 = Button(win5, text="Множина X ∪ Y", font='Arial 14', width=30)
    button4_win5.bind("<Button-1>", show_Z_easy)
    button4_win5.grid(sticky=W, row=4)
    button5_win5 = Button(win5, text="Перевірити на еквівалентність D", font='Arial 14', width=30)
    button5_win5.bind("<Button-1>", oneequalstwo)
    button5_win5.grid(sticky=W, row=5)
    button6_win5 = Button(win5, text="Перевірити на еквівалентність Z", font='Arial 14', width=30)
    button6_win5.bind("<Button-1>", threequalsfour)
    button6_win5.grid(sticky=W, row=6)


label_root3 = Label(root, text="Задайте потужність A: ", width=40, font='Arial 12', height=15,
                    justify=CENTER).place(relx=0.02, rely=0)
label_root2 = Label(root, text="Задайте потужність B: ", width=40, font='Arial 12', height=15,
                    justify=RIGHT).place(relx=0.35, rely=0)
label_root1 = Label(root, text="Задайте потужність C: ", width=40, height=15, font='Arial 12',
                    justify=CENTER).place(relx=0.68, rely=0)
entry_root1 = Entry(root, width=30)
entry_root1.place(relx=0.09, rely=0.25)
entry_root2 = Entry(root, width=30)
entry_root2.place(relx=0.42, rely=0.25)
entry_root3 = Entry(root, width=30)
entry_root3.place(relx=0.75, rely=0.25)
label_root4 = Label(root, text="Множина А:", width=30, font="Arial 12", height=15, justify=CENTER).place(
    relx=0.05, rely=0.3)
label_root5 = Label(root, text="Множина B:", width=30, font="Arial 12", height=15, justify=CENTER).place(
    relx=0.38, rely=0.3)
label_root6 = Label(root, text="Множина C:", width=30, font="Arial 12", height=15, justify=CENTER).place(
    relx=0.72, rely=0.3)
entry_root4 = Entry(root, width=30)
entry_root4.place(relx=0.08, rely=0.55)
entry_root5 = Entry(root, width=30)
entry_root5.place(relx=0.41, rely=0.55)
entry_root6 = Entry(root, width=30)
entry_root6.place(relx=0.75, rely=0.55)
label_root7 = Label(root, text="←-- Задайте діапазон множини від 0 до 255: --→", width=45, justify=CENTER,
                    font="Aria 17").place(relx=0.26, rely=0.8)
entry_root7 = Entry(root, width=30)
entry_root7.place(relx=0.08, rely=0.815)
entry_root8 = Entry(root, width=30)
entry_root8.place(relx=0.75, rely=0.815)
button_root1 = Button(root, text="Отримати відомості про студента", font="Arial 13",
                      command=give_info_about_student).place(
    relx=0.06, rely=0.01)
button_root2 = Button(root, text="Дізнатися варіант студента", font="Arial 13", command=display_variant).place(
    relx=0.275, rely=0.01)
button_root3 = Button(root, text="Сформувати випадковим чином множини A,B,C заданої потужності", font="Arial 13",
                      command=random_filling).place(relx=0.4575, rely=0.01)
button_root4 = Button(root, text="Сформувати універсальну множину", font="Arial 13", command=universal_set).place(
    rely=0.07, relx=0.06)
button_root5 = Button(root, text="Сформувати множину власноруч", font="Arial 13", command=solo).place(relx=0.29,
                                                                                                      rely=0.07)
button_root6 = Button(root, text="Отримати потужність", font="Arial 13", command=get_power).place(relx=0.502, rely=0.07)
main_menu = Menu(root)
root.config(menu=main_menu)
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Друге вікно", command=window2)
file_menu.add_command(label="Третє вікно", command=window3)
file_menu.add_command(label="Четверте вікно", command=window4)
file_menu.add_command(label="П'яте вікно", command=window5)
main_menu.add_cascade(label="Усі вікна", menu=file_menu)

root.mainloop()
