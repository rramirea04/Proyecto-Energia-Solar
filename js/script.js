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
  document.addEventListener("DOMContentLoaded", function () {
    const calcularBtn = document.getElementById("calcular-btn");
    const consumoInput = document.getElementById("consumo");
    const tipoEnergiaSelect = document.getElementById("tipo-energia");
    const resultadosSection = document.getElementById("resultados");
    const ahorrokwhSpan = document.getElementById("ahorro-kwh");
    const ahorroCo2Span = document.getElementById("ahorro-co2");
    const ahorroUsdSpan = document.getElementById("ahorro-usd");

    calcularBtn.addEventListener("click", function () {
        const consumo = parseFloat(consumoInput.value);
        const tipoEnergia = tipoEnergiaSelect.value.toLowerCase();

        if (isNaN(consumo) || consumo <= 0) {
            alert("Por favor, ingrese un consumo válido mayor a cero");
            return;
        }

        let factorAhorro;
        switch (tipoEnergia) {
            case "solar":
                factorAhorro = 0.2;
                break;
            case "eólica":
                factorAhorro = 0.25;
                break;
            case "hidrógeno verde":
                factorAhorro = 0.3;
                break;
            default:
                factorAhorro = 0;
        }

        const ahorroEnergetico = consumo * factorAhorro;
        const reduccionCo2 = ahorroEnergetico * 0.5;
        const ahorroEconomico = ahorroEnergetico * 0.15;

        ahorrokwhSpan.textContent = ahorroEnergetico.toFixed(2);
        ahorroCo2Span.textContent = reduccionCo2.toFixed(2);
        ahorroUsdSpan.textContent = ahorroEconomico.toFixed(2);

        resultadosSection.classList.remove("hidden");
    });
});