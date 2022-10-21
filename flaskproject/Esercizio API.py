# pyton corso base
# Esercizi
# @todo Lezione 11 - Esercizio 3
# API
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 21/10/22

import flask
from flask import request, jsonify
import sqlite3

# inizializzo l'oggetto app
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# definisco il nostro oggetto SQLlite
DB = "users.db"


def dict_factory(cursor, row):
    """Converto i valori del DB in oggetti dizionario."""
    d = dict()
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# creo il routing home page
@app.route('/', methods=["GET"])
def home():
    return '''<h1>SERVER USERS</h1>
            <p> Prova le nostre API</p>
            <ul>
               <li> <b>Tutti gli utenti</b> 
               <a href="http://127.0.0.1:5000/api/v1/resources/users/all">
                  http://127.0.0.1:5000/api/v1/resources/users/all
               </a></li>
               <li> <b>Ricerca Utente per età</b> 
               Es.: <a href="http://127.0.0.1:5000/api/v1/resources/users?age=28">
                  http://127.0.0.1:5000/api/v1/resources/users?age=28
                  </a>
               </li>
            </ul>'''


# routing error page 404
@app.errorhandler(404)
def page_not_found():
    return "<h1>OOPS</h1> <p> Page not found </p>", 404


# routing per ottenere la lista completa degli album
@app.route('/api/v1/resources/users/all', methods=["GET"])
def api_all():
    # creo una connessione al DB che chiamo conn utilizzano il metodo sqlite3.connect
    conn = sqlite3.connect(DB)

    # utilizzo row_factory in sqllite cosi che la righe siano restituite nel formato dizionario:
    conn.row_factory = dict_factory

    # assegno un puntatore che punta al db che useremo per le operazioni
    cur = conn.cursor()

    # eseguo una query sul database
    all_users = cur.execute("SELECT * FROM users;").fetchall()

    return jsonify(all_users)


# routing api connection to users db
@app.route("/api/v1/resources/users", methods=["GET"])
def api_filter():

    query_parameters = request.form

    field_list = (
        'id', 'firstName', 'lastName', 'maidenName',
        'age', 'gender', 'email', 'phone', 'username',
        'birthDate', 'bloodGroup', 'height', 'weigth',
        'eyeColor', 'university', 'ein', 'ssn', 'userAgent'
    )

    # building our SQL query
    query = "SELECT * FROM users WHERE "
    to_filter = []

    for field in field_list:
        value = query_parameters.get(field)
        if value:
            query += ' ' + field + ' =? AND'
            to_filter.append(value)

    if not (len(to_filter)):
        return page_not_found()

    # this is needed to clean the SQL query after the last item is added; basically it removes the " AND" and add a ";"
    query = query[:-4] + ";"

    conn = sqlite3.connect(DB)
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


@app.route('/api/v1/resources/user/add', methods=["POST"])
def api_add():

    parameters = request.form
    # write in a fle request.txt request parameters in variables separated by a comma
    with open("request.txt", "w") as f:
        f.write(str(parameters))

    # building our SQL query
    user = []
    fields = ''
    values = ''
    field_list = (
        'id', 'firstName', 'lastName', 'maidenName',
        'age', 'gender', 'email', 'phone', 'username',
        'birthDate', 'bloodGroup', 'height', 'weigth',
        'eyeColor', 'university', 'ein', 'ssn', 'userAgent'
    )

    for field in field_list:
        value = query_parameters.get(field)
        if value:
            fields += ' ' + field + ', '
            values += ' ?, '
            user.append(value)

    if not (len(to_filter)):
        return page_not_found()

    # this is needed to clean the SQL query after the last item is added
    fields = fileds[:-2]
    values = values[:-2]
    sql = f'INSERT INTO users ({fields}) VALUES ({values})'

    conn = sqlite3.connect(DB)

    # conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute(query, sql)
    conn.commit()

    result = {"lastid": cur.lastrowid}

    return jsonify(result)
