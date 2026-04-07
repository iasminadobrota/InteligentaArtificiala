#Filtrați jucătorii care au contractul până în 2021
import pandas as pd
data = pd.read_csv("data.csv")

filtered = data[data["Contract Valid Until"] == 2021.0]
print(data[data["Contract Valid Until"].astype(str) == "2021"][["Name", "Contract Valid Until"]])