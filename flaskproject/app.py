# pyton corso base
# Esempio APP Flask
# Lezione 07/10/2022
# FLASK
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 07/10/22

from flask import Flask

app = Flask(__name__)


@app.route("/app")
def hello_world():
    return "<p>Hello, World!</p>"
