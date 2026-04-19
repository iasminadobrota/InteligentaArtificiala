#Creati un grafic pentru a vizualiza mai bine datele.(seaborn scatterplot)

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

def convert_money(x):
    x = str(x).replace('€', '')
    if 'M' in x:
        return float(x.replace('M', '')) * 1_000_000
    elif 'K' in x:
        return float(x.replace('K', '')) * 1_000
    return float(x)

data["Value_num"] = data["Value"].apply(convert_money)
data["Wage_num"] = data["Wage"].apply(convert_money)

plt.figure(figsize=(10, 6))

plt.scatter(data["Wage_num"], data["Value_num"])

plt.xlabel("Wage (€)")
plt.ylabel("Value (€)")
plt.title("Wage vs Value")

plt.show()