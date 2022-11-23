# pyton corso avanzato
# Esercizi
# Lezione 9 - Esercizio 1
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 23/11/22

# Scrivi il programma python che:
#  Crea un nuova directory ‘numeri_primi’ su una directory già esistente da te scelta
#  Crea all’interno della nuova directory 50 file txt nominati da 1 a 50 (ex 1.txt, 2.txt, 3.txt, … 50.txt)
#  Scrive un numero casuale all’interno di ciascun file (numero compreso tra 2 e 9999)

import os
from random import randrange


if not os.path.exists('numeri_primi'):
    os.system('mkdir numeri_primi')

for i in range(1, 51):
    f = open('numeri_primi/' + str(i) + '.txt', 'w')
    numero = randrange(2, 10000)
    f.write(str(numero))
    f.close()
