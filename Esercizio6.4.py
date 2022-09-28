# Scrivere un applicazione che data una lista di voti
# (numeri interi) trova il voto più basso

# Creo una lista
lista_voti = [24, 22, 30, 18, 25, 28]

# ciclo la lista_voti per trovare il valore più basso
voto_basso = 100
for value in iter(lista_voti):
    if value < voto_basso:
        voto_basso = value

print('Il voto più basso usando i cicli è : ' + str(voto_basso))

print('Il voto più basso usando la funzione built in min è: ' + str(min(lista_voti)))

lista_voti.sort()
print('Il voto più basso usando il metodo sort delle liste è: ' + str(lista_voti[0]))
