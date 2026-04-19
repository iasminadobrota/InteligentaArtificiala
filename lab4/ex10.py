#Completați valorile lipsă din coloana 'Position' cu stringul "Unknown".

import pandas as pd
data = pd.read_csv("data.csv")

print("Valori lipsa inainte:", data["Position"].isna().sum())
data["Position"] = data["Position"].fillna("Unknown")

print("Valori lipsa dupa:", data["Position"].isna().sum())
print(data[["Name", "Position"]].head(10))

data.to_csv("data_fara_nan.csv", index=False)