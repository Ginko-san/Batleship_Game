__author__ = 'salchi'

from tkinter import *
from tkinter import messagebox

root = Tk()

'''
def callback(event):
    print("Click at", event.x, event.y)


frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
'''


def callback():
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()
    status.clear()


class StatusBar(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

status = StatusBar(root)
status.set("%s", "Sabee")
status.pack(side=BOTTOM, fill=X)

root.protocol("WM_DELETE_WINDOW", callback)

root.mainloop()