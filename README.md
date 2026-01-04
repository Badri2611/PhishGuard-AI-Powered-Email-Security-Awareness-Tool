# 🛡️ PhishGuard

PhishGuard is a lightweight cybersecurity tool designed to detect common phishing indicators in email text and provide users with actionable security awareness tips. It utilizes a **Flask REST API** for backend analysis and a **Streamlit** dashboard for an intuitive user experience.

## ✨ Features
- **Phishing Detection:** Scans email content for high-risk keywords used by cybercriminals.
- **Real-time API Analysis:** Processes data through a dedicated Flask backend.
- **Awareness Guide:** Provides an interactive list of best practices to stay safe from social engineering attacks.
- **Cross-Platform:** Accessible via a web interface powered by Streamlit.

## 🛠️ Tech Stack
- **Backend:** Python, Flask, Flask-CORS
- **Frontend:** Streamlit
- **Communication:** REST API (JSON)
- **Deployment:** Streamlit Cloud / Localhost

## 📂 Project Structure
```text
├── backend.py             # Flask Backend API
├── frontend.py              # Streamlit Frontend 
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
