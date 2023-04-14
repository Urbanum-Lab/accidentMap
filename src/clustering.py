import pandas as pd
from sklearn import preprocessing

df = pd.read_csv("data/interim/cleaned.csv")

le = preprocessing.LabelEncoder()
encoded = le.fit_transform(df["Baleset típus"])
labels = list(set(encoded))
id2label = dict(zip(labels, le.inverse_transform(labels)))
id2label = {int(k): v for k, v in id2label.items()}
label2id = {v: k for k, v in id2label.items()}

for k in id2label:
    print(type(k))