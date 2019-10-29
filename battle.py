from vikingsClases import War
from vikingsClases import Viking
from vikingsClases import Saxon
import random
batalla = War()
batalla.addViking(Viking('Julito', 99, 130))
batalla.addViking(Viking('Tu_pana_sincero_93', 88, 120))
batalla.addViking(Viking('El Rober', 78, 160))
batalla.addSaxon(Saxon(89, 178))
batalla.addSaxon(Saxon(98, 189))
batalla.addSaxon(Saxon(88, 176))
batalla.addViking(Viking('Tu_nene', 123, 130))
ataque1 = batalla.vikingAttack
ataque2 = batalla.saxonAttack
lista = [ataque1, ataque2]

#imposible más aleatoriedad...
while len(batalla.vikingArmy) != 0 and len(batalla.saxonArmy) != 0:
    random.choice(lista)()
    print(batalla.showStatus())

#los vikingos siempre empiezan
'''while True:
    batalla.vikingAttack()
    print(batalla.showStatus())
    if len(batalla.vikingArmy) == 0 or len(batalla.saxonArmy) == 0:
        break
    batalla.saxonAttack()
    print(batalla.showStatus())
    if len(batalla.vikingArmy) == 0 or len(batalla.saxonArmy) == 0:
        break
    '''
