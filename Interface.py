__author__ = 'salchi'

from tkinter import *
from StatusBar import StatusBar
from tkinter import messagebox


class Dialog:
    def __init__(self, parent, n):

        top = self.top = Toplevel(parent)
        top.geometry("180x75")
        top.attributes("-toolwindow", 1)

        if n == 1 or n == 2:
            Label(top, text="Player Name %i" % n).pack()
        else:
            Label(top, text=n).pack()

        self.e = Entry(top)
        self.e.pack(padx=5)

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

        self.result = None

    def ok(self):
        self.result = self.e.get()

        self.top.destroy()


def callback(event):
    print("Click at", event.x, event.y)


def hide_me(event):  # se encarga de hacer invisible cualquier evento asignado.
    event.widget.pack_forget()


def Create_Main():
    root = Tk()
    root.geometry("1280x700")
    root.resizable(0, 0)  # Code to ensure that the window did not resize.
    root.title("Main")  # Set Main Title.

    font = ("Forte", 12)

    bkg = PhotoImage(file="Imgs/background2.gif")
    bkg_lbl = Label(root, image=bkg)
    bkg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

    lbl_1 = Label(root, text="Player 1", font=font, bg="White", fg="gray")
    lbl_1.place(x=180, y=130)

    lbl_1 = Label(root, text="Player 2", font=font, bg="White", fg="gray")
    lbl_1.place(x=950, y=130)

    Bar_1 = StatusBar(root)

    Bar_1.set("Turno: %s", "Jugador 1")
    Bar_1.pack(padx=30, pady=65)

    frm_2 = Frame(root, width=520, height=520, bd=-2, bg="gray")
    frm_1 = Frame(root, width=520, height=520, bd=-2, bg="gray")

    frm_1.pack(side=LEFT)
    #frm_1.pack_propagate(0)

    frm_2.pack(side=RIGHT)

    def dialog_cons(n, msg):
        """

            :rtype : object
            """
        widg = Dialog(root, n)
        root.wait_window(widg.top)
        while widg.result == "":
            if msg != None:
                messagebox.showinfo("Warning!", msg)
            else:
                messagebox.showinfo("Warning!", "Please insert the name for the %s Player!" % n)
            widg = Dialog(root, n)
            root.wait_window(widg.top)
        return widg.result

    OneTwoPlayer = messagebox.askyesno("Player or PC", "Do you want to play with other human? (No = PC)")
    if OneTwoPlayer == 1:
        player1 = dialog_cons(1, None)
        player2 = dialog_cons(2, None)
        print(player1, player2)    # Testing Lines
    else:
        player1 = dialog_cons(1, None)
        player2 = "Computer"
        print(player1, player2)    # Testing Lines

    try:
        ships = int(dialog_cons("Ships", "Please Quantity of ships for the Game!"))
    except ValueError:
        messagebox.showinfo("Warning!", "La variable debe ser numero")
        ships = int(dialog_cons("Ships", "Please Quantity of ships for the Game!"))
    print(ships)    # Testing Lines

    try:
        xy = int(dialog_cons("Ships", "Please Quantity of ships for the Game!"))
    except ValueError:
        messagebox.showinfo("Warning!", "La variable debe ser numero")
        xy = int(dialog_cons("Ships", "Please Quantity of ships for the Game!"))
    print(xy)    # Testing Lines

    frm_1.bind("<Button-1>", callback)
    frm_2.bind("<Button-1>", callback)

    root.bind("<Button-1>", callback)

    root.mainloop()


Create_Main()

