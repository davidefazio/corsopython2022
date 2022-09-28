# Generare una stringa alfanumerica di 8 caratteri se l'utente vuole
# una password semplice, o di 20 caratteri qualora desideri una
# password più complicata. I primi due caratteri della password
# generata devono essere date dal giorno della nascita.

from datetime import datetime
import string
import random

datainput = input('inserisic la tua data di nascita nel formato DD/MM/YYYY: ')
pwd_type = input('vuoi generare una password semplice o complessa: 1=Semplice, 2=Complessa ')
data = datetime.strptime(datainput, "%d/%m/%Y")
giorno_nascita = datetime.strftime(data, '%d')
now = datetime.now()

length_of_string = 6
if pwd_type == '2':
    length_of_string = 18

password = str(giorno_nascita) + \
           ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
length_of_password = len(password)
print(f'la password generata è {password} e la sua lunghezza è {length_of_password} caratteri')
