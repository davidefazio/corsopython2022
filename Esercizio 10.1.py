# pyton corso base
# Esercizi
# Lezione 10 - Esercizio 1
# Classi
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 05/10/22

# Creare una classe Cane con attributi: nome, razza, eta
# creare metodi per delle funzionalita di base, come ad esempio
# mangia e abbaia, fai i bisogni ("Gnam Gnam", "Bau Bau" ."pupù e pipi"

# instanzio la classe Cane con i relativi metodi
class Cane:
    def __init__(self, nome, razza, eta):
        # self allows to attach parameter to the class
        self.nome = nome
        self.razza = razza
        self.eta = eta

    @staticmethod
    def mangia():
        print('Gnam Gnam')

    @staticmethod
    def abbaia():
        print('Bau Bau')

    @staticmethod
    def bisogni():
        print('pupù e pipi')


# Creo oggetto mio_cane della classe Cane
mio_cane = Cane('Bob', 'Pastore', 3)
# Stampo gli attributi di mio_cane
print('Nome:', mio_cane.nome)
print('Razza:', mio_cane.razza)
print('Età: ', mio_cane.eta)

# Utilizzo i metodi direttamente sulla classe visto che sono statici
Cane.mangia()
Cane.abbaia()
Cane.bisogni()
