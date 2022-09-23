# Creare un set con gli elementi dell’ insieme delle note musicali
# Creare un set con gli elementi dell’ insieme articoli determinativi
# della lingua italiana.
# Mostrare l’unione dei due set
# Mostrare l’intersezione tra i due set
# Mostrare la differenza tra i due set
# Mostrare la intersezione simmetrica tra i due set

# Set note musicali
note = {'DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI'}

# Set articoli determinativi
# Non ho usato questa sintassi
# articoli = set(['IL', 'LO', 'LA', 'I', 'GLI', 'LE'])
# poichè pycharm suggerisce di usare quella abbreviata
articoli = {'IL', 'LO', 'LA', 'I', 'GLI', 'LE'}

# unione dei due set
print('Unione: ', note | articoli)

# intersezione tra i due set
print('Intersezione: ', note & articoli)

# differenza tra i due set
print('Differenza: ', note - articoli)

# intersezione simmetrica tra i due set
print('Intersezione simmetrica: ', note ^ articoli)
