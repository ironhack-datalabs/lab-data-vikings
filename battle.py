from vikingsClases import War
from vikingsClases import Viking
from vikingsClases import Saxon

war = War()

war.addViking(Viking('Pepeluis', 45, 80))
war.addViking(Viking('Victorina', 30, 95))
war.addViking(Viking('Blanca', 3, 487))
war.addViking(Viking('Alvaro Cotelo', 100, 14))

war.addSaxon(Saxon(120, 50))
war.addSaxon(Saxon(20, 89))
war.addSaxon(Saxon(97, 80))

print(war.vikingAttack())
print(war.saxonAttack())
print(war.vikingAttack())
print(war.saxonAttack())
print(war.vikingAttack())
print(war.saxonAttack())
print(war.showStatus())