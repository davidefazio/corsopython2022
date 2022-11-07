# pyton corso avanzato
# Esercizi
# Lezione 3 - Esercizio 1
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 07/11/22

# Scrivere una funzione sommaElem(list) che riceve in input una list (list) e
# restituisce la somma degli elementi della lista (list)

def somma_elem(lista):
    somma = 0
    for i in lista:
        if isinstance(i, int) or isinstance(i, float):
            somma += i
    return somma


lista_esempio = [1, 5, 10, 25]
somma1 = somma_elem(lista_esempio)
print(somma1)
