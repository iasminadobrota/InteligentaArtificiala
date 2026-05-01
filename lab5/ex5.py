#5. Crearea de caracteristici noi (Feature Engineering)
# Creați o variabilă nouă average_score ca medie a scorurilor la:
# matematică
# citire
# scriere
# Creați o variabilă categorială performance_level, astfel:
# „low” pentru valori sub 50
# „medium” pentru valori între 50 și 70
# „high” pentru valori peste 70
# Creați o variabilă binară is_prepared, pe baza variabilei „test preparation course”
# Justificați utilitatea caracteristicilor create

import pandas as pd
df = pd.read_csv("StudentsPerformance.csv")

df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

def performance_level(avg):
    if avg < 50:
        return "low"
    elif avg <= 70:
        return "medium"
    else:
        return "high"

df['performance_level'] = df['average_score'].apply(performance_level)

df['is_prepared'] = df['test preparation course'].apply(lambda x: 1 if x == 'completed' else 0)

print(df[['average_score', 'performance_level', 'is_prepared']].head())

#Am creat variabila average_score pentru a avea o măsură generală a performanței elevului,
# combinând toate scorurile într-o singură valoare ușor de analizat.
# Variabila performance_level ajută la interpretarea mai simplă a rezultatelor,
# transformând valorile numerice în categorii (low, medium, high), ceea ce face
# analiza mai intuitivă. Variabila binară is_prepared simplifică informația despre
# participarea la cursul de pregătire, fiind utilă pentru modele de machine learning
# care funcționează mai bine cu valori numerice.