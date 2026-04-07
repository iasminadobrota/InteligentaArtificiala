#Afișați toți jucătorii cu Overall ≥ 85 și Age < 25

import pandas as pd
data = pd.read_csv("data.csv")

filtered = data[(data["Overall"] >= 85) & (data["Age"] < 25)]
print(filtered[["Name", "Overall", "Age"]])