# pyton corso avanzato
# Esercizi
# Lezione 3 - Esercizio 4
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 07/11/22

# Scrivere un programma ricorsivo per il problema di Fibonacci

def fibonacci_ric(numero):
    result = 0
    if numero == 1:
        result = 1
    elif numero > 1:
        result = fibonacci_ric(numero - 1) + fibonacci_ric(numero - 2)
    return result


n = -1
while not n >= 0:
    n = int(input('Inserisci un numero intero: '))

print('Il numero di fibonacci di', n, 'è', fibonacci_ric(n))
