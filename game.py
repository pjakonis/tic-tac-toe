"""Žaidimas "Kryžiukai - Nuliukai". Skirtas žaisti dviems žaidėjams."""

from tkinter import *
from tkinter import messagebox

# Žaidimo langas:
langas = Tk()
langas.title("Kryžiukai - Nuliukai")

meniu = Menu(langas)
langas.config(menu=meniu)

# Create an options menu
kaskada = Menu(meniu, tearoff=False)
meniu.add_cascade(label="Meniu", menu=kaskada)
kaskada.add_command(label="Naujas žaidimas")
kaskada.add_command(label="Išeiti", command=langas.quit)


# Klasė, kurioje priskiriami 9 žaidimo mygtukai ir jų funkcija juos nuspaudus "TRUE - FALSE" tvarka.
class Zaidimas:
    def __init__(self):
        global clicked
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        self.ejimu_skaicius = 0
        self.X_laimejimai = 0
        self.O_laimejimai = 0
        clicked = True

        # 9 žaidimo mygtukai:
        b1 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b1))
        b2 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b2))
        b3 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b3))
        b4 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b4))
        b5 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b5))
        b6 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b6))
        b7 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b7))
        b8 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b8))
        b9 = Button(langas, text=" ", font=("Arial", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b9))
        # Rezultato užrašas:
        self.rezultatas = Label(langas, text="")
        self.rezultatas.grid(row=3, column=1)

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
        # Rezultato išdėstymas:



    # Mygtukų funkcija kuri nustato kokia reikšmė bus nuspaudus mygtuką. True arba False.
    def kieno_eile(self, b):
        global clicked
        global ejimu_skaicius
        if b["text"] == " " and clicked == True:
            b["text"] = "X"
            clicked = False
            self.ejimu_skaicius += 1
            self.tikrinamas_laimejimas()
        elif b["text"] == " " and clicked == False:
            b["text"] = "O"
            clicked = True
            self.ejimu_skaicius += 1
            self.tikrinamas_laimejimas()
        else:
            messagebox.showerror("Kryžiukai - Nuliukai",
                                 "Ei, šis langelis jau pasirinktas!\n Pasirink tuščią langelį!")  # Pranešimas, jei mygtukas jau pasirinktas.

    def tikrinamas_laimejimas(self):  # Yra 8 galimi laimėjimo variantai.
        global laimejimas
        laimejimas = False

        #  Tikrinami "X" laimėjimai:
        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "X laimėjo!")
            self.X_laimejimai += 1
            self.reset()
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "X laimėjo!")
            self.X_laimejimai += 1
            self.reset()
        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "X laimėjo!")
            self.X_laimejimai += 1
            self.reset()
        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "X laimėjo!")
            self.X_laimejimai += 1
            self.reset()
        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "X laimėjo!")
            self.X_laimejimai += 1
            self.reset()
        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "X laimėjo!")
            self.X_laimejimai += 1
            self.reset()
        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "X laimėjo!")
            self.X_laimejimai += 1
            self.reset()
        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "X laimėjo!")
            self.X_laimejimai += 1
            self.reset()

            # Tikrinami "O" laimėjimai:
        elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "O laimėjo!")
            self.O_laimejimai += 1
            self.reset()
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "O laimėjo!")
            self.O_laimejimai += 1
            self.reset()
        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "O laimėjo!")
            self.O_laimejimai += 1
            self.reset()
        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "O laimėjo!")
            self.O_laimejimai += 1
            self.reset()
        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "O laimėjo!")
            self.O_laimejimai += 1
            self.reset()
        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "O laimėjo!")
            self.O_laimejimai += 1
            self.reset()
        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "O laimėjo!")
            self.O_laimejimai += 1
            self.reset()
        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            laimejimas = True
            messagebox.showinfo("Kryžiukai - Nuliukai", "O laimėjo!")
            self.O_laimejimai += 1
            self.reset()
        elif self.ejimu_skaicius == 9 and laimejimas == False:
            messagebox.showinfo("Kryžiukai - Nuliukai", "Lygiosios!")
            self.reset()


    def reset(self):
        self.rezultatas["text"] = f"X - {self.X_laimejimai}   :   O - {self.O_laimejimai}"
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        global clicked
        global laimejimas
        self.ejimu_skaicius = 0
        clicked = True
        laimejimas = False
        b1["text"] = " "
        b2["text"] = " "
        b3["text"] = " "
        b4["text"] = " "
        b5["text"] = " "
        b6["text"] = " "
        b7["text"] = " "
        b8["text"] = " "
        b9["text"] = " "


Zaidimas()

langas.mainloop()
