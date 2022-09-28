password = 'Password_sicura'

tuo_username = input('Inserisci il tuo nome utente: ')
tua_password = input('Inserisci la tua password: ')
messaggio = 'Password non corretta'
if tua_password == password:
    messaggio = 'Ciao ' + tuo_username

print(messaggio)
