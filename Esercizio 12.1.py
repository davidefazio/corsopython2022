# pyton corso base
# Esercizi
# Lezione 12 - Esercizio 1
# API
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 10/10/22

import requests
import json

# definisco la tupla dei parametri con segno Leone e data oggi
params = (
    ('sign', 'leo'),
    ('day', 'today')
)

# effettuo la richiesta post passando i parametri precedentemente definiti
response = requests.post('https://aztro.sameerkumar.website', params=params)
# converto il contenuto della risposta in json
data = json.loads(response.content)
# stampo a video la risposta
print(data)
