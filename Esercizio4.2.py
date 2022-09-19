# Chiedere all’utente di inserire un numero da uno a 10
# e stampare la tabellina corrispondente

# Chiedo all'utente di inserire un numero
numero = input('Inserisci un numero intero da 1 a 10: ')
numero = int(numero)

if 1 <= numero <= 10:
    print('La tabellina del ' + str(numero) + ' è: ')
    for i in range(10):
        print(str(numero) + ' x ' + str(i + 1) + ' = ' + str(numero * (i + 1)))
else:
    print('numero non ammesso.')
