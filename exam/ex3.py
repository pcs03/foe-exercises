import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./exam.csv", index_col=False)
cond = df["sex"] == "male"
df = df.drop(df[cond].index)
print(df.head())

plt.scatter(df["sibsp"], df["embarked"])
plt.savefig("./fig.png")
