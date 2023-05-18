from tkinter import Tk, Button, Label

def vali_raskusaste(raskusaste):
    if raskusaste == "kerge":
        print("Valitud on kerge tase.")
    elif raskusaste == "keskmine":
        print("Valitud on keskmine tase.")
    elif raskusaste == "raske":
        print("Valitud on raske tase.")
    elif raskusaste == "jatka":
        salvestatud_tulemus = loe_salvestatud_tulemus("salvestatud_tulemus.txt")
        print("Jätkame pooleliolevat mängu:")
        print(salvestatud_tulemus)

def loe_salvestatud_tulemus(failinimi):
    with open(failinimi, 'r') as fail:
        tulemused = []
        for rida in fail:
            rida = rida.strip().split('|')
            kasutaja = rida[0]
            aeg = rida[1]
            kpv = rida[2]
            tulemused.append((kasutaja, aeg, kpv))
        sorteeritud = sorted(tulemused, key=lambda x: x[1])
    return sorteeritud

def loo_menuu():
    def vali_kerge():
        vali_raskusaste("kerge")

    def vali_keskmine():
        vali_raskusaste("keskmine")

    def vali_raske():
        vali_raskusaste("raske")

    def vali_jatka():
        vali_raskusaste("jatka")

    aknake = Tk()
    aknake.title("Sudoku Menüü")

    pealkiri_silt = Label(aknake, text="Vali raskusaste:")
    pealkiri_silt.pack()

    kerge_nupp = Button(aknake, text="Kerge", command=vali_kerge)
    kerge_nupp.pack()

    keskmine_nupp = Button(aknake, text="Keskmine", command=vali_keskmine)
    keskmine_nupp.pack()

    raske_nupp = Button(aknake, text="Raske", command=vali_raske)
    raske_nupp.pack()

    jatka_nupp = Button(aknake, text="Jätka mängu", command=vali_jatka)
    jatka_nupp.pack()

    aknake.mainloop()

#loo_menuu()
