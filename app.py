# ------------------------------------------
# Importación de librerías necesarias
# ------------------------------------------
import os                  # Para acceder a variables del entorno del sistema
import io                  # Para manejar flujos de datos en memoria (como imágenes)
import numpy as np         # Para cálculos numéricos y datos aleatorios
import matplotlib
matplotlib.use('Agg')      # Configura matplotlib para entornos sin entorno gráfico (como Render)
import matplotlib.pyplot as plt  # Librería de gráficos
from flask import Flask, render_template, Response  # Funciones principales de Flask

# Inicializa la aplicación Flask
app = Flask(__name__)

# ------------------------------------------
# Rutas para renderizar páginas HTML
# ------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')  # Página de inicio

@app.route('/panel')
def panel():
    return render_template('panel.html')  # Página personalizada del usuario

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')  # Calculadora energética

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')  # Noticias del sector

@app.route('/tipos')
def tipos():
    return render_template('tipos.html')  # Tipos de energía

# ------------------------------------------
# Rutas que generan y devuelven gráficos dinámicamente
# ------------------------------------------

# 📊 Ruta 1: Histograma con datos aleatorios
@app.route('/grafico-histograma')
def grafico_histograma():
    datos = np.random.randn(1000)  # 1000 datos aleatorios con distribución normal
    fig, ax = plt.subplots()
    ax.hist(datos, bins=20, color='blue', edgecolor='black')
    ax.set_title("Histograma Talento Tech")
    ax.set_xlabel("Valores")
    ax.set_ylabel("Frecuencia")

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)

    return Response(img.getvalue(), mimetype='image/png')


# 🥧 Ruta 2: Gráfico de pastel (pie chart)
@app.route('/grafico-pie')
def grafico_pie():
    participante = [25, 15, 30, 20, 10]
    etiquetas = ['Empresa A', 'Empresa B', 'Empresa C', 'Empresa D', 'Empresa E']
    colores = ['blue', 'green', 'red', 'orange', 'purple']
    sobresale = [0, 0, 0.2, 0.1, 0]

    fig, ax = plt.subplots()
    ax.pie(participante, labels=etiquetas, colors=colores,
           autopct='%.1f%%', startangle=90, explode=sobresale)
    ax.set_title('Distribución de mercado', fontsize=16, fontweight='bold')

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)

    return Response(img.getvalue(), mimetype='image/png')


# 📈 Ruta 3: Gráfico de línea (original del panel)
@app.route('/grafico')
def grafico():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, color='green')
    ax.set_title("Consumo energético ficticio")
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Consumo")

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)

    return Response(img.getvalue(), mimetype='image/png')

# ------------------------------------------
# Configuración para ejecución (local o producción)
# ------------------------------------------

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Usa puerto 5000 o el definido en el entorno
    app.run(host='0.0.0.0', port=port)        # Ejecuta la app accesible desde cualquier IP