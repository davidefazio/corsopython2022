# Utilizzare e documentare tre funzioni built in all’interno
# di un software e commentarne il suo utilizzo

valore1 = 'test'
valore2 = 'esempio'

# la funzione hash restituisce un codice random intero relativo al valore di input
hash1 = hash(str(valore1))
print('L\'hash di ' + str(valore1) + ' è ' + str(hash1))
hash2 = hash(str(valore2))
print('L\'hash di ' + str(valore2) + ' è ' + str(hash2))

if hash1 < hash2:
    print('L\'hash di "' + valore2 + '" è maggiore dell\'hash di "' + valore1 + '" ')
else:
    print('L\'hash di "' + valore2 + '" è minore dell\'hash di "' + valore1 + '" ')

print()

# la funzione help restituisce la descrizione di una funzione passata in input e la stampa a video
# nello specifico ho richiesto l'help della funzione hash precedentemente utilizzata
help('hash')
# di seguito il valore restituito dall'help di hash
# Help on built-in function hash in module builtins:
#
# hash(obj, /)
#     Return the hash value for the given object.
#
#     Two objects that compare equal must also have the same hash value, but the
#     reverse is not necessarily true.

print()

# la funzione iter permette di scorrere un elemento con più valori come una lista
# nell'esempio definita una lista stampo i valori che la contengono
# corrisponde al foreach in altri linguaggi
lista = [10, 100, 1000]
for value in iter(lista):
    print(str(value))
