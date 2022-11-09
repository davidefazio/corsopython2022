# pyton corso avanzato
# Esercizi
# Lezione 4 - Esercizio 1
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 09/11/22

# Esercizio 1:
# 1) Scrivere programma Python che definisce una classe Autoveicolo con 3 attributi:
# a) cilindrata
# b) modello
# c) numeroRuote
# 2) Scrivere i metodi della Classe Autoveicolo set_cilindrata(self, cilindrata)…. set_modello(…)
# e set_numero_ruote(…) per assegnare un valore ai relativi attributi della classe
# 3) Creare 5 oggetti Autoveicolo(auto1, auto2,…), assegnare valori a piacere agli attributi
# modello e numeroRuote; assegnare un valore casuale tra 100 e 1000 all’attributo
# cilindrata
# 4) Stampare a video i valori di cilindrata, modello e numeroRoute solo dell’Autoveicolo con la
# cilindrata con valore maggiore
# 5) Stampare a video i valori di cilindrata, modello e numeroRoute di tutti gli Autoveicoli

from random import randrange


class Automobile:
    def __init__(self):
        self._modello = str()
        self._cilindrata = 100
        self._numero_ruote = 4

    def set_modello(self, modello):
        self._modello = modello

    def set_cilindrata(self, cilindrata):
        self._cilindrata = cilindrata

    def set_numero_ruote(self, numero_ruote):
        self._numero_ruote = numero_ruote

    def get_cilindrata(self):
        return self._cilindrata

    def print(self):
        print(f'Modello: {self._modello}; Cilindrata: {self._cilindrata}; Ruote: {self._numero_ruote}')


automobili = list()
for i in range(0, 5):
    automobili.append(Automobile())

automobili[0].set_modello('VW Golf')
automobili[1].set_modello('VW Polo')
automobili[2].set_modello('Opel Corsa')
automobili[3].set_modello('Audi A3')
automobili[4].set_modello('VW T-Roc')


for i in automobili:
    i.set_cilindrata(randrange(100, 1001))

automobile = automobili[0]
for i in automobili:
    cilindrata_auto = i.get_cilindrata()
    if cilindrata_auto > automobile.get_cilindrata():
        automobile = i

print()
automobile.print()
print()
for i in automobili:
    i.print()
