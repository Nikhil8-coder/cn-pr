const socket = io();

const statusElement = document.getElementById("connection-status");
const chatBox = document.getElementById("chat-box");
const messageInput = document.getElementById("message");

// When the client connects to the server
socket.on("connect", () => {
    statusElement.textContent = "Connected";
});

// When the client disconnects from the server
socket.on("disconnect", () => {
    statusElement.textContent = "Disconnected";
});

// Receive a message from the server
socket.on("message", (message) => {
    const messageElement = document.createElement("div");

    messageElement.className = "message";
    messageElement.textContent = message;

    chatBox.appendChild(messageElement);

    // Automatically scroll to the latest message
    chatBox.scrollTop = chatBox.scrollHeight;
});

// Send a message to the server
function sendMessage() {
    const message = messageInput.value.trim();

    if (message === "") {
        return;
    }

    socket.send(message);
    messageInput.value = "";
    messageInput.focus();
}

// Send message when Enter is pressed
messageInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        sendMessage();
    }
});
