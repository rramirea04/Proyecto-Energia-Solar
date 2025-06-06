from flask import Flask, send_file
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/grafica')
def grafica():
    meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',
             'Septiembre','Octubre','Noviembre','Diciembre']
    ventas = [40000000,43000000,47000000,48000500,61500300,78000000,
              77780500,68000000,80500700,87000000,10500500,110500700]

    plt.figure(figsize=(15,6))
    plt.plot(meses, ventas, color='blue', marker='o', linestyle='-', linewidth=2, label='Ventas 2025')
    plt.title('Evolución de Ventas Mensuales en 2025', fontsize=16, fontweight='bold')
    plt.xlabel('Meses', fontsize=14)
    plt.ylabel('Ventas', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.legend(fontsize=12)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return send_file(buf, mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
