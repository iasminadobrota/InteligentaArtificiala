from sklearn.neural_network import MLPClassifier

model = MLPClassifier(
    hidden_layer_sizes=(128,),
    activation='relu',
    max_iter=10
)

print(model)