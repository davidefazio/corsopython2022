# pyton corso avanzato
# Esercizi
# Lezione 2 - Esercizio 1
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 31/10/22

# Scrivere un programma Python che chiede all’utente di inserire un stringa,
# verifica che questa sia palindroma o non palindroma e stampi a video
# rispettivamente: ‘Stringa inserita è palindroma’ o ‘Stringa inserita non è
# palindroma’. Prima di effettuare il controllo sulla stringa è necessario
# eliminare eventuali spazi bianchi e trasformare la stringa tutta in minuscolo
# (lower case). Stringa test: ‘I topi non avevano nipoti’

stringa = input('inserisci una stringa: ')
stringa_pulita = stringa.lower().replace(" ", "")
stringa_inversa = stringa_pulita[::-1]

for i in range(int(len(stringa_pulita) / 2)):
    if stringa_pulita[i] != stringa_pulita[len(stringa_pulita) - 1 - i]:
        print(stringa, "non è palindroma")
        break
else:
    print(stringa, "è palindroma")
