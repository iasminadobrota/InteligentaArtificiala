#Creati o histograma pentru caracteristica BMI.

from sklearn.datasets import load_diabetes
import pandas as pd
import matplotlib.pyplot as plt
diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

df["bmi"].hist()

plt.show()