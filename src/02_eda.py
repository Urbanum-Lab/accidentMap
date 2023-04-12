import pandas as pd

df = pd.read_csv("data/interim/cleaned.csv")
print(df.columns)
for col in df.columns:
    print(len(set(df[col])), set(df[col]))

