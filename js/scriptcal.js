function responder() {
    const input = document.getElementById("userInput").value.trim();
    const respuesta = document.getElementById("respuestaBot");
  
    if (input === "") {
      respuesta.textContent = "Por favor, escribe algo.";
    } else {
      respuesta.textContent = "Gracias por tu pregunta. Te responderemos pronto.";
    }
  }
  
  function toggleChatbot() {
    const chatbot = document.getElementById("chatbot-box");
    chatbot.style.display = chatbot.style.display === "block" ? "none" : "block";
  }