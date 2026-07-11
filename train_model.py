import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score

# Load datasets
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# Add labels
fake["label"] = "FAKE"
true["label"] = "REAL"

# Keep only text and label
fake = fake[["text", "label"]]
true = true[["text", "label"]]

# Merge datasets
df = pd.concat([fake, true], ignore_index=True)

# Shuffle
df = df.sample(frac=1, random_state=42)

X = df["text"]
y = df["label"]

# TF-IDF
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)

X = vectorizer.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train
model = PassiveAggressiveClassifier(max_iter=1000)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("Accuracy :", accuracy)

joblib.dump(model, "fake_news_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model Saved Successfully")