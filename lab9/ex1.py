from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
import numpy as np

mnist = fetch_openml('mnist_784', version=1)

X = mnist.data.to_numpy()
y = mnist.target.to_numpy()

X = X / 255.0

X = X.reshape(-1, 28, 28)

x_train, x_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Train:", x_train.shape)
print("Test:", x_test.shape)

print("Min:", X.min())
print("Max:", X.max())
#nu mi a mers sa intalez celalalt