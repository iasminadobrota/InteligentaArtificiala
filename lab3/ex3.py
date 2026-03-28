#Scrieți o funcție care normalizează datele
# dintr-o listă într-un interval [0,1].
#Funcția trebuie să accepte o listă de numere
# și să returneze lista normalizată.
#Testați funcția pe un set de date aleator.
#ex:data = [10, 20, 30, 40, 50]
#normalized_data = normalize_data(data)
#print(normalized_data)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]

import random

def normalize_data(lista):
    minim = min(lista)
    maxim = max(lista)

    rezultat = []

    for x in lista:
        valoare = (x - minim) / (maxim - minim)
        rezultat.append(valoare)

    return rezultat

data = [10, 25, 35, 40, 50] #am mai schimbat valorile sa ma asigur ca functioneaza
print("Date initiale:", data)
print("Date normalizate:", normalize_data(data))

data_random = []

for i in range(5):
    nr = random.randint(1, 100)
    data_random.append(nr)

print("\nDate initiale random:", data_random)
print("Date normalizate:", normalize_data(data_random))
