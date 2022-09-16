# Definire 4 funzioni per le operazioni matematiche:
# addizione,
# sottrazione,
# divisione,
# moltiplicazione

def operazione(valore1, valore2, operatore):
    risultato = 0
    if operatore == '+' or operatore == 'somma' or operatore == 'addizione':
        risultato = somma(valore1, valore2)
    elif operatore == '-' or operatore == 'sottrai' or operatore == 'sottrazione':
        risultato = sottrai(valore1, valore2)
    elif operatore == 'x' or operatore == '*' or operatore == 'moltiplica' or operatore == 'moltiplicazione':
        risultato = moltiplica(valore1, valore2)
    elif operatore == ':' or operatore == '/' or operatore == 'dividi' or operatore == 'divisione':
        risultato = dividi(valore1, valore2)
    return risultato


def somma(valore1, valore2):
    return float(valore1) + float(valore2)


def sottrai(valore1, valore2):
    return float(valore1) - float(valore2)


def moltiplica(valore1, valore2):
    return float(valore1) * float(valore2)


def dividi(valore1, valore2):
    risultato = 0
    if valore2 != 0 and valore2 != '0':
        risultato = float(valore1) / float(valore2)
    return risultato


# Chiedere all’utente un primo numero
valore_1 = input('Inserisci il primo numero: ')
# Chiedere all’utente un secondo numero
valore_2 = input('Inserisci il secondo numero: ')

# Chiedere all’utente l’operazione da effettuare
print('Inserisci l\'operazione da effettuare: ')
print('puoi utilizzare i comandi:')
print('   +, somma, addizione per sommare i 2 numeri')
print('   -, sottrai, sottrazione per sottrarre i 2 numeri')
print('   x, *, moltiplica, moltiplicazione per moltiplicare i 2 numeri')
print('   :, /, dividi, divisione per dividere i 2 numeri')
operatore_input = input()


print('L\'operazione ' + str(operatore_input) + ' dei numeri ' + str(valore_1) + ' e ' + str(valore_2))
print('ha il seguente risultato:')
print(operazione(valore_1, valore_2, operatore_input))