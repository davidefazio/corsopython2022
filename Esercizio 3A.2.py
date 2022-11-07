# pyton corso avanzato
# Esercizi
# Lezione 3 - Esercizio 2
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 07/11/22

# Scrivere un programma Python che:
# A. Richiede all’utente di inserire un numero N compreso tra 5 e 15
# B. Richiede all’utente di inserire N elementi e li memorizza in una lista L
# C. Creare una copia L2 della lista L
# D. Modificare il valore di N/3 elementi della lista L2 scelti in modo casuale
# con valori casuali tra 0 e 100 (valutare se opportuno scrivere una
# funzione)
# E. Stampare (utilizzare la funzione sommaElem(list) dell’esercizio 1) il
# valore della lista L e della lista L2

from random import randrange


def somma_elem(lista):
    somma = 0
    for i in lista:
        if isinstance(i, int) or isinstance(i, float):
            somma += i
    return somma


n = 0
while n < 5 or n > 15:
    n = int(input('Inserisci un numero intero compreso tra 5 e 15: '))

lista1 = list()
print('Dovrai inserire ', n, 'elementi')
for e in range(0, n):
    elem = int(input(f'Inserisci l\'elemento {e + 1}: '))
    lista1.append(elem)

lista2 = lista1.copy()
pos = n // 3
lista2[pos] = randrange(0, 101)

somma1 = somma_elem(lista1)
somma2 = somma_elem(lista2)

print('La somma della lista 1', lista1, 'è', somma1)
print('La somma della lista 2', lista2, 'è', somma2)
