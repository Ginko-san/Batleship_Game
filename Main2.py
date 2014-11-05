__author__ = 'salchi'

from tkinter import *
from StatusBar import StatusBar
root = Tk()
root.geometry("1280x700")
root.resizable(0, 0)  # Code to ensure that the window did not resize.


class Main():
    def __init__(self, master):
        self.master = master

    frm_1 = Frame(root, width=520, height=520, bd=-2, bg="red")
    frm_2 = Frame(root, width=520, height=520, bd=-2, bg="green")

    frm_1.pack(side=LEFT)
    frm_1.pack_propagate(0)

    frm_2.pack(side=RIGHT)


    #def RunMain(self):

def callback(event):
    print("Click at", event.x, event.y)


Bar_1 = StatusBar(root)
#Bar_2 = StatusBar(root, Main.frm_2)

Bar_1.set("%s", "Turno Jugador 1")
#Bar_2.set("%s", "Espera")

Bar_1.pack(padx=1, pady=65)


Main.frm_1.bind("<Button-1>", callback)
Main.frm_2.bind("<Button-1>", callback)

root.bind("<Button-1>", callback)

Main(root)

root.mainloop()