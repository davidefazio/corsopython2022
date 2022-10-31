# pyton corso avanzato
# Esercizi
# Lezione 2 - Esercizio 2
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 31/10/22

# Scrivere un programma Python che chiede all’utente di inserire un stringa,
# verifica che questa sia palindroma o non palindroma e stampi a video
# rispettivamente: ‘Stringa inserita è palindroma’ o ‘Stringa inserita non è
# palindroma’. Prima di effettuare il controllo sulla stringa è necessario
# eliminare eventuali spazi bianchi e trasformare la stringa tutta in minuscolo
# (lower case). Stringa test: ‘I topi non avevano nipoti’

# Scrivere il programma precedente senza l’utilizzo di cicli for o while

stringa = input('inserisci una stringa: ')
stringa_pulita = stringa.lower().replace(" ", "")
stringa_inversa = stringa_pulita[::-1]

if stringa_pulita == stringa_inversa:
    print(stringa, "è palindroma")
else:
    print(stringa, "non è palindroma")
