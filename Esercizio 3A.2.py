# pyton corso avanzato
# Esercizi
# Lezione 3 - Esercizio 2
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 07/11/22

# Scrivere un programma Python che:
# A. Richiede all’utente di inserire un numero N compreso tra 5 e 15
# B. Richiede all’utente di inserire N elementi e li memorizza in una lista L
# C. Creare una copia L2 e L3 della lista L
# D1. Modificare il valore dell'elemento in posizione della lista L2 con valori casuali tra 0 e 100
# D. Modificare il valore di N/3 elementi della lista L3 scelti in modo casuale
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


def modifica_elem(lista, n_elem_to_modify, min_new_value=0, max_new_value=100):
    pos_modified = list()
    for i in range(0, n_elem_to_modify):
        pos_to_modify = randrange(0, len(lista))
        if not (pos_to_modify in pos_modified):
            lista[pos_to_modify] = randrange(min_new_value, max_new_value + 1)
    return lista


n = 0
while n < 5 or n > 15:
    n = int(input('Inserisci un numero intero compreso tra 5 e 15: '))

lista1 = list()
print('Dovrai inserire ', n, 'elementi')
for e in range(0, n):
    elem = int(input(f'Inserisci l\'elemento {e + 1}: '))
    lista1.append(elem)

lista2 = lista1.copy()
lista3 = lista1.copy()
pos = n // 3
n_elem = pos
lista2[pos] = randrange(0, 101)
lista3 = modifica_elem(lista3, n_elem)

somma1 = somma_elem(lista1)
somma2 = somma_elem(lista2)
somma3 = somma_elem(lista3)

print('La somma della lista 1', lista1, 'è', somma1)
print('La somma della lista 2', lista2, 'è', somma2)
print('La somma della lista 3', lista3, 'è', somma3)
