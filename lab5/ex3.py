#3. Curățarea datelor
#Verificați existența valorilor lipsă
#Dacă există:
#înlocuiți valorile numerice lipsă cu mediana
#înlocuiți valorile categorice lipsă cu „Unknown”
#Verificați din nou dataset-ul pentru a confirma eliminarea valorilor lipsă

import pandas as pd
df = pd.read_csv("StudentsPerformance.csv")

categorical_cols = df.select_dtypes(include=['object', 'string']).columns
numerical_cols = df.select_dtypes(include=['number']).columns

print("=== Valori lipsă ÎNAINTE de curățare ===")
print(df.isnull().sum())

for col in numerical_cols:
    median_value = df[col].median()
    df[col] = df[col].fillna(median_value)

for col in categorical_cols:
    df[col] = df[col].fillna("Unknown")

print("\n=== Valori lipsă DUPĂ curățare ===")
print(df.isnull().sum())

print("\nMai există valori lipsă în dataset?")
print(df.isnull().values.any())