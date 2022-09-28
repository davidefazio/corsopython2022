# Chiedere data di nascita ad un utente e calcolare se è  maggiorenne o minorenne

from datetime import datetime

datainput = input('inserisic la tua data di nascita nel formato DD/MM/YYYY: ')
data = datetime.strptime(datainput, "%d/%m/%Y")
now = datetime.now()
now_ita = datetime.strftime(now, '%d/%m/%Y')
diff = now - data
if diff.days / 365 > 18:
    print('Sei Maggiorenne')
else:
    print('Sei Minorenne')
