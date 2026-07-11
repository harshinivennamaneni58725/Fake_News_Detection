import joblib

model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def detect_news(news):

    data = vectorizer.transform([news])

    prediction = model.predict(data)

    return prediction[0]