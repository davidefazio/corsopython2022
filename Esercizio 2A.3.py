# pyton corso avanzato
# Esercizi
# Lezione 2 - Esercizio 3
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 31/10/22

# Scrivere un programma Python che chiede all’utente di inserire un numero
# intero X e memorizzi in una lista tutti i numeri primi compresi tra 0 e X (X
# compreso)

def numero_primo(numero):
    is_numero_primo = True
    for i in range(2, numero):
        modulo = numero % i
        if modulo == 0:
            is_numero_primo = False
            break
    return is_numero_primo


x = int(input('inserisci un numero intero: '))
lista_numeri_primi = []
for z in range(2, x + 1):
    if numero_primo(z):
        lista_numeri_primi.append(z)
print("i numeri primi tra 2 e ", x, "compreso sono:")
print(lista_numeri_primi)
