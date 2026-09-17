import streamlit as st
from datetime import datetime

# ---------------------------------------------------------
# CLIENT-SERVER CHAT APPLICATION
# Built using Streamlit
# ---------------------------------------------------------

st.set_page_config(
    page_title="Client-Server Chat",
    page_icon="💬",
    layout="centered"
)

# ---------------------------------------------------------
# APPLICATION TITLE
# ---------------------------------------------------------

st.title("💬 Client-Server Chat Application")

st.write(
    "A simple project demonstrating the basic "
    "Client-Server communication model."
)

# ---------------------------------------------------------
# SERVER INFORMATION
# ---------------------------------------------------------

st.subheader("🌐 Server Information")

col1, col2 = st.columns(2)

with col1:
    st.write("**Server:** Streamlit Cloud")
    st.write("**Host:** Online Server")

with col2:
    st.write("**Protocol:** HTTPS")
    st.write("**Model:** Client-Server")

st.divider()

# ---------------------------------------------------------
# CONNECTION STATUS
# ---------------------------------------------------------

st.subheader("🔌 Connection Status")

st.success("Client Connected to Server")

st.divider()

# ---------------------------------------------------------
# CHAT HISTORY
# ---------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

st.subheader("💬 Chat")

# Display previous messages
for message in st.session_state.messages:

    if message["sender"] == "Client":
        with st.chat_message("user"):
            st.write(message["text"])
            st.caption(message["time"])

    else:
        with st.chat_message("assistant"):
            st.write(message["text"])
            st.caption(message["time"])


# ---------------------------------------------------------
# CLIENT MESSAGE
# ---------------------------------------------------------

message = st.chat_input("Type your message...")

if message:

    current_time = datetime.now().strftime("%H:%M:%S")

    # Client sends message to server
    st.session_state.messages.append(
        {
            "sender": "Client",
            "text": message,
            "time": current_time
        }
    )

    # Server receives and responds
    st.session_state.messages.append(
        {
            "sender": "Server",
            "text": f"Server received: {message}",
            "time": current_time
        }
    )

    st.rerun()


# ---------------------------------------------------------
# NETWORKING CONCEPTS
# ---------------------------------------------------------

st.divider()

st.subheader("📡 Networking Concepts")

st.markdown(
    """
    **Client:**  
    The browser/user sends a message to the application.

    **Server:**  
    The Streamlit application receives and processes the message.

    **Communication:**  
    The client sends a request and the server processes it.

    **Protocol:**  
    HTTPS is used for communication between the browser
    and the deployed Streamlit application.

    **Client-Server Model:**

    ```
    Client
       |
       |  Message
       ↓
    Streamlit Server
       |
       |  Response
       ↓
    Client
    ```
    """
)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "Client-Server Chat Application | "
    "Built with Python and Streamlit"
)
