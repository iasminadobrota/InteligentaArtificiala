#Care este cea mai frecventa nationalitate a jucatorilor? Afisati top 5 nationalitati.
import pandas as pd
data = pd.read_csv("data.csv")

print("Cea mai frecventa nationalitate:",data["Nationality"].value_counts().idxmax())

print("Top 5 nationalitati:",data["Nationality"].value_counts().head(5))