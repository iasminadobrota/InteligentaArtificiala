#8.Regresie pe două caracteristici (bmi și bp):
#a)Selectați bmi și bp ca input (X).
#b)Antrenați un nou model de regresie liniară folosind aceste două caracteristici.
#c)Afișați coeficienții modelului pentru fiecare caracteristică.
#d)Calculați scorul R² al modelului pe setul de testare.

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df["target"] = diabetes.target

#a)
X = df[["bmi", "bp"]]
y = df["target"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#b)
model = LinearRegression()
model.fit(X_train, y_train)

#c)
print("Coeficient bmi:", model.coef_[0])
print("Coeficient bp:", model.coef_[1])

#d)
r2 = model.score(X_test, y_test)
print("R^2:", r2)