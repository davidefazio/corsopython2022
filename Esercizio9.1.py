# Chiedere data di nascita all’utente e chiedere quanti giorni sono passati da quel giorno

from datetime import datetime

datainput = input('inserisic la tua data di nascita nel formato DD/MM/YYYY: ')
data = datetime.strptime(datainput, "%d/%m/%Y")
now = datetime.now()
now_ita = datetime.strftime(now, '%d/%m/%Y')
print(str(now))
diff = now - data
print(f'la differenza in giorni tra la data di nascita inserita ({datainput})',
      f'e la data odierna ({now_ita}) è di {diff.days} giorni')
