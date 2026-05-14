from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

wine = load_wine()

X = wine.data
y = wine.target

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

importance = pd.DataFrame({
    'Feature': wine.feature_names,
    'Importance': model.feature_importances_
})

importance = importance.sort_values(
    by='Importance',
    ascending=False
)

print(importance)

#Caracteristicile cu valori mai mari in feature_importances_ influenteaza mai mult
#deciziile arborelui. In general, flavanoids, proline si color_intensity sunt printre cele
#mai importante caracteristici pentru clasificarea vinurilor.