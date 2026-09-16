const socket = io();

const statusSpan = document.getElementById("connection-status");
const chatBox = document.getElementById("chat-box");
const connStatusConcept = document.getElementById("conn-status-concept");

socket.on("connect", () => {
  statusSpan.textContent = "Connected";
  connStatusConcept.textContent = "Connected";
});

socket.on("disconnect", () => {
  statusSpan.textContent = "Disconnected";
  connStatusConcept.textContent = "Disconnected";
});

socket.on("message", (msg) => {
  let msgDiv = document.createElement("div");
  msgDiv.textContent = `Server/Client: ${msg}`;
  chatBox.appendChild(msgDiv);
  chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom
});

function sendMessage() {
  const input = document.getElementById("message");
  if (input.value.trim() !== "") {
    socket.send(input.value);
    input.value = "";
  }
}
