import pandas as pd

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

print("Fake rows:", len(fake))
print("True rows:", len(true))

print("\nFirst 5 Fake labels:")
print(fake.head())

print("\nFirst 5 True labels:")
print(true.head())