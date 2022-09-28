# In una sesione di esami gli studenti hanno preso i seguenti voti: 29,
# 18, 18, 25, 28, 27, 19, 30, 20
# Calcolare e mostrare la media aritmetica
# Calcolare la mediana, il valore centrale (se i valori sono in numero
# pari la media dei due valori centrali)
# Calcolare la moda, la tendenza centrale.

import statistics

voti = (29, 18, 18, 25, 28, 27, 19, 30, 20)

# Calcolare e mostrare la media aritmetica
print('La media dei voti è', statistics.mean(voti))

print('La mediana dei voti è', statistics.median(voti))

print('La moda dei voti è', statistics.mode(voti))
