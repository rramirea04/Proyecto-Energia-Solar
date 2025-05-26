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


  //contenido jacript para la calculadora//

  document.getElementById('calcular-btn').addEventListener('click', () => {
    const consumo = parseFloat(document.getElementById('consumo').value);
    const tipo = document.getElementById('tipo-energia').value;
  
    if (isNaN(consumo) || !tipo) {
      alert('Por favor complete todos los campos');
      return;
    }
  
    // Cálculos ficticios (puedes ajustar con tus fórmulas reales)
    let ahorroKwh = 0;
    let ahorroCO2 = 0;
    let ahorroUSD = 0;
  
    switch (tipo) {
      case 'solar':
        ahorroKwh = consumo * 0.4;
        break;
      case 'eolica':
        ahorroKwh = consumo * 0.5;
        break;
      case 'hidrogeno':
        ahorroKwh = consumo * 0.6;
        break;
    }
  
    ahorroCO2 = ahorroKwh * 0.5;
    ahorroUSD = ahorroKwh * 0.12;
  
    // Insertar valores en el DOM
    document.getElementById('ahorro-kwh').textContent = ahorroKwh.toFixed(2);
    document.getElementById('ahorro-co2').textContent = ahorroCO2.toFixed(2);
    document.getElementById('ahorro-usd').textContent = ahorroUSD.toFixed(2);
  
    // Mostrar resultados
    document.getElementById('resultados').classList.remove('hidden');
  });
  