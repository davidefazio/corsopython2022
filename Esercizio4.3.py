# Creare un piccolo gioco interattivo in cui si chiede
# all’utente di indovinare un numero tra 1 e 100.
# Ogni qualvolta l’utente inserirà un numero si
# comunicherà se il numero è “troppo grande” o
# “troppo piccolo” rispetto al numero sa indovinare

numero_esatto = 28
while True:
    numero = input('indovina un numero intero tra 1 e 100: ')
    numero = int(numero)

    if 1 <= numero <= 100:
        if numero > numero_esatto:
            print('Il numero ' + str(numero) + ' è troppo grande ')
        elif numero < numero_esatto:
            print('Il numero ' + str(numero) + ' è troppo piccolo ')
        else:
            print('Il numero ' + str(numero) + ' è esatto. HAI INDOVINATO ')
            break;
    else:
        print('numero non ammesso.')
