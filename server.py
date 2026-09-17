import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Client-Server Chat",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Client-Server Chat Application")

st.write(
    "A simple Streamlit application demonstrating "
    "client-server communication concepts."
)

# Connection status
st.success("Connected")

# Networking information
st.subheader("Networking Information")

col1, col2 = st.columns(2)

with col1:
    st.write("**Host:** localhost")
    st.write("**Port:** 8501")

with col2:
    st.write("**Protocol:** HTTP")
    st.write("**Model:** Client-Server")

st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.subheader("Chat")

# Display messages
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["text"])

# Message input
message = st.chat_input("Type your message...")

if message:
    st.session_state.messages.append({
        "role": "user",
        "text": message
    })

    st.session_state.messages.append({
        "role": "assistant",
        "text": f"Server received: {message}"
    })

    st.rerun()

st.divider()

st.caption(
    f"Last accessed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)
