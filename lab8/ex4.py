from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

wine = load_wine(as_frame=True)

X = wine.data[['alcohol', 'flavanoids']]
y = wine.target

model = DecisionTreeClassifier(
    max_depth=2,
    random_state=42
)

model.fit(X, y)

plt.figure(figsize=(10,6))

plot_tree(
    model,
    feature_names=['alcohol', 'flavanoids'],
    class_names=wine.target_names,
    filled=True
)

plt.show()

#d) Primul nod verifica o conditie, de exemplu flavanoids <= 1.58, pentru a separa cat mai bine
# clasele de vinuri. Daca conditia este adevarata, datele merg in stanga, altfel in dreapta.
#Nodurile afiseaza: gini= impuritatea, samples= numarul de exemple, class = clasa prezisa.
#Arborele foloseste alcohol si flavanoids pentru a imparti datele in grupuri cat mai pure.