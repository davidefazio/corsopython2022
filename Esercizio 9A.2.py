# pyton corso avanzato
# Esercizi
# Lezione 9 - Esercizio 2
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 23/11/22

#  Leggere il contenuto di ogni file creato nella pt.1
#  Verificare che questo numero sia primo o no
#  Se il numero è primo rinominare il file come: numeroprimo.txt (supponendo si legga 7 il file sarà rinominato 7.txt)
#  Se il numero non è primo eliminare il file
#  Dopo aver controllato tutti i file scrivere un file report.txt le seguenti informazioni:
#  numeriPrimi : primi (esempio numeriPrimi : 15)

import os
import shutil


def numero_primo(numero):
    is_numero_primo = True
    for z in range(2, numero):
        modulo = numero % z
        if modulo == 0:
            is_numero_primo = False
            break
    return is_numero_primo


if not os.path.exists('numeri_primi_temp'):
    os.system('mkdir numeri_primi_temp')

count_numeri_primi = 0

for i in os.listdir('numeri_primi'):
    f = open('numeri_primi/' + i, 'r')
    num = int(f.read().splitlines()[0])
    f.close()
    if numero_primo(num) and not os.path.exists('numeri_primi_temp/' + str(num) + '.txt'):
        f1 = open('numeri_primi_temp/' + str(num) + '.txt', 'w')
        f1.write(str(num))
        f1.close()
        count_numeri_primi += 1
    os.remove('numeri_primi/' + i)

f = open('numeri_primi/report.txt', 'w')
f.write('numeriPrimi : ' + str(count_numeri_primi))
f.close()

for i in os.listdir('numeri_primi_temp'):
    src = 'numeri_primi_temp/' + i
    dst = 'numeri_primi'
    shutil.move(src, dst)

os.system('rm -r numeri_primi_temp')
