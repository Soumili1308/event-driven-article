const socket = new WebSocket("ws://localhost:8000/ws");

socket.onmessage = function (event) {
  const div = document.getElementById("updates");
  div.innerHTML += `<p>${event.data}</p>`;
};
