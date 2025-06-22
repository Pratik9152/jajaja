
import streamlit as st
from backend.chat_logic import get_response
from admin.uploader import upload_pdf
import time
import os

st.set_page_config(page_title="Payroll Assistant", layout="wide")

st.markdown("""
    <style>
    .chat-bubble {
        background-color: #1e40af;
        color: white;
        padding: 1rem;
        border-radius: 1rem;
        margin-bottom: 1rem;
        animation: fadeIn 0.4s ease-in-out;
    }
    .user-bubble {
        background-color: #0f766e;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
"", unsafe_allow_html=True)

st.title("💼 Payroll Assistant Chatbot")

# Admin Panel
with st.sidebar:
    st.header("🔐 Admin Panel")
    upload_pdf()

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat Input
user_input = st.chat_input("Type your payroll question here...")

if user_input:
    with st.spinner("Payroll Assistant is thinking..."):
        response = get_response(user_input)
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("bot", response))

# Display Chat
for role, message in st.session_state.chat_history:
    css_class = "user-bubble" if role == "user" else "chat-bubble"
    st.markdown(f"<div class='{css_class} chat-bubble'>{message}</div>", unsafe_allow_html=True)
