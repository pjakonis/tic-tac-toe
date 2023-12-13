"""Žaidimas "Kryžiukai - Nuliukai". Skirtas žaisti dviems žaidėjams."""

from tkinter import *
from tkinter import messagebox

# Žaidimo langas:
langas = Tk()
langas.title("Kryžiukai - Nuliukai")


# Klasė, kurioje priskiriami 9 žaidimo mygtukai ir jų funkcija juos nuspaudus "TRUE - FALSE" tvarka.
class Zaidimas:
    def __init__(self):
        global clicked
        clicked = True

        # 9 žaidimo mygtukai:
        b1 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eilė(b1))
        b2 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eilė(b2))
        b3 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eilė(b3))
        b4 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eilė(b4))
        b5 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eilė(b5))
        b6 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eilė(b6))
        b7 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eilė(b7))
        b8 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eilė(b8))
        b9 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eilė(b9))
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

    # Mygtukų funkcija kuri nustato kokia reikšmė bus nuspaudus mygtuką. True arba False.
    def kieno_eilė(self, b):
        global clicked
        if b["text"] == " " and clicked == True:
            b["text"] = "X"
            clicked = False
        elif b["text"] == " " and clicked == False:
            b["text"] = "O"
            clicked = True
        else:
            messagebox.showerror("Kryžiukai - Nuliukai", "Ei, šis langelis jau pasirinktas!\n Pasirink tuščią langelį!")


Zaidimas()

langas.mainloop()
