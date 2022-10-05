# pyton corso base
# Esercizi
# Lezione 10 - Esercizio 2
# Classi
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 05/10/22

# Creare una classe "Carta Ricaricabile",
# dove è possibile effettuare versamenti, prelievi,
# stampa del saldo ed ottenere la lista degli ultimi 10 movimenti.

import random


# instanzio la classe Carta Ricaricabile
class CartaRicaricabile:
    def __init__(self):
        self.saldo = 0
        self.movimenti = []

    def prelievo(self, valore):
        self.saldo -= valore
        self.movimenti.append(-valore)

    def versamento(self, valore):
        self.saldo += valore
        self.movimenti.append(valore)

    def print_lista_ultimi_10_movimenti(self):
        for value in self.movimenti[-10:]:
            print(value)

    def get_lista_ultimi_10_movimenti(self):
        return self.movimenti[-10:]

    def print_saldo(self):
        print(self.saldo)


mia_ricaricabile = CartaRicaricabile()

# movimento la carta con valori casuali
i = 0
while i <= 8:
    valore_casuale = random.randint(-1000, 1000)
    print('Valore casuale:', valore_casuale)
    if valore_casuale == 0:
        continue
    if valore_casuale < 0:
        mia_ricaricabile.prelievo(abs(valore_casuale))
    else:
        mia_ricaricabile.versamento(valore_casuale)
    i += 1

# Stampa del saldo
print('Saldo:')
mia_ricaricabile.print_saldo()

# Stampo la lista degli ultimi 10 movimenti
print('Lista Movimenti:')
mia_ricaricabile.print_lista_ultimi_10_movimenti()

# Scarico la lista degli ultimi 10 movimenti e la stampo
ultimi_movimenti = mia_ricaricabile.get_lista_ultimi_10_movimenti()
print('Ultimi movimenti:', ultimi_movimenti)
