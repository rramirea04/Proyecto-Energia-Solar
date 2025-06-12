# ------------------------------------------
# Importación de librerías necesarias
# ------------------------------------------
import os
import io
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Para entornos sin GUI (como Render)
import matplotlib.pyplot as plt
from flask import Flask, render_template, Response

app = Flask(__name__)

# ------------------------------------------
# Rutas de páginas HTML
# ------------------------------------------

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

# ------------------------------------------
# Rutas de gráficas realistas
# ------------------------------------------

@app.route('/grafico')
def grafico():
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    ahorro_kwh = np.random.normal(loc=420, scale=50, size=12).round(0)

    fig, ax = plt.subplots()
    ax.plot(meses, ahorro_kwh, marker='o', color='green')
    ax.set_title('Ahorro Energético Mensual')
    ax.set_ylabel('kWh')
    ax.grid(True)

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)
    return Response(img.getvalue(), mimetype='image/png')


@app.route('/grafico-histograma')
def grafico_histograma():
    ahorro_kwh = np.random.normal(loc=420, scale=50, size=12).round(0)
    co2 = ahorro_kwh * 0.707
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

    fig, ax = plt.subplots()
    ax.plot(meses, co2, marker='s', linestyle='--', color='red')
    ax.set_title('Reducción de CO₂ Mensual')
    ax.set_ylabel('kg CO₂')
    ax.grid(True)

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)
    return Response(img.getvalue(), mimetype='image/png')


@app.route('/grafico-pie')
def grafico_pie():
    ahorro_trimestres = [300000, 340000, 290000, 360000]
    trimestres = ['Ene-Mar', 'Abr-Jun', 'Jul-Sep', 'Oct-Dic']

    fig, ax = plt.subplots()
    ax.pie(ahorro_trimestres, labels=trimestres, autopct='%1.1f%%')
    ax.set_title('Ahorro Económico Trimestral')

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)
    return Response(img.getvalue(), mimetype='image/png')

# ------------------------------------------
# Ejecución local o en Render
# ------------------------------------------

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
