"""Žaidimas "Kryžiukai - Nuliukai". Skirtas žaisti dviems žaidėjams."""

from tkinter import *
from tkinter import messagebox
import random

# Pagrindinis langas
langas = Tk()
langas.title("Kryžiukai-Nuliukai")

# Submeniu langas:
meniu = Menu(langas)
langas.config(menu=meniu)

submeniu = Menu(meniu, tearoff=False)
meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Naujas žaidimas", command=lambda: Zaidimas().naujas_zaidimas())
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=langas.quit)


# Klasė, kurioje priskiriami 9 žaidimo mygtukai ir jų funkcija juos nuspaudus "TRUE - FALSE" tvarka.
class Zaidimas:
    def __init__(self):
        global clicked
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        self.ejimu_skaicius = 0
        self.X_laimejimai = 0
        self.O_laimejimai = 0
        clicked = random.choice([True, False])

        # Žaidimo pristatymas ir spredimas kas pradės žaidimą:
        messagebox.showinfo("Kryžiukai-Nuliukai",
                            "Sveiki! Nuobodu? Pažaiskime Kryžiukus-Nuliukus!\n\nŠis žaidimas skirtas dviems. Tad, žaidėjai, išsirinkite, kas bus kryžiukas, o kas - nuliukas.\n\n Nuspaudus OK, burtais išrinksiu, kas pradės!")
        messagebox.showinfo("Kryžiukai-Nuliukai", f"Eni beni, diki daki...\n\nPradeda {'X' if clicked else 'O'}!")

        # 9 žaidimo mygtukai:
        b1 = Button(langas, text=" ", font=("San Francisco", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b1))
        b2 = Button(langas, text=" ", font=("San Francisco", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b2))
        b3 = Button(langas, text=" ", font=("San Francisco", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b3))

        b4 = Button(langas, text=" ", font=("San Francisco", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b4))
        b5 = Button(langas, text=" ", font=("San Francisco", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b5))
        b6 = Button(langas, text=" ", font=("San Francisco", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b6))

        b7 = Button(langas, text=" ", font=("San Francisco", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b7))
        b8 = Button(langas, text=" ", font=("San Francisco", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b8))
        b9 = Button(langas, text=" ", font=("San Francisco", 25), height=5, width=10,
                    command=lambda: self.kieno_eile(b9))

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

        # Rezultato užrašas:
        self.rezultatas = Label(langas, text="X - 0   :   O - 0", font=("San Francisco", 25))
        self.rezultatas.grid(row=3, column=1)

    # Mygtukų funkcija kuri nustato kokia reikšmė bus nuspaudus mygtuką. True arba False.
    def kieno_eile(self, b):
        global clicked
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

        # Pranešimas, jei mygtukas jau pasirinktas:
        else:
            messagebox.showerror("Kryžiukai-Nuliukai",
                                 "Ei, šis langelis jau užimtas!\n\nPasirink tuščią langelį...")

    # Yra 8 galimi laimėjimo variantai. Čia aprašomi 16 galimų laimėjimo variantų kryžiukams ir nuliukams:
    def tikrinamas_laimejimas(self):
        global laimejimas, clicked
        laimejimas = False

        #  Tikrinami "X" laimėjimai:
        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            laimejimas = True
            clicked = True
            messagebox.showinfo("Kryžiukai-Nuliukai", "X laimėjo!\n\nNuliuk, neliūdėk, bet kitą žaidimą pradeda X!")
            self.X_laimejimai += 1
            self.reset()
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            laimejimas = True
            clicked = True
            messagebox.showinfo("Kryžiukai-Nuliukai", "X laimėjo!\n\nŽaidimą pradeda X!")
            self.X_laimejimai += 1
            self.reset()

        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            laimejimas = True
            clicked = True
            messagebox.showinfo("Kryžiukai-Nuliukai", "X laimėjo!\n\nX pradeda kitą žaidimą!")
            self.X_laimejimai += 1
            self.reset()
        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            laimejimas = True
            clicked = True
            messagebox.showinfo("Kryžiukai-Nuliukai", "X laimėjo!\n\nBūūū, Nuliuk, kitą žaidimą pradeda X!")
            self.X_laimejimai += 1
            self.reset()

        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            laimejimas = True
            clicked = True
            messagebox.showinfo("Kryžiukai-Nuliukai", "X laimėjo!\n\nKas laimi, tas ir pradeda - X!")
            self.X_laimejimai += 1
            self.reset()
        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            laimejimas = True
            clicked = True
            messagebox.showinfo("Kryžiukai-Nuliukai", "X laimėjo!\n\nNuliuk, pasistenk! X pradeda kitą žaidimą!")
            self.X_laimejimai += 1
            self.reset()

        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            laimejimas = True
            clicked = True
            messagebox.showinfo("Kryžiukai-Nuliukai",
                                "X laimėjo!\n\nSarmata, Nuliuk... \n\nnes kitą žaidimą pradeda X!")
            self.X_laimejimai += 1
            self.reset()
        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            laimejimas = True
            clicked = True
            messagebox.showinfo("Kryžiukai-Nuliukai",
                                "X laimėjo!\n\nKas čia nutiko? Nuliuk, užsisapnavai?\n\nKitą žaidimą pradeda X!")
            self.X_laimejimai += 1
            self.reset()

        # Tikrinami "O" laimėjimai:
        elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            laimejimas = True
            clicked = False
            messagebox.showinfo("Kryžiukai-Nuliukai",
                                "O laimėjo!\n\nCha-cha-cha, Kryžiuk!\n\nKitą žaidimą pradeda O!\n")
            self.O_laimejimai += 1
            self.reset()
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            laimejimas = True
            clicked = False
            messagebox.showinfo("Kryžiukai-Nuliukai", "O laimėjo!\n\nKas laimi, tas ir pradeda - O!\n")
            self.O_laimejimai += 1
            self.reset()

        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            laimejimas = True
            clicked = False
            messagebox.showinfo("Kryžiukai-Nuliukai", "O laimėjo!\n\nŽaidimą pradeda O!\n")
            self.O_laimejimai += 1
            self.reset()
        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            laimejimas = True
            clicked = False
            messagebox.showinfo("Kryžiukai-Nuliukai", "O laimėjo!\n\nKryžiuk, pasistenk! O pradeda kitą žaidimą!\n")
            self.O_laimejimai += 1
            self.reset()

        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            laimejimas = True
            clicked = False
            messagebox.showinfo("Kryžiukai-Nuliukai",
                                "O laimėjo!\n\nKryžiukas miega. Zzz...\n\n Žaidimą pradeda O!\n")
            self.O_laimejimai += 1
            self.reset()
        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            laimejimas = True
            clicked = False
            messagebox.showinfo("Kryžiukai-Nuliukai",
                                "O laimėjo!\n\nKryžiuk, užsisapnavai?\n\nKitą žaidimą pradeda O!\n")
            self.O_laimejimai += 1
            self.reset()

        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            laimejimas = True
            clicked = False
            messagebox.showinfo("Kryžiukai-Nuliukai", "O laimėjo!\n\nTodėl kitą žaidimą pradeda O!\n")
            self.O_laimejimai += 1
            self.reset()
        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            laimejimas = True
            clicked = False
            messagebox.showinfo("Kryžiukai-Nuliukai", "O laimėjo!\n\nLaimėjai, tai ir pradėk, O!\n")
            self.O_laimejimai += 1
            self.reset()

        # Tikrinamos lygiosios:
        elif self.ejimu_skaicius == 9 and laimejimas == False:
            clicked = random.choice([True, False])
            messagebox.showinfo("Kryžiukai-Nuliukai",
                                f"Lygiosios!\n\nBurtų keliu kitą ėjimą pradeda {'X' if clicked else 'O'}!\n")
            self.reset()

    # Žaidimo restartavimas. Mygtukų, ėjimų ir laimėjimo kintamųjų restartavimas:
    def reset(self):
        self.rezultatas["text"] = f"X - {self.X_laimejimai}   :   O - {self.O_laimejimai}"
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        global laimejimas
        self.ejimu_skaicius = 0
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

    # Naujas žaidimas, atliekantis restart funciją ir restartuoja rezultatų kintamuosius:
    def naujas_zaidimas(self):
        self.reset()
        self.X_laimejimai = 0
        self.O_laimejimai = 0


# Paleidžiamas žaidimas:
Zaidimas()

# Langas išlieka iki žaidimo išjungimo:
langas.mainloop()
