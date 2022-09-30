# Realizzare il classico gioco “morra cinese”.
# Chiedere all’utente se uno dei due giocatori deve essere il
# computer o un altro giocatore umano ed implementare le due
# versioni

from random import randrange


def morra(mossa1, mossa2):
    risultato = -1
    if mossa1 == mossa2 and (mossa1 == 1 or mossa1 == 2 or mossa1 == 3):
        risultato = 0
    elif (mossa1 == 1 and mossa2 == 2) or (mossa1 == 2 and mossa2 == 3) or (mossa1 == 3 and mossa2 == 1):
        risultato = 2
    elif (mossa2 == 1 and mossa1 == 2) or (mossa2 == 2 and mossa1 == 3) or (mossa2 == 3 and mossa1 == 1):
        risultato = 1
    return risultato


# inizializzo numero_giocatori
numero_giocatori = 0
# Chiedere numero giocatori
try:
    numero_giocatori = int(input('Inserisci il numero di giorcatori (1 o 2): '))
except:
    print("Numero giocatori non valido")

mossa_giocatore1 = 0
mossa_giocatore2 = 0

if numero_giocatori == 2:
    try:
        print('Fate le vostre giocate (1: Carta, 2: Forbice, 3: Sasso')
        mossa_giocatore1 = int(input('Giocatore 1: '))
        mossa_giocatore2 = int(input('Giocatore 2: '))
    except:
        print("Gioocata non valida")
else:
    try:
        print('Fai la tua giocata (1: Carta, 2: Forbice, 3: Sasso')
        mossa_giocatore1 = int(input('Giocatore 1: '))
    except:
        print("Giocata non valida")

    # random da 1 a 3
    mossa_giocatore2 = randrange(1, 4)

tupla_morra = ('Carta', 'Forbice', 'Sasso')

morra = morra(mossa_giocatore1, mossa_giocatore2)
if morra == 0:
    print('PAREGGIO. Entrambi avete giocato: ', tupla_morra[mossa_giocatore1 - 1])
elif morra == 1:
    print('VINCE GIOCATORE 1.', tupla_morra[mossa_giocatore1 - 1], 'batte', tupla_morra[mossa_giocatore2 - 1])
elif morra == 2 and numero_giocatori == 2:
    print('VINCE GIOCATORE 2.', tupla_morra[mossa_giocatore2 - 1], 'batte', tupla_morra[mossa_giocatore1 - 1])
elif morra == 2:
    print('VINCE IL COMPUTER.', tupla_morra[mossa_giocatore2 - 1], 'batte', tupla_morra[mossa_giocatore1 - 1])
else:
    print('GIOCATA NON VALIDA.')
