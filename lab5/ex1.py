#1. Explorarea datelor
#Încărcați setul de date într-un DataFrame Pandas
#Afișați primele 5 înregistrări
#Analizați structura dataset-ului (tipuri de date, număr de valori non-null)
#Calculați statistici descriptive pentru variabilele numerice
#Identificați eventualele valori lipsă

import pandas as pd
df = pd.read_csv("StudentsPerformance.csv")

print("=== Primele 5 înregistrări ===")
print(df.head())

print("\n=== Dimensiunea dataset-ului ===")
print(df.shape)

print("\n=== Numele coloanelor ===")
print(df.columns)

print("\n=== Informații generale ===")
print(df.info())

print("\n=== Statistici descriptive ===")
print(df.describe())

print("\n=== Valori lipsă pe fiecare coloană ===")
print(df.isnull().sum())

print("\n=== Număr de valori unice pe coloană ===")
print(df.nunique())