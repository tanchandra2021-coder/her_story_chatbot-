# app.py
import streamlit as st
from chatbot import *  # Import all the chatbot logic you wrote

# -------------------
# App Page Setup
# -------------------
st.set_page_config(
    page_title="Finance Leaders Chatbot",
    layout="wide"
)

st.markdown('<h1 style="text-align:center; color:#00e6ac;">💼 Finance Leaders AI Chat</h1>', unsafe_allow_html=True)

# -------------------
# Leader Selection and Chat handled in chatbot.py
# -------------------
# Your existing chatbot.py already handles:
# - Leader selection
# - Chat input
# - GPT-3.5 responses
# - Maintaining session_state messages
# So we just import it above and it will run in this app

# -------------------
# Optional: Footer / Credits
# -------------------
st.markdown("""
<div style="text-align:center; margin-top:40px; color:#aaa;">
Developed with ❤️ using Streamlit & OpenAI GPT-3.5
</div>
""", unsafe_allow_html=True)
