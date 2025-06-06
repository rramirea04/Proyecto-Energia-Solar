import os
import io
import matplotlib.pyplot as plt
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/panel')
def panel():
    return render_template('panel.html')

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/tipos')
def tipos():
    return render_template('tipos.html')

# 🚀 Ruta que genera la gráfica dinámicamente
@app.route('/grafico')
def grafico():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30], marker='o')
    ax.set_title("Consumo Energético")
    ax.set_xlabel("Días")
    ax.set_ylabel("Consumo (kWh)")

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)

    return Response(img.getvalue(), mimetype='image/png')

# 🟢 Configuración para que funcione en Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
