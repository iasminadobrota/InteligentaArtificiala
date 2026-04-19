#Care jucatori reprezinta o “afacere buna”?
#Afisati doar coloanele Name, Wage, Value intr-un nou df.
#Adaugati o noua coloana “difference” in care sa calculati diferenta
# dintre value(current market value) si wage(current wage).
#Afisati jucatorii in ordine descrescatoare, de la cea mare diferenta la cea mai mica.

import pandas as pd
data = pd.read_csv("data.csv")

def convert_money(x):
    x = str(x).replace('€', '')
    if 'M' in x:
        return float(x.replace('M', '')) * 1_000_000
    elif 'K' in x:
        return float(x.replace('K', '')) * 1_000
    else:
        return float(x)

data["Value_num"] = data["Value"].apply(convert_money)
data["Wage_num"] = data["Wage"].apply(convert_money)

df = data[["Name", "Wage", "Value"]].copy()

df["difference"] = data["Value_num"] - data["Wage_num"]

df = df.sort_values(by="difference", ascending=False)

print(df.head(10))