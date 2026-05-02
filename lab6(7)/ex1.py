#Încărcați setul de date diabetes folosind scikit-learn

from sklearn.datasets import load_diabetes
diabetes = load_diabetes()

X = diabetes.data

y = diabetes.target

print("Shape X:", X.shape)
print("Shape y:", y.shape)
print("Feature names:", diabetes.feature_names)
