
from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)
