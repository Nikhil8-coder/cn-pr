from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)

# Secret key used by Flask
app.config["SECRET_KEY"] = "chat-secret-key"

# Initialize Socket.IO
socketio = SocketIO(app)


@app.route("/")
def index():
    """Display the chat application."""
    return render_template("index.html")


@socketio.on("message")
def handle_message(message):
    """Receive and broadcast a message to all connected clients."""
    print(f"Message received: {message}")

    # Broadcast the message to all connected clients
    send(message, broadcast=True)


if __name__ == "__main__":
    print("Client-Server Chat Server")
    print("Server running at: http://localhost:5000")

    socketio.run(
        app,
        host="0.0.0.0",
        port=5000,
        debug=True
    )
