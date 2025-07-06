from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def home():
    return "Bias Analyzer API is running ✅"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "No text provided"}), 400

    # تحلیل ساده: اگر متن خیلی منفی یا خیلی مثبت باشه → ممکنه bias داشته باشه
    polarity = TextBlob(text).sentiment.polarity
    subjectivity = TextBlob(text).sentiment.subjectivity

    result = {
        "text": text,
        "polarity": polarity,
        "subjectivity": subjectivity,
        "bias_score": round(abs(polarity) * subjectivity, 2)
    }

    return jsonify(result)
