#Listați toate caracteristicile disponibile (feature_names).

from sklearn.datasets import load_diabetes
diabetes = load_diabetes()

print(diabetes.feature_names)

#pt ex 4:Cum putem accesa informatii statistice
# precum media, deviatia standard sau valoarea minima?
# Pentru a obține informații statistice precum media, deviația standard
# și valoarea minimă, putem folosi funcția describe() din pandas, care oferă
# un rezumat al tuturor coloanelor numerice din DataFrame.