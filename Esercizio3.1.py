# dichiara una variabile mia_eta e valorizzala
mia_eta = 43
# dichiara una variabile mio_nome e inserisci il tuo nome
mio_nome = 'Davide'
# stampa sul terminale il messaggio:
# "Ciao sono mio_nome ed ho mia_eta, ti dò l benvenuto"
print('Ciao sono ' + mio_nome + ' e ho ' + str(mia_eta) + ' anni, ti dò il benvenuto')

# chiedi all'utente il suo nome e la sua età
tuo_nome = input('Inserisci il tuo nome: ')
tua_eta = input('Inserisci la tua età: ')

# stampa a video il seguente messaggio:
# "Ciao tuo_nome benvenuto, sai che la somma della tua età e della mia età è somma_eta"
somma_eta = mia_eta + int(tua_eta)  # Calcolo somma_eta
print('Ciao ' + tuo_nome + ' benvenuto, sai che la somma della tua età e della mia età è ' + str(somma_eta))
