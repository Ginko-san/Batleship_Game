__author__ = 'salchi'

from tkinter import *
from tkinter import messagebox
from random import *


class Main():
    def __init__(self, player1, player2, x, y, ships, menu):
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

        # --------------------------- CREATE SHIPS -------------------------------------------

        for i in range(0, self.ships - 1):  # Create the ships in the matrix's
            self.matrix_shoots_player_1[randrange(0, x - 1)][randrange(0, y - 1)] = 1
            self.matrix_shoots_comp_player_2[randrange(0, x - 1)][randrange(0, y - 1)] = 1

        #--------------------------                ------------------------------------------

        self.battle_ship = PhotoImage(file="Imgs/ship02.gif")
        self.explotion = PhotoImage(file="Imgs/explo01.gif")
        self.sea = PhotoImage(file="Imgs/sea.gif")

        for x in range(len(self.matrix_shoots_player_1)):
            for y in range(len(x)):
                lbl = Label(self.window, text="", image=self.sea)
                self.matrix_player_1[x][y] = lbl
                self.matrix_player_1[x][y].grid(column=y, row=x)
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
                messagebox.showinfo("End...",
                                    "Player %s  won! for now :3!" % self.player2)  # adaptar nombre j2 con comp


