import random

numar_secret=random.randint(1,50)
incercari=0

print("Am ales un numar intre 1 si 50.")

while True:
    ghicire=int(input("Ghiceste numarul intre 1-50: "))
    incercari +=1

    if ghicire<numar_secret:
        print("Numarul este mai mare")
    elif ghicire >numar_secret:
        print("Numarul este mai mic")
    else:
        print(f"Felicitari, ai ghicit numarul in {incercari} incercari")

