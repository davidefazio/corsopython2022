# Scrivere un programma per richiedere all'utente 2 numeri
# effettuare la # somma ed il prodotto dei due numeri.
# Stampare a video due messaggi :
# “La somma di primo_numero e secondo_numero è uguale a somma_numeri”
# “Il prodotto di primo_numero e secondo_numero è uguale a prodotto_numeri”

# richiedere primo numero
primo_numero = input('Inserisci un numero: ')
secondo_numero = input('Inserisci un altro numero: ')

# calcolare la somma dei due numeri
somma_numeri = float(primo_numero) + float(secondo_numero)

# calcolare il prodotto dei due numeri
prodotto_numeri = float(primo_numero) * float(secondo_numero)

# Stampare i messaggi
print('La somma di ' + str(primo_numero) + ' e ' + str(secondo_numero) + ' è uguale a ' + str(somma_numeri))
print('Il prodotto di ' + str(primo_numero) + ' e ' + str(secondo_numero) + ' è uguale a ' + str(prodotto_numeri))
