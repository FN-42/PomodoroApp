from tkinter import *

def appendSession():
    master = Tk()
    Label(master, text="Fach").grid(row=0)
    Label(master, text="Aufgabe").grid(row=1)
    Label(master, text="Dauer").grid(row=2)
    Label(master, text="Datum").grid(row=3)
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    mainloop()