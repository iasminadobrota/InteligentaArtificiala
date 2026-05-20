from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

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

model = MLPClassifier(
    hidden_layer_sizes=(128,),
    activation='relu',
    max_iter=20
)

model.fit(x_train, y_train)

index = 0

image = x_test[index]

prediction = model.predict([image])

plt.imshow(image.reshape(28, 28), cmap='gray')

plt.title(f"Predicție: {prediction[0]}")
plt.axis('off')

plt.show()