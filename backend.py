from flask import Flask, request, jsonify
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to detect phishing keywords
def detect_phishing(email_text):
    phishing_keywords = ["urgent", "verify account", "click here", "password reset", "bank", "suspicious activity"]
    detected = [word for word in phishing_keywords if word in email_text.lower()]
    return detected if detected else None

@app.route("/check", methods=["POST"])
def check_email():
    data = request.json
    email_text = data.get("email_text", "")
    detected_words = detect_phishing(email_text)
    
    if detected_words:
        return jsonify({"phishing_detected": True, "keywords": detected_words})
    else:
        return jsonify({"phishing_detected": False, "message": "No phishing indicators detected."})

@app.route("/awareness", methods=["GET"])
def phishing_awareness():
    awareness_tips = {
        "1": "Always check the sender's email address before clicking any links.",
        "2": "Avoid clicking on links in emails from unknown sources.",
        "3": "Look for grammatical errors in emails, as phishing emails often contain them.",
        "4": "Do not download attachments from suspicious emails.",
        "5": "Verify URLs by hovering over links before clicking them."
    }
    return jsonify(awareness_tips)

if __name__ == "__main__":
    app.run(debug=True)