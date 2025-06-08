# Importación de librerías necesarias
import os                  # Permite acceder a variables del entorno del sistema (como el puerto)
import io                  # Permite trabajar con flujos de datos en memoria (para enviar la imagen generada)
import matplotlib.pyplot as plt  # Librería para crear gráficos
import numpy as np         # Librería para manejar datos numéricos (aquí se usa para generar datos aleatorios)
from flask import Flask, render_template, Response  # Funciones principales de Flask

# Inicializa la aplicación Flask
app = Flask(__name__)

# ----------------------------
# Rutas para las distintas páginas de la aplicación
# ----------------------------

@app.route('/')
def index():
    # Renderiza el archivo HTML llamado index.html
    return render_template('index.html')

@app.route('/panel')
def panel():
    # Renderiza el archivo HTML llamado panel.html
    return render_template('panel.html')

@app.route('/calculadora')
def calculadora():
    # Renderiza el archivo HTML llamado calculadora.html
    return render_template('calculadora.html')

@app.route('/noticias')
def noticias():
    # Renderiza el archivo HTML llamado noticias.html
    return render_template('noticias.html')

@app.route('/tipos')
def tipos():
    # Renderiza el archivo HTML llamado tipos.html
    return render_template('tipos.html')

# ----------------------------
# Rutas que generan gráficas dinámicamente
# ----------------------------

# 📊 Ruta 1: Genera un histograma con datos aleatorios
@app.route('/grafico-histograma')
def grafico_histograma():
    datos = np.random.randn(1000)  # Genera 1000 datos aleatorios con distribución normal
    fig, ax = plt.subplots()       # Crea la figura y el eje para la gráfica
    ax.hist(datos, bins=20, color='blue', edgecolor='black')  # Dibuja el histograma con 20 barras

    # Agrega título y etiquetas a los ejes
    ax.set_title("Histograma Talento Tech")
    ax.set_xlabel("Valores")
    ax.set_ylabel("Frecuencia")

    img = io.BytesIO()            # Crea un flujo de datos en memoria
    fig.savefig(img, format='png')  # Guarda la figura en ese flujo en formato PNG
    img.seek(0)                   # Lleva el puntero al inicio del flujo
    plt.close(fig)               # Cierra la figura para liberar memoria

    # Devuelve la imagen como respuesta HTTP, indicando que es un PNG
    return Response(img.getvalue(), mimetype='image/png')

# 🥧 Ruta 2: Genera un gráfico circular (pie chart)
@app.route('/grafico-pie')
def grafico_pie():
    # Datos para el gráfico de pastel
    participante = [25, 15, 30, 20, 10]  # Porcentaje de participación de cada empresa
    etiquetas = ['Empresa A', 'Empresa B', 'Empresa C', 'Empresa D', 'Empresa E']
    colores = ['blue', 'green', 'red', 'orange', 'purple']  # Colores asignados a cada empresa
    sobresale = [0, 0, 0.2, 0.1, 0]  # "Explosión" para destacar ciertas porciones

    fig, ax = plt.subplots()  # Crea la figura y eje
    ax.pie(participante, labels=etiquetas, colors=colores,  # Dibuja el gráfico de pastel
           autopct='%.1f%%', startangle=90, explode=sobresale)  # autopct muestra el porcentaje

    ax.set_title('Distribución de mercado', fontsize=16, fontweight='bold')  # Título del gráfico

    img = io.BytesIO()                # Crea flujo de datos
    fig.savefig(img, format='png')    # Guarda la imagen en ese flujo
    img.seek(0)                       # Vuelve al inicio del flujo
    plt.close(fig)                    # Cierra la figura

    return Response(img.getvalue(), mimetype='image/png')  # Devuelve la imagen como respuesta HTTP

# ----------------------------
# Configuración final para producción (por ejemplo, en Render.com)
# ----------------------------

# Esta sección solo se ejecuta si se lanza el archivo directamente (no en modo importado)
if __name__ == '__main__':
    # Obtiene el puerto desde una variable de entorno o usa el 5000 por defecto
    port = int(os.environ.get('PORT', 5000))
    # Ejecuta la aplicación en modo accesible desde cualquier IP (necesario en producción)
    app.run(host='0.0.0.0', port=port)

