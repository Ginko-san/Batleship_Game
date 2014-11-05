__author__ = 'salchi'

from tkinter import *
from tkinter import messagebox
from random import *

class Main():
    def __init__(self, player1, player2, x, y, ships):

        self.player1 = player1
        self.player2 = player2

        self.x = x
        self.y = y

        self.ships = ships

        self.matrix_player_1 = []
        self.matrix_comp_player_2 = []

        self.matrix_shoots_player_1 = []
        self.matrix_shoots_comp_player_2 = []

        # ---------------------------- CREATE MATRIX ---------------------------------------

        for i in range(x):  # This create a matrix where I put the Imgs Later.
            self.matrix_player_1.append([])
            self.matrix_comp_player_2.append([])
            for j in range(y):
                self.matrix_player_1[i].append(0)
                self.matrix_comp_player_2[i].append(0)

        for i in range(x):  # and that it's for the shoots of the players and machine.
            self.matrix_shoots_player_1.append([])
            self.matrix_shoots_comp_player_2.append([])
            for j in range(y):
                self.matrix_shoots_player_1[i].append(0)
                self.matrix_shoots_comp_player_2[i].append(0)

        self.imprimir = print(self.matrix_shoots_player_1, "\n", self.matrix_shoots_comp_player_2)
        #--------------------------- CREATE SHIPS -------------------------------------------

        for i in range(0, self.ships):  # Create the ships in the matrix's
            verify_x = randrange(0, x - 1)
            verify_y = randrange(0, y - 1)
            while self.matrix_shoots_player_1[verify_x][verify_y] == 1:
                verify_x = randrange(0, x - 1)
                verify_y = randrange(0, y - 1)
            self.matrix_shoots_player_1[verify_x][verify_y] = 1
            verify_x = randrange(0, x - 1)
            verify_y = randrange(0, y - 1)
            while self.matrix_shoots_comp_player_2[verify_x][verify_y] == 1:
                verify_x = randrange(0, x - 1)
                verify_y = randrange(0, y - 1)
            self.matrix_shoots_comp_player_2[verify_x][verify_y] = 1

        self.imprimir2 = print(self.matrix_shoots_player_1, "\n", self.matrix_shoots_comp_player_2)
        #--------------------------                ------------------------------------------

        self.battle_ship = PhotoImage(file="Imgs/ship02.png")
        self.explotion = PhotoImage(file="Imgs/explo01.png")
        self.sea = PhotoImage(file="Imgs/sea.png")

    def images(self, frame, matrix_shoot, matrix):
        for x in range(len(matrix_shoot)):
            for y in range(len(matrix_shoot[x])):
                lbl = Label(frame, text="", image=self.sea)
                matrix[x][y] = lbl
                matrix[x][y].grid(column=y, row=x)

    def click(self):

        '''
        self.stat_player1 = Label(self.window, text=("Nick: %s" % self.player1))
        self.stat_comp_player2 = Label(self.window, text=("Nick: %s" % self.player2))

        self.stat_shoots_player1 = Label(self.window, text=("Shoots: %s" % )) # pensar
        self.stat_shoots_comp_player2 = Label(self.window, text=("Shoots: %s" % )) # pensar

        self.stat_shoots_successful_player1 = Label(self.window, text=("Shoots: %s" % )) # pensar
        self.stat_shoots_successful_comp_player2 = Label(self.window, text=("Shoots: %s" % )) # pensar

        self.stat_player1.grid(row=x, column=0)
        self.stat_comp_player2.grid(row=x, column=0)

        self.stat_shoots_player1.grid(row=x, column=0)
        self.stat_shoots_comp_player2.grid(row=x, column=0)

        self.stat_shoots_successful_player1.grid(row=x, column=0)
        self.stat_shoots_successful_comp_player2.grid(row=x, column=0)
        '''
    def win_lose(self):
        if self.stat_shoots_successful_player1 == self.ships:
            messagebox.showinfo("End...", "Player %s  won! for now :3!" % self.player1)
                # Falta mas...
        elif self.stat_shoots_successful_comp_player2 == self.ships:
            messagebox.showinfo("End...", "Player %s  won! for now :3!" % self.player2) # adaptar nombre j2 con comp


def hide_me(event):  # se encarga de hacer invisible cualquier evento asignado.
    event.widget.pack_forget()

'''
root = Tk()
btn = Button(root, text="Click")
btn.bind('<Button-1>', hide_me)
btn.pack()
'''