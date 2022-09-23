# Creare un ambiente virtuale chiamato laboratorio

# Realizzare un piccolo gioco “numero_misterioso”
# 1. Importare la libreria random
# 2. Far scegliere all’utente la lingua (IT on ENG)
# 3. Generare un numero misteioso da 1 a 10
# 4. Chiedere all’utente se il numero misterioso è <= a 5 o >5
# 5. Comunicare all’utente il risultato.
# 6. Tenere conto dei risultati; l’utente vince se indovina 10 volte
# prima di sbagliare 10 volte

# Importo la libreria random
from random import randrange

lingua = input('Scegli la lingua IT o ENG: ')

dizionario = {
    "IT": [
        'indovina se il numero misterioso è <= o > di 5. 1: <=, 2: > ',
        'Hai indovinato! Il numero misterioso è:',
        'Hai sbagliato! Il numero misterioso è:',
        'Hai perso! hai sbagliato',
        'volte e indovinato',
        'volte',
        'Hai VINTO! hai indovinato',
        'volte e sbagliato',
    ],
    "ENG": [
        'Guess if the mystery number is <= or> of 5. 1: <=, 2: > ',
        'You guess it! The mysterious number is:',
        'You were wrong! The mysterious number is:',
        'GAME OVER! you were wrong',
        'times and you guessed',
        'times',
        'WIN! you guessed',
        'times and you were wrong',
    ],

}

vittorie = 0
sconfitte = 0
while True:
    # Genero un numero misteioso da 1 a 10
    numero_misterioso = randrange(1, 11)
    # 4. Chiedere all’utente se il numero misterioso è <= a 5 o >5
    scommessa = input(dizionario[lingua][0])
    scommessa = int(scommessa)

    # Verifico e comunico all’utente il risultato.
    if (scommessa == 1 and numero_misterioso <= 5) or (scommessa == 2 and numero_misterioso > 5):
        print(dizionario[lingua][1], numero_misterioso)
        vittorie += 1
    else:
        print(dizionario[lingua][2], numero_misterioso)
        sconfitte += 1

    if sconfitte >= 10:
        print(dizionario[lingua][3], sconfitte, dizionario[lingua][4], vittorie, dizionario[lingua][5])
        break

    if vittorie >= 10:
        print(dizionario[lingua][6], vittorie, dizionario[lingua][7], sconfitte, dizionario[lingua][5])
        break
