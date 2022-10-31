# pyton corso avanzato
# Esercizi
# Lezione 2 - Esercizio 0
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 31/10/22

def numero_primo(numero):
    is_numero_primo = True
    for i in range(2, numero):
        modulo = numero % i
        if modulo == 0:
            print('fattore di ', numero, '=', i)
            is_numero_primo = False

    if is_numero_primo:
        print(numero, 'è un numero primo')


for z in range(2, 25):
    numero_primo(z)
