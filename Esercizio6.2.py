# Realizzare un piccolo script di controllo dello stato del sito
# google.com che effettui il ping 10 volte.

import os

print(os.system('ping google.com -c 10'))