#6. Selectarea caracteristicilor (Feature Selection)
#Analizați fiecare coloană din dataset și decideți dacă este relevantă pentru predicția performanței academice
#Pentru fiecare coloană, justificați decizia luată (păstrată sau eliminată), având în vedere:
#dacă este un identificator
#dacă aduce informație relevantă
#dacă este redundantă
#Verificați existența:
#coloanelor constante
#coloanelor redundante (corelate puternic)
#Eliminați caracteristicile considerate irelevante.

import pandas as pd

# Încărcare date
df = pd.read_csv("StudentsPerformance.csv")

# === 1. Verificare coloane constante ===
constant_cols = [col for col in df.columns if df[col].nunique() == 1]
print("Coloane constante:", constant_cols)

# === 2. Corelații între variabile numerice ===
corr_matrix = df.select_dtypes(include=['number']).corr()

print("\n=== Matrice de corelație ===")
print(corr_matrix)

# Identificare corelații mari (>0.8)
high_corr = []
for col in corr_matrix.columns:
    for row in corr_matrix.index:
        if col != row and abs(corr_matrix.loc[row, col]) > 0.8:
            high_corr.append((row, col, corr_matrix.loc[row, col]))

print("\nCorelații puternice (>0.8):")
for item in high_corr:
    print(item)

columns_to_drop = []

columns_to_drop += constant_cols

if 'writing score' in df.columns:
    columns_to_drop.append('writing score')

columns_to_drop = list(set(columns_to_drop))

df_reduced = df.drop(columns=columns_to_drop)

print("\nColoane eliminate:", columns_to_drop)
print("\nColoane finale:", df_reduced.columns)