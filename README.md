# 📰 Fake News Detection using Machine Learning

## 📌 Overview

This project is a Fake News Detection web application developed using Python, Machine Learning, and Flask. It predicts whether a news article is **REAL** or **FAKE** by analyzing its text content.

The model is trained on real-world news datasets using Natural Language Processing (NLP) techniques and can classify news articles entered by users through a web interface.

---

## 🚀 Features

- Detects whether a news article is **REAL** or **FAKE**
- User-friendly Flask web interface
- Machine Learning-based prediction
- Text preprocessing using NLP
- TF-IDF Vectorization
- High prediction accuracy
- Easy to use and deploy

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Joblib
- HTML
- CSS

---

## 📂 Project Structure

```
Fake_News_Detection/
│
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── fake_news_model.pkl
├── vectorizer.pkl
└── screenshots/
```

---

## 📊 Dataset

This project uses the Fake and True News datasets from Kaggle.

Download the dataset here:

https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

Files:

- Fake.csv
- True.csv

> These dataset files are not included in this repository because of GitHub's file size limits.

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Fake_News_Detection.git
```

Go to the project folder

```bash
cd Fake_News_Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train the model

```bash
python train_model.py
```

Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 💡 How It Works

1. User enters a news article.
2. The text is cleaned and preprocessed.
3. TF-IDF converts the text into numerical features.
4. The trained Passive Aggressive Classifier predicts the result.
5. The application displays whether the news is REAL or FAKE.

---

## 📸 Screenshots

### Home Page

<img width="1920" height="1080" alt="Screenshot (17)" src="https://github.com/user-attachments/assets/53bc47b8-f953-40c9-a07d-ba09aae958d6" />


### Prediction Result

<img width="1920" height="1080" alt="Screenshot (18)" src="https://github.com/user-attachments/assets/83f27ad1-693b-4e08-9ed6-e0040e5cfe70" />


## 📈 Future Improvements

- Integrate BERT/DistilBERT for better prediction.
- Add confidence score.
- Verify news using trusted news APIs.
- Support multiple languages.
- Deploy on Render or Hugging Face Spaces.
- Add explainable AI (why the model predicted REAL or FAKE).

---

## 👩‍💻 Author

**Harshini Vennamaneni**

GitHub:
https://github.com/harshinivennamaneni58725

---

## ⭐ If you like this project

Please ⭐ this repository and feel free to contribute.
