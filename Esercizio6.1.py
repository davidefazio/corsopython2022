# Creare una lista ed una tupla
# contare gli elementi contenuti in ambedue.
# Convertire la lista in tupla e la tupla in lista

# Creo una lista
lista_voti = [24, 22, 30, 18, 25]

# aggiungo un elemento alla lista
lista_voti.append(28)

# Creo una tupla
tupla_voti = (24, 22, 30, 18, 25)

# Conto gli elementi della lista
print('Numero di elementi della lista voti: ' + str(len(lista_voti)))

# Conto gli elementi della tupla
print('Numero di elementi della tupla voti: ' + str(len(tupla_voti)))

# converto la lista_voti in una tupla
tupla_lista_voti = tuple(lista_voti)

# converto la tupla_voti in una lista
lista_tupla_voti = list(tupla_voti)

# effettuo una operazione di lista sulla lista ottenuta dalla tupla
lista_tupla_voti.pop(1)

# Stampo la nuova lista
print('nuova lista: ' + str(lista_tupla_voti))
