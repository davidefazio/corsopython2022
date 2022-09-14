ore_lavorate = input('Inserisci le ore lavorate: ')
paga_oraria = input('Inserisci la paga oraria: ')
paga_totale = float(ore_lavorate) * float(paga_oraria)
if float(ore_lavorate) > 40:
    paga_totale = (40 * int(paga_oraria)) + ((float(ore_lavorate) - 40) * int(paga_oraria) * 1.5)

print('Ore lavorate: ' + str(ore_lavorate))
print('Tariffa oraria: ' + str(paga_oraria))
print('Paga totale: ' + str(paga_totale))
