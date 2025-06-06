
from flask import Flask, render_template, send_file
import matplotlib.pyplot as plt
import io
import os

app = Flask(__name__, static_folder='.', template_folder='.')

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

@app.route('/grafica')
def grafica():
    meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',
             'Septiembre','Octubre','Noviembre','Diciembre']
    ventas = [40000000,43000000,47000000,48000500,61500300,78000000,
              77780500,68000000,80500700,87000000,10500500,110500700]

    plt.figure(figsize=(15,6))
    plt.plot(meses, ventas, color='blue', marker='o', linestyle='-', linewidth=2, label='Ventas 2025')
    plt.title('Evolución de Ventas Mensuales en 2025')
    plt.xlabel('Meses')
    plt.ylabel('Ventas')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
