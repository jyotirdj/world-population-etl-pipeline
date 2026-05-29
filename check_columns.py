import pandas as pd

df = pd.read_csv("world_population.csv")
print(df.columns.tolist())
print(df.head(2))
