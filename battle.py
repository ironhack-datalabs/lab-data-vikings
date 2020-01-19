import vikingsClases as v
import random as rd
import pyglet

def randomNumber():
    return rd.randint(1, 10)

while 1:
    try:
        numberSaxon = int(input("Number of Saxons: "))
        numberVikings = int(input("Number of Vikings: "))
        if numberSaxon == 0 or numberVikings == 0:
            print("Debe introduccir un número mayor que 0")
            continue
        break
    except Exception as e:
        print("Se debe introduccir un número")

war = v.War()
for i in range(0, numberSaxon):
    war.addViking(v.Viking(f"Viking-{i + 1}", randomNumber(), randomNumber()))
    war.addSaxon(v.Saxon(randomNumber(), randomNumber()))

contador = 1
while 1:
    print(f"{contador}- War")
    print("-----")
    contador += 1
    whoFight = randomNumber()
    if whoFight < 5:
        print(war.saxonAttack())
    if whoFight >= 5:
        print(war.vikingAttack())
    print("-----\n")
    if len(war.saxonArmy) == 0 or len(war.vikingArmy) == 0:
        print("WAR IS OVER!!!")
        print(f"{war.showStatus()}\n")
        break
    print(f"{war.showStatus()}\n")
ag_file = "giphy.gif"
animation = pyglet.resource.animation(ag_file)
sprite = pyglet.sprite.Sprite(animation)
win = pyglet.window.Window(width=sprite.width, height=sprite.height)




