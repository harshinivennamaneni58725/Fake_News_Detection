import pandas as pd

true = pd.read_csv("True.csv")
fake = pd.read_csv("Fake.csv")

print("===== FIRST REAL ARTICLE =====\n")
print(true.iloc[0]["text"])

print("\n\n===== FIRST FAKE ARTICLE =====\n")
print(fake.iloc[0]["text"])