__author__ = 'salchi'

from tkinter import *
root = Tk()
root.geometry("1048x700")


class Main():
    def __init__(self, master):
        self.master = master

    frm_1 = Frame(root, width=520, height=520, bg="red")
    frm_2 = Frame(root, width=520, height=520, bg="green")

    frm_1.pack(side=LEFT)
    frm_2.pack(side=RIGHT)


def callback(event):
    print("Click at", event.x, event.y)


Main.frm_1.bind("<Button-1>", callback)
Main.frm_2.bind("<Button-1>", callback)

Main(root)

root.mainloop()