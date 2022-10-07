# pyton corso base
# Esercizi
# Lezione 11 - Esercizio 1
# Render Template
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 07/10/22

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template('home.html', title='home')


@app.route("/chisiamo")
def chisiamo():
    return render_template('chisiamo.html', title='chi siamo', nominativo='Davide Fazio')


@app.route("/servizi")
def servizi():
    return render_template('servizi.html', title='servizi', servizi='Sviluppo Software')


@app.route("/contatti")
def contatti():
    return render_template('contatti.html', title='contatti', telefono="+393999999999", email="fazio@olomedia.it")
