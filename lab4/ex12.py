#Câți jucători au o valoare de transfer mai mare decât salariul?

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

result = data[data["Value_num"] > data["Wage_num"]]

print("Numarul jucatorilor cu valoarea de transfer mai mare decat salariul:",len(result))