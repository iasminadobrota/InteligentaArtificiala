#Afisati cate randuri si coloane are setul de date. Cati jucatori unici avem?

import pandas as pd
data = pd.read_csv("data.csv")

print("Randuri:", data.shape[0])
print("Coloane:", data.shape[1])

print("Jucatori unici:", data["Name"].nunique())