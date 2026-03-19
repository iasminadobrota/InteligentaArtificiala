import random
print("Bine ai venit la Loteria Python!\n")

numere = []
i = 0
while i < 6:
    nr = int(input("Introdu un numar intre 1 si 49: "))

    if 1 <= nr <= 49:
        numere.append(nr)
        i = i + 1
    else:
        print("Numar invalid!")
extrase = random.sample(range(1, 50), 6)
ghicite = []
i = 0

while i < 6:
    if numere[i] in extrase:
        ghicite.append(numere[i])
    i = i + 1
print("Numerele tale:", numere)
print("Numere extrase:", extrase)
print("Ai ghicit", len(ghicite), "numere:", ghicite)

if len(ghicite) >= 3:
    print("Felicitari! Ai castigat!")
else:
    print("Mai incearca!")