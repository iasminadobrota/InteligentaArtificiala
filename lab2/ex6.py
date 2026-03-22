print("Bine ai venit in padurea magica!\n")

inventar = []
joc = True

while joc:
    alegere = input("Mergi la stanga sau la dreapta? ")

    if alegere == "stanga":
        print("Ai intalnit un lup! 🐺")

        actiune = input("Fugi sau lupti? (raspunde cu fugi sau lupti)")

        if actiune == "fugi":
            print("Ai scapat!")
        elif actiune == "lupti":
            print("Ai invins lupul!")
            inventar.append("blana de lup")
        else:
            print("Actiune invalida!")

    elif alegere == "dreapta":
        print("Ai gasit o comoara! 💰")
        inventar.append("aur")

    else:
        print("Directie invalida!")

    print("Inventar:", inventar)

    continua = input("Vrei sa continui? (da/nu) ")
    if continua == "nu":
        joc = False

print("Joc terminat!")