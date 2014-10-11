__author__ = 'salchi'

from tkinter import *
from random import *

main = Tk()


class sin_nombre():

    def __init__(self, player1, player2, x, y, ships, menu):
        self.window = Toplevel()    # This create a window for the game.

        self.player1 = player1
        self.player2 = player2

        self.x = x
        self.y = y

        self.ships = ships

        self.matrix_player_1 = []
        self.matrix_comp_player_2 = []

        self.matrix_shoots_player_1 = []
        self.matrix_shoots_comp_player_2 = []

#---------------------------- CREATE MATRIX ---------------------------------------

        for i in range(x):      # This create a matrix where I put the Imgs Later.
            self.matrix_player_1.append([])
            self.matrix_comp_player_2.append([])
            for j in range(y):
                self.matrix_player_1[i].append(0)
                self.matrix_comp_player_2[i].append(0)

        for i in range(x):      # and that it's for the shoots of the players and machine.
            self.matrix_shoots_player_1.append([])
            self.matrix_shoots_comp_player_2.append([])
            for j in range(y):
                self.matrix_shoots_player_1[i].append(0)
                self.matrix_shoots_comp_player_2[i].append(0)

#--------------------------- CREATE SHIPS -------------------------------------------

        #for i in range(0, self.ships - 1):



def hide_me(event):     # se encarga de hacer invisible cualquier evento asignado.
    event.widget.pack_forget()

root = Tk()
btn = Button(root, text="Click")
btn.bind('<Button-1>', hide_me)
btn.pack()
btn2=Button(root, text="Click too")
btn2.bind('<Button-1>', hide_me)
btn2.pack()
root.mainloop()