from sklearn.datasets import load_wine

wine = load_wine()
X = wine.data
y = wine.target
feature_names = wine.feature_names
target_names = wine.target_names

print(X.shape)
print(y.shape)

print(feature_names)
print(target_names)