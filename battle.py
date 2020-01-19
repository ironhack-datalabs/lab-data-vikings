import vikingsClases as v
import random as rd
import time as t
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
for i in range(1, 4):
    t.sleep(0.75)
    print(f"{i}............")
t.sleep(0.75)
print("Gooooo")

while 1:
    t.sleep(1)
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
        print(f"{war.showStatus()}")
        print("WAR IS OVER!!!")
        print("LET'S CELEBRATE")
        break

t.sleep(2)
animation = pyglet.image.load_animation("vikingRave.gif")
animSprite = pyglet.sprite.Sprite(animation)
w = animSprite.width
h = animSprite.height
window = pyglet.window.Window(width=w, height=h, fullscreen=True1)
window.set_visible(True)
r, g, b, alpha = 0.5, 0.5, 0.8, 0.5
pyglet.gl.glClearColor(r, g, b, alpha)
music = pyglet.resource.media("celebrate.mp3", streaming=False)
music.play()

@window.event
def on_draw():
    window.clear()
    animSprite.draw()

pyglet.app.run()