"""Žaidimas "Kryžiukai - Nuliukai". Skirtas žaisti dviems žaidėjams."""

from tkinter import *

# Žaidimo langas:
langas = Tk()
langas.title("Kryžiukai - Nuliukai")

# 9 žaidimo mygtukai:
b1 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10)
b2 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10)
b3 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10)
b4 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10)
b5 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10)
b6 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10)
b7 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10)
b8 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10)
b9 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10)

# Mygtukų išdėstymas:
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

langas.mainloop()
