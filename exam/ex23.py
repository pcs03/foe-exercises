import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./exam.csv")
print(df.head())
print(df)

df = df[(df["age"] > 20) & (df["age"] < 80)]
print(df.describe())

plt.hist(df["age"])
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Age counts")
plt.savefig("exam.png")
