# Create un file di testo tramite python con 10 righe di nomi e cognomi
# Aggiungete tramite codice il sig. “Mario Ultimo”
# Leggete i primi tre nominativi da codice
# Creare manualmente una directory con dentro un file ed eliminare ambedue da codice

import os

lista_persone = ['Mario Rossi', 'Mario Bianchi', 'Mario Neri', 'Mario Verde', 'Mario Blu',
                 'Giuseppe Rossi', 'Giuseppe Bianchi', 'Giuseppe Neri', 'Giuseppe Blu']
f = open('file_esempio.txt', 'w')
for value in lista_persone:
    f.write(value)
    f.write('\n')

f.close()
f = open('file_esempio.txt', 'a')
f.write('Mario Ultimo')
f.write('\n')
f.close()

f = open('file_esempio.txt', 'r')
righe_di_testo = f.read().splitlines()
f.close()

print(righe_di_testo[0:3])
print(righe_di_testo[0])
print(righe_di_testo[1])
print(righe_di_testo[2])

if not os.path.exists('dir_esempio'):
    os.system('mkdir dir_esempio')

f = open('dir_esempio/file_esempio2.txt', 'w')
f.write('Mario Ultimo')
f.close()

if os.path.exists('dir_esempio/file_esempio2.txt'):
    os.remove('dir_esempio/file_esempio2.txt')
    os.system('rm -r dir_esempio')
