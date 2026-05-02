#Creati graficul pentru BMI și vârstă în funcție de variabila țintă.
from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt

diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df["target"] = diabetes.target

plt.scatter(df["bmi"], df["target"])
plt.xlabel("BMI")
plt.ylabel("Target")
plt.title("BMI vs Target")
plt.show()

plt.scatter(df["age"], df["target"])
plt.xlabel("Age")
plt.ylabel("Target")
plt.title("Age vs Target")
plt.show()