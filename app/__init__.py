import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/athena')
def athena():
    return render_template('athena.html', name="Athena")

@app.route('/patrick')
def patrick():
    return render_template('patrick.html', name ="Patrick")

@app.route('/juancarlos')
def juancarlos():
    return render_template('juancarlos.html', name="Juan Carlos")

@app.route('/individual')
def base():
    return render_template('individual.html')


# @app.route("/static/<path:path>")
# def static_dir(path):
#     return send_from_directory("static", path)