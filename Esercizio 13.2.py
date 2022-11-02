# pyton corso base
# Esercizi
# Lezione 13 - Esercizio 2
# Test
# Autore: davide.fazio
# Email: fazio@olomedia.it
# Creato il 02/11/22

# Realizzare un test tramite Unit Test

import unittest


def numero_primo(numero):
    is_numero_primo = True
    for i in range(2, numero):
        modulo = numero % i
        if modulo == 0:
            is_numero_primo = False
            break
    return is_numero_primo


# assert numero_primo(2) == True, "Dovrebbe essere Vero"
# assert numero_primo(5) == True, "Dovrebbe essere Vero"
# assert numero_primo(6) == False, "Dovrebbe essere Falso"
class TestNumeroPrimo(unittest.TestCase):

    def test_is_numero_primo(self):
        self.assertTrue(numero_primo(2))
        self.assertTrue(numero_primo(5))
        self.assertFalse(numero_primo(6))


unittest.main()
