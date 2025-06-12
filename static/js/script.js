// =====================
// CHATBOT DE ENERGÍAS RENOVABLES
// =====================

function responder() {
  // Obtiene el texto del input, eliminando espacios y pasando a minúsculas
  const input = document.getElementById("userInput").value.trim().toLowerCase();
  const respuesta = document.getElementById("respuestaBot"); // Elemento donde se muestra la respuesta

  // Si el input está vacío, muestra un mensaje de advertencia
  if (input === "") {
    respuesta.textContent = "Por favor, escribe una pregunta relacionada con energías renovables.";
    return;
  }

  // Respuesta a saludos + sugerencias de preguntas frecuentes
  if (
    input.includes("hola") ||
    input.includes("buenos días") ||
    input.includes("buenas tardes") ||
    input.includes("buenas noches")
  ) {
    respuesta.innerHTML = `¡Hola! Soy tu asistente virtual de energías renovables 🌱.<br><br>
    Puedes preguntarme cosas como:<ul>
      <li>¿Qué es la energía solar?</li>
      <li>¿Para qué sirve el hidrógeno verde?</li>
      <li>¿Qué ventajas tiene la energía eólica?</li>
      <li>¿Qué es la biomasa?</li>
      <li>¿Qué energías renovables hay en Colombia?</li>
      <li>¿Cómo ayuda la eficiencia energética al planeta?</li>
    </ul>`;
    return;
  }

  // Diccionario de respuestas según temas detectados
  if (input.includes("solar")) {
    respuesta.textContent = "☀️ La energía solar se obtiene del sol. Un sistema fotovoltaico convierte la luz solar en electricidad sin contaminar. Colombia tiene un alto potencial solar gracias a su ubicación cerca del Ecuador.";
  } else if (input.includes("eólica") || input.includes("viento")) {
    respuesta.textContent = "💨 La energía eólica utiliza el viento para mover turbinas que generan electricidad. En la Guajira, Colombia tiene uno de los mayores potenciales eólicos de América Latina.";
  } else if (input.includes("hidrógeno")) {
    respuesta.textContent = "⚗️ El hidrógeno verde se produce mediante electrólisis usando energía renovable. Es una fuente limpia y versátil, ideal para transporte pesado e industria.";
  } else if (input.includes("biomasa")) {
    respuesta.textContent = "🌿 La biomasa es materia orgánica (residuos agrícolas, forestales o estiércol) que puede transformarse en energía. Es renovable si se gestiona adecuadamente.";
  } else if (input.includes("geotermia") || input.includes("geotérmica")) {
    respuesta.textContent = "🌋 La energía geotérmica se obtiene del calor interno de la Tierra. Puede aprovecharse mediante pozos en zonas volcánicas. Es estable y constante.";
  } else if (input.includes("eficiencia")) {
    respuesta.textContent = "💡 La eficiencia energética significa usar menos energía para obtener el mismo resultado. Cambiar a bombillas LED o mejorar el aislamiento de una casa son buenos ejemplos.";
  } else if (input.includes("cambio climático") || input.includes("calentamiento global")) {
    respuesta.textContent = "🌎 El cambio climático es el resultado del aumento de gases de efecto invernadero. Las energías renovables ayudan a reducir estas emisiones y proteger el planeta.";
  } else if (input.includes("energía renovable")) {
    respuesta.textContent = "🔄 Las energías renovables son fuentes que se regeneran naturalmente: solar, eólica, hidroeléctrica, biomasa y geotermia. Son claves para un futuro sostenible.";
  } else if (input.includes("colombia")) {
    respuesta.textContent = "🇨🇴 Colombia tiene un gran potencial en energía solar (por su radiación), eólica (La Guajira), hídrica (por sus ríos) y biomasa (por su actividad agrícola).";
  } else if (input.includes("gracias") || input.includes("muy amable")) {
    respuesta.textContent = "¡Con gusto! Si tienes más preguntas sobre energías renovables, estaré aquí para ayudarte 🌿.";
  } else if (input.includes("adiós") || input.includes("hasta luego")) {
    respuesta.textContent = "¡Hasta pronto! 🌞 Sigue cuidando el planeta con energías limpias.";
  } else {
    // Mensaje por defecto si no se reconoce el tema
    respuesta.textContent = "Lo siento, aún estoy aprendiendo. Intenta preguntarme sobre energía solar, eólica, hidrógeno verde, biomasa, geotermia o eficiencia energética.";
  }
}

// Función para mostrar u ocultar el chatbot en pantalla
function toggleChatbot() {
  const chatbot = document.getElementById("chatbot-box");
  chatbot.style.display = chatbot.style.display === "block" ? "none" : "block";
}

// Permitir enviar pregunta presionando la tecla Enter
document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("userInput");

  input.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      event.preventDefault(); // Previene comportamiento por defecto
      responder(); // Llama al chatbot
    }
  });
});

// =====================
// CALCULADORA DE AHORRO ENERGÉTICO
// =====================

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
      alert("Por favor, ingresa un valor de consumo válido.");
      return;
    }

    // Factores aproximados de eficiencia por tipo de energía
    let factorAhorro = {
      solar: 0.20,
      eolica: 0.25,
      hidrogeno: 0.30,
      hidraulica: 0.22,
      biomasa: 0.18,
      geotermica: 0.28,
    }[tipoEnergia] || 0;

    const ahorroEnergetico = consumo * factorAhorro;     // Ahorro estimado en kWh
    const reduccionCo2 = ahorroEnergetico * 0.5;         // Reducción de CO₂ en kg (estimado)
    const ahorroEconomico = ahorroEnergetico * 0.15;     // Ahorro económico estimado (USD)

    // Mostrar resultados
    ahorrokwhSpan.textContent = ahorroEnergetico.toFixed(2);
    ahorroCo2Span.textContent = reduccionCo2.toFixed(2);
    ahorroUsdSpan.textContent = ahorroEconomico.toFixed(2);

    resultadosSection.classList.remove("hidden");
  });
});