# Creare un dizionario ed eseguire le seguenti operazioni
# Ordinare in funzione delle chiavi
# Ordinare in funzione dei valori
# Verificare se un elemento è presente nel dizionario
# Estrarre chiavi, Estrarre valori
# Modificare chiavi, Modificare valori
# Aggiungere una nuova coppia chiave/valore
# Eliminare una chiave da un dizionario
# Eliminare un valore da un dizionario

import operator
import collections

# Creao il dizionario dei colori
dizionario = {'red': 'rosso', 'green': 'verde', 'blue': 'blu', 'yellow': 'giallo',
              'white': 'bianco', 'black': 'nero', 'gray': 'grigio'}

# Ordinare in funzione delle chiavi
dizionario_ordinato_chiavi = {}
# estraggo la lista di chiavi e la ordino
chiavi = list(dizionario.keys())
chiavi.sort()

# scorro la lista delle chiavi per ordinare i valori
for chiave in chiavi:
    dizionario_ordinato_chiavi[chiave] = dizionario[chiave]

# mostro il contenuto del dizionario ordinato per il valore della chiave
print('Dizionario ordinato per chiavi', dizionario_ordinato_chiavi)

# Ordinare in funzione dei valori
dizionario_ordinato_valori = dict(sorted(dizionario.items(), key=operator.itemgetter(1)))
print('Dizionario ordinato per valori (modalita1)', dizionario_ordinato_valori)

dizionario_ordinato_valori2 = dict(collections.OrderedDict(sorted(dizionario.items(), key=lambda x: x[1])))
print('Dizionario ordinato per valori (modalita2)', dizionario_ordinato_valori2)

# Verificare se un elemento è presente come chiave nel dizionario
print('l\'elemento rosso è presente nelle chiavi?', 'rosso' in dizionario)
print('l\'elemento red è presente nelle chiavi?', 'red' in dizionario)

# Verificare se un elemento è presente come valore nel dizionario
print('l\'elemento rosso è presente nei valori?', 'rosso' in list(dizionario.values()))
print('l\'elemento red è presente nei valori?', 'red' in list(dizionario.values()))

# Estrarre chiavi, Estrarre valori
chiavi = list(dizionario.keys())
valori = list(dizionario.values())
print('chiavi:', chiavi)
print('valori:', valori)

# Aggiungere una nuova coppia chiave/valore
dizionario["orange"] = "arancione"
print('Dizionario dopo aver aggiunto orange:arancione', dizionario)

# Eliminare una chiave da un dizionario
del dizionario["orange"]
print('Dizionario dopo aver eliminato la chiave orange', dizionario)
dizionario.pop('gray', 0)
print('Dizionario dopo aver eliminato la chiave orange', dizionario)

# Eliminare un valore da un dizionario
remove = [k for k in dizionario.keys() if dizionario[k] == 'blu']
for key in remove:
    del dizionario[key]

print('Dizionario dopo aver eliminato il valore blu', dizionario)
