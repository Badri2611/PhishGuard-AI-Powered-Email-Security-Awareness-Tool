import streamlit as st

# --- LOGIC SECTION (Formerly Flask) ---
def detect_phishing(email_text):
    phishing_keywords = ["urgent", "verify account", "click here", "password reset", "bank", "suspicious activity"]
    detected = [word for word in phishing_keywords if word in email_text.lower()]
    return detected if detected else None

def get_awareness_tips():
    return [
        "Always check the sender's email address before clicking any links.",
        "Avoid clicking on links in emails from unknown sources.",
        "Look for grammatical errors in emails, as phishing emails often contain them.",
        "Do not download attachments from suspicious emails.",
        "Verify URLs by hovering over links before clicking them."
    ]

# --- UI SECTION (Streamlit) ---
st.set_page_config(page_title="PhishGuard", page_icon="🛡️")

st.title("🛡️ PhishGuard: Phishing Awareness App")
st.write("Enter email text below to check for phishing indicators:")

email_text = st.text_area("Email Content:", placeholder="Paste the email body here...")

if st.button("Check for Phishing"):
    if email_text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        detected_words = detect_phishing(email_text)
        if detected_words:
            st.error(f"⚠️ Phishing Detected! High-risk keywords found: **{', '.join(detected_words)}**")
        else:
            st.success("✅ No common phishing indicators detected in this text.")

st.divider()

st.write("### 📘 Phishing Awareness Guide")
if st.button("Show Awareness Tips"):
    tips = get_awareness_tips()
    for i, tip in enumerate(tips, 1):
        st.info(f"**Tip {i}:** {tip}")
