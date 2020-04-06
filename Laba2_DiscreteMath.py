from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Головне вікно")
root.geometry("1300x600")


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


