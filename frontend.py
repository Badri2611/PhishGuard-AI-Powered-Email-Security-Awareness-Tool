import streamlit as st
import requests

st.title("Phishing Awareness App")
st.write("Enter email text below to check for phishing indicators:")

email_text = st.text_area("Email Content:")

if st.button("Check for Phishing"):
    response = requests.post("http://127.0.0.1:5000/check", json={"email_text": email_text})
    result = response.json()
    
    if result["phishing_detected"]:
        st.error(f"Phishing Detected! Keywords: {', '.join(result['keywords'])}")
    else:
        st.success(result["message"])

st.write("### Phishing Awareness Guide")
if st.button("Show Awareness Tips"):
    awareness_response = requests.get("http://127.0.0.1:5000/awareness")
    tips = awareness_response.json()
    for key, tip in tips.items():
        st.write(f"{key}. {tip}")