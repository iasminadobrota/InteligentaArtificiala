from sklearn.datasets import load_wine

wine = load_wine(as_frame=True)
df = wine.frame

print(df.head())