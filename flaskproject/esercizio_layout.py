# pyton corso base
# Esercizi
# Lezione 11 - Esercizio 2
# Utilizzo Layout
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 10/10/22

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/homel")
def home():
    return render_template('homel.html', title='home', titolo_pagina='HOME', nome_pagina='homel.html',
                           testo_pagina='Questa è la nostra home page')


@app.route("/chisiamol")
def chisiamo():
    return render_template('chisiamol.html', title='chi siamo', titolo_pagina='CHI SIAMO', nome_pagina='chisiamol.html',
                           testo_pagina='Questa è la nostra pagina Chi Siamo', nominativo='Davide Fazio')


@app.route("/servizil")
def servizi():
    return render_template('servizil.html', title='servizi', titolo_pagina='SERVIZI', nome_pagina='servizil.html',
                           testo_pagina='Questa è la nostra pagina Servizi', servizi='Sviluppo Software')


@app.route("/contattil")
def contatti():
    return render_template('contattil.html', title='contatti', titolo_pagina='CONTATTI', nome_pagina='contattil.html',
                           testo_pagina='Questa è la nostra pagina Contatti',
                           telefono="+393999999999", email="fazio@olomedia.it")
