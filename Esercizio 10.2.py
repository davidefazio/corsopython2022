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
import logging

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(filename='ricaricabile.log', filemode='w', level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger()


# instanzio la classe Carta Ricaricabile
class CartaRicaricabile:
    def __init__(self, log):
        self.saldo = 0
        self.massimale = 1000
        self.movimenti = []
        self.log = log
        self.log.debug('inizializzata carta ricaricabile')

    def prelievo(self, valore):
        self.log.debug(f'richiamata prelievo')
        if self.saldo > valore:
            self.saldo -= valore
            self.movimenti.append(-valore)
            self.log.debug(f'registrato prelievo di {valore}')
            return 1
        else:
            print(f'Il tuo saldo ({self.saldo}) non è sufficiente ad effettuare il prelievo di {valore}')
            self.log.debug(f'Prelievo non effettuabile. '
                           f'Il tuo saldo ({self.saldo}) non è sufficiente ad effettuare il prelievo di {valore}')
            return 0

    def versamento(self, valore):
        self.log.debug(f'richiamata versamento')
        if self.saldo + valore <= self.massimale:
            self.saldo += valore
            self.movimenti.append(valore)
            self.log.debug(f'registrato versamento di {valore}')
            return 1
        else:
            print(f'Il versamento di {valore} non può essere effettuato perché supererebbe '
                  f'il massimale ({self.massimale}).')
            self.print_saldo()
            self.log.debug(f'Versamento non effettuabile. '
                           f'Il versamento di {valore} non può essere effettuato perché supererebbe '
                           f'il massimale ({self.massimale})')
            return 0

    def print_lista_ultimi_10_movimenti(self):
        self.log.debug(f'richiamata print_lista_ultimi_10_movimenti')
        for value in self.movimenti[-10:]:
            print(value)

    def get_lista_ultimi_10_movimenti(self):
        self.log.debug(f'richiamata get_lista_ultimi_10_movimenti')
        return self.movimenti[-10:]

    def print_saldo(self):
        self.log.debug('richiamata print_saldo')
        print('Il tuo saldo è:', self.saldo)
        self.log.debug(f'stampato il saldo {self.saldo}')


logger.debug('inizio simulazione')
mia_ricaricabile = CartaRicaricabile(logger)
# movimento la carta con valori casuali
i = 0
while i <= 8:
    valore_casuale = random.randint(-1000, 1000)
    print('Valore casuale:', valore_casuale)
    result = 0
    if valore_casuale == 0:
        continue
    if valore_casuale < 0:
        result = mia_ricaricabile.prelievo(abs(valore_casuale))
    else:
        mia_ricaricabile.versamento(valore_casuale)
    if result == 1:
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
logger.debug('fine simulazione')
