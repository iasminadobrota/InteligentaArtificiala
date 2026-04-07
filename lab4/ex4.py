#Sortează jucătorii după Skill Moves descrescător

import pandas as pd
data = pd.read_csv("data.csv")

sorted_data = data.sort_values(by="Skill Moves", ascending=False)
print(data.sort_values(by="Skill Moves", ascending=False)[["Name", "Skill Moves"]])