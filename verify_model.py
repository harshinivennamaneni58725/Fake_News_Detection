import pandas as pd
import joblib

# Load model
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Load datasets
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# Test first fake article
fake_text = fake.iloc[0]["text"]
fake_prediction = model.predict(vectorizer.transform([fake_text]))[0]

# Test first real article
true_text = true.iloc[0]["text"]
true_prediction = model.predict(vectorizer.transform([true_text]))[0]

print("Fake Article Prediction :", fake_prediction)
print("Real Article Prediction :", true_prediction)