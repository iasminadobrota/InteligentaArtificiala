#Aflați care club are cea mai mare medie de Overall.

import pandas as pd
data = pd.read_csv("data.csv")

club_mean = data.groupby("Club")["Overall"].mean()
print("Clubul care are cea mai mare medie de Overall:",club_mean.idxmax(), club_mean.max())