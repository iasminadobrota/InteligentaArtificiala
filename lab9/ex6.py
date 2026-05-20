from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

mnist = fetch_openml('mnist_784', version=1)

X = mnist.data.to_numpy()
y = mnist.target.to_numpy()

X = X / 255.0

x_train, x_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

epoci = [5, 10, 20, 50]

for e in epoci:

    print(f"\nModel cu {e} epoci")

    model = MLPClassifier(
        hidden_layer_sizes=(128,),
        activation='relu',
        max_iter=e
    )

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)

    print("Accuracy:", accuracy)