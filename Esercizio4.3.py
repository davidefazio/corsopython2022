tuo_nome = input('Inserisci il tuo nome: ')
tua_eta = input('Inserisci la tua età: ')
password = 'Password_sicura'
maggiorenne_minorenne = 'maggiorenne'
if int(tua_eta) < 18:
    print('Ciao ' + tuo_nome + ', non puoi accedere perché minorenne')
else:
    print('Ciao ' + tuo_nome + ' benvenuto.')
    tua_password = input('Inserisci la tua password: ')
    messaggio = 'Password non corretta'
    if tua_password == password:
        messaggio = 'Ciao ' + tuo_nome
    print(messaggio)
