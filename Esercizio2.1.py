tuo_nome = input('Inserisci il tuo nome: ')
tua_eta = input('Inserisci la tua età: ')
maggiorenne_minorenne = 'maggiorenne'
if int(tua_eta) < 18:
    maggiorenne_minorenne = 'minorenne'

print('Ciao ' + tuo_nome + ' benvenuto, sei ' + maggiorenne_minorenne)
