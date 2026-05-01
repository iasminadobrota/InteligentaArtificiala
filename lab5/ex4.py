#Transformarea variabilelor categoriale (Encoding)
#Identificați variabilele categoriale
#Aplicați:
#Label Encoding pentru o variabilă binară
#One-Hot Encoding pentru celelalte variabile categorice
#Explicați alegerea metodelor utilizate

import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("StudentsPerformance.csv")

categorical_cols = df.select_dtypes(include=['object', 'string']).columns

print("Variabile categorice:", list(categorical_cols))

binary_col = None
for col in categorical_cols:
    if df[col].nunique() == 2:
        binary_col = col
        break

if binary_col is not None:
    print(f"\nVariabilă binară aleasă pentru Label Encoding: {binary_col}")
    le = LabelEncoder()
    df[binary_col] = le.fit_transform(df[binary_col])
else:
    print("\nNu există variabile binare în dataset.")

other_categorical = [col for col in categorical_cols if col != binary_col]

df = pd.get_dummies(df, columns=other_categorical, drop_first=True)

print("\n=== Primele 5 rânduri după encoding ===")
print(df.head())

print("\n=== Coloane după encoding ===")
print(df.columns)

# am folosit Label encoding pentru variabila binara fiindca are doar doua valori si
# poate fi reprezentata simplu ca 0 și 1, iar pentru celelalte variabile
# am ales One-Hot Encoding deoarece nu au o ordine naturala
# si astfel evitam ca modelul sa interpreteze gresit relatii intre categorii