import vikingsClases as vk 
import random

warInstance = vk.War()
vikingsNames = ["a","b","c"]
nVikings = int(input("How many vikings do you want in your army? "))
nSaxons = int(input("How many saxons do you want in your army? "))
for i in range(nVikings):
    name = random.choice(vikingsNames)
    health = random.uniform(30,50)
    strength = random.uniform(15,30)
    viking = vk.Viking(name,health,strength)
    warInstance.addViking(viking)

for i in range(nSaxons):
    health = random.uniform(40,60)
    strength = random.uniform(10,25)
    saxon = vk.Saxon(health,strength)
    warInstance.addSaxon(saxon)

while warInstance.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    print(warInstance.vikingAttack())
    print(warInstance.saxonAttack())
    status = warInstance.showStatus()
    print(status)


"""
- Generar una batalla

- Variable (war) con los atributos

- Funcion que cree sajones, funcion que cree vikingos

- Una vez tengo la lista de los ejercitos empiezo a pelear hasta que no queden mas vikingos o sajones (con un while)
"""


