#Creati un joc Rock-Paper-Scissors pentru doi jucatori.
# (Hint: Solicitati selectia jucatorilor (folosind input),
# comparati alegerile lor, afisati un mesaj de felicitari pentru castigator
# si intreabati  daca jucatorii doresc sa inceapa un nou joc).
#Tine minte regulile:
#Piatra bate foarfeca
#Foarfeca taie hartia
#Hartia bate piatra

print("Joc: Piatra - Hartie - Foarfeca\n")

joc = True

while joc:
    j1 = input("Jucator 1 (piatra/hartie/foarfeca): ")
    j2 = input("Jucator 2 (piatra/hartie/foarfeca): ")

    if j1 == j2:
        print("Egalitate!")

    elif (j1 == "piatra" and j2 == "foarfeca") or \
            (j1 == "foarfeca" and j2 == "hartie") or \
            (j1 == "hartie" and j2 == "piatra"):
        print("Jucatorul 1 castiga!")

    else:
        print("Jucatorul 2 castiga!")

    raspuns = input("Vreti sa mai jucati? (da/nu): ")
    if raspuns == "nu":
        joc = False

print("Joc terminat!")
