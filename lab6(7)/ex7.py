#.Regresie liniară simplă folosind bmi:
#a)Selectați doar coloana bmi ca input (X) și scorul diabetului ca target (y).
#b)Împărțiți datele în set de antrenare și set de testare (80%-20%).
#c)Antrenați un model de regresie liniară folosind datele de antrenare.
#d)Reprezentați grafic datele de testare și linia de regresie.
#e)Calculați eroarea pătratică medie (MSE) folosind datele de testare (y_test și y_pred).

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt

diabetes = load_diabetes()


df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df["target"] = diabetes.target

#a)
X = df[["bmi"]]
y = df["target"]

#b)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#c)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

#d)
plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred)
plt.xlabel("BMI")
plt.ylabel("Target")
plt.title("Regresie liniară BMI vs Target")
plt.show()

#e)
mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)