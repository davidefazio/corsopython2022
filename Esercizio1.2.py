# chiedere di inserire quante ore ha lavorato
ore_lavorate = input('Inserisci quante ore hai lavorato: ')
# chiedere di inserire la sua tariffa oraria
paga_oraria = input('Inserisci la tua tariffa oraria: ')

# Stampare paga lorda:  “Con il tuo lavoro hai guadagnato paga_lorda”
paga_lorda = float(ore_lavorate) * float(paga_oraria)  # calcolo paga lorda

print('Con il tuo lavoro hai guadagnato ' + str(paga_lorda))
