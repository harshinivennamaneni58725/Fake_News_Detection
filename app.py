from flask import Flask,render_template,request
from predict import detect_news

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():

    news = request.form["news"]

    result = detect_news(news)

    return render_template(
        "index.html",
        prediction=result,
        news=news
    )

if __name__=="__main__":
    app.run(debug=True)