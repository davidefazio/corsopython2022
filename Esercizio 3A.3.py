# pyton corso avanzato
# Esercizi
# Lezione 3 - Esercizio 3
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 07/11/22

# Scrivere un programma iterativo per il problema di Fibonacci

def fibonacci_iter(numero):
    result = 0
    if numero > 0:
        a, b = 0, 1
        for i in range(numero - 1):
            a, b = b, a+b
        result = b
    return result


n = -1
while not n > 0:
    n = int(input('Inserisci un numero intero: '))

print('Il numero di fibonacci di', n, 'è', fibonacci_iter(n))
