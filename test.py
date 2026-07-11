import joblib

model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

real_news = """
The Reserve Bank of India announced that the repo rate will remain unchanged after the latest monetary policy meeting.
"""

fake_news = """
NASA has confirmed that dinosaurs are living on the Moon and will visit Earth next week.
"""

for text in [real_news, fake_news]:
    x = vectorizer.transform([text])
    print(model.predict(x)[0])