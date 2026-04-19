#Creați o coloană nouă “is_underpaid” care este True dacă Wage < Value / 100.

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

data["is_underpaid"] = data["Wage_num"] < (data["Value_num"] / 100)

print(data[["Name", "Value", "Wage", "is_underpaid"]].head(10))