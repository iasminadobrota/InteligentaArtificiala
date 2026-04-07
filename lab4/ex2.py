#Afisati primii 10 jucatorii cu varsta > 40.(hint:filter)

import pandas as pd
data = pd.read_csv("data.csv")

filtered = data[data["Age"] > 40]
print(filtered[["Name", "Age"]].head(10))