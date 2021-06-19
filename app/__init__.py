import os
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=22)

@app.route('/')
def index():
    return render_template('index.html', title="Portfolio", url=os.getenv("URL"))

@app.route('/athena')
def athena():
    return render_template('athena.html', name="Athena")

@app.route('/patrick')
def patrick():
    return render_template('patrick.html', name ="Patrick")

@app.route('/juancarlos')
def juancarlos():
    return render_template('juancarlos.html', name="Juan Carlos")

@app.route('/health', methods=[ 'GET' ])
def health():
    return jsonify(status=200)