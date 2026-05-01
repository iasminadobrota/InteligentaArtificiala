#Scalarea datelor
# Selectați variabilele numerice relevante
# Aplicați metoda StandardScaler pentru normalizarea acestora
# Comparați valorile înainte și după scalare
# Explicați de ce este necesară scalarea în contextul algoritmilor bazați pe distanță

import pandas as pd
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("StudentsPerformance.csv")

numerical_cols = ['math score', 'reading score', 'writing score']

X = df[numerical_cols]

print("=== Înainte de scalare ===")
print(X.head())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_scaled_df = pd.DataFrame(X_scaled, columns=numerical_cols)

print("\n=== După scalare ===")
print(X_scaled_df.head())

#Scalarea datelor este necesară deoarece variabilele numerice pot avea scale diferite,
# iar algoritmii bazați pe distanță (precum KNN sau K-Means) sunt sensibili la aceste
# diferențe. Dacă datele nu sunt scalate, variabilele cu valori mai mari vor influența
# disproporționat rezultatul. Prin utilizarea StandardScaler, datele sunt transformate
# astfel încât să aibă media 0 și deviația standard 1, ceea ce permite fiecărei variabile
# să contribuie în mod egal la calculul distanțelor și îmbunătățește performanța modelului.