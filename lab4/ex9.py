#Calculați media atributelor ‘SprintSpeed’ și ‘Acceleration’
# pentru fiecare naționalitate. (groupby("Nationality"))

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("data.csv")

top5 = data["Nationality"].value_counts().head(5)

plt.figure()
plt.pie(top5, labels=top5.index, autopct='%1.1f%%')
plt.title("Top 5 nationalitati - proportia jucatorilor")

plt.show()
