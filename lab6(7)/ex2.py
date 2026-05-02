#Afișați primele 5 rânduri într-un DataFrame Pandas

from sklearn.datasets import load_diabetes
import pandas as pd

diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

df["target"] = diabetes.target

print(df.head())