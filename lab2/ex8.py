print("Verificare tranzactie\n")

suma = int(input("Introdu suma tranzactiei: "))
tara = input("Introdu tara: ")
nr_tranzactii = int(input("Cate tranzactii ai facut intr-un minut? "))

tari_risc = ["Coreea de Nord", "Siria", "Iran"]

suspect = False

if suma > 10000:
    print("Suma mare!")
    suspect = True

for t in tari_risc:
    if tara == t:
        print("Tara cu risc ridicat!")
        suspect = True

if nr_tranzactii > 3:
    print("Activitate suspecta (posibil bot)!")
    suspect = True

if suspect:
    print("Tranzactie suspecta!")
else:
    print("Tranzactie sigura.")