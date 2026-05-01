#2. Identificarea tipurilor de variabile Determinați:
#variabilele categorice
#variabilele numerice
#Enumerați fiecare categorie identificată

import pandas as pd
df = pd.read_csv("StudentsPerformance.csv")

categorical_cols = df.select_dtypes(include=['object']).columns

numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

print("=== Variabile categorice ===")
for col in categorical_cols:
    print(f"- {col}")

print("\n=== Variabile numerice ===")
for col in numerical_cols:
    print(f"- {col}")

print("\n=== Categorii pentru fiecare variabilă categorică ===")
for col in categorical_cols:
    print(f"\n{col}:")
    print(df[col].unique())