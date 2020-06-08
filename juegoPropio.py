import unittest
import random
from equiposClases import War
from equiposClases import Viking
from equiposClases import Saxon
from inspect import signature
# Lista con todos los nombres
nombres = ["Miguel_Ceinos", "Eduardo_Vill", "Laura", "Patricia", "Xabier", "Cristina", "Santi", "Irene", "Ricardo_Alf", "Fernando", "Guille_Diego", "María", "Jose_Vidal",
           "Eduardo_Garo", "Marlena", "Guille_Mart", "Alex_Vidal", "Iván", "Sergio", "Elisa", "Amanda", "Héctor", "Jose_Pérez", "Fabián", "Marc", "Clara", "Blanca", "Fran", "Felipe"]

vikingTeam = []
saxonTeam = []
# Aquí es donde realmente se hacen los equipos
nombres1 = list(random.sample(nombres, int(len(nombres)/2)))
nombres2 = [i for i in nombres if i not in nombres1]
empieza = ""
# Con esta función añado los equipos a los ejércitos convertidos en Vikings y Saxons con fuerza y salud


def creandoEquipos():
    for v in nombres1:
        vikingTeam.append(Viking(v, 10, random.choice(range(5, 15))))
    for s in nombres2:
        saxonTeam.append(Saxon(s, 10, random.choice(range(5, 15))))


def vikAttack():
    sax = random.choice(saxonTeam)
    vik = random.choice(vikingTeam)
    vikatt = sax.receiveDamage(vik.strength)
    print("Turno Vikingo")
    print("{} ataca a {} con fuerza {}".format(
        vik.name, sax.name, vik.strength))
    if sax.health <= 0:
        saxonTeam.remove(sax)
        print("{} ha muerto".format(sax.name))
    else:
        print("La vida de {} ahora es {}".format(sax.name, sax.health))
    # return vikatt


def saxAttack():
    sax = random.choice(saxonTeam)
    vik = random.choice(vikingTeam)
    saxatt = vik.receiveDamage(sax.strength)
    print("Turno Sajón")
    print("{} ataca a {} con fuerza {}".format(
        sax.name, vik.name, sax.strength))
    if vik.health <= 0:
        vikingTeam.remove(vik)
        print("{} ha muerto".format(vik.name))
    else:
        print("La vida de {} ahora es {}".format(vik.name, vik.health))
    # return saxatt


def eligeInicio():
    global empieza
    empieza = input("Introduce V o S para empezar el juego  ")
    return empieza


def empiezaVik():
    while True:
        vikAttack()
        if len(vikingTeam) == 0 or len(saxonTeam) == 0:
            break
        saxAttack()
        print("Quedan {} sajones y {} vikingos".format(
            len(saxonTeam), len(vikingTeam)))
        if len(vikingTeam) == 0 or len(saxonTeam) == 0:
            break


def empiezaSax():
    while True:
        saxAttack()
        if len(vikingTeam) == 0 or len(saxonTeam) == 0:
            break
        vikAttack()
        print("Quedan {} sajones y {} vikingos".format(
            len(saxonTeam), len(vikingTeam)))
        if len(vikingTeam) == 0 or len(saxonTeam) == 0:
            break


def muestraGana():
    if len(vikingTeam) > len(saxonTeam):
        print("Vikingos ganan")
        for i in vikingTeam:
            print("Superviviente: ", i.__dict__)
    else:
        print("Sajones ganan")
        for i in saxonTeam:
            print("Superviviente: ", i.__dict__)


creandoEquipos()

print("Vikingos")
for i in vikingTeam:
    print(i.__dict__)

print("Sajones")
for i in saxonTeam:
    print(i.__dict__)

eligeInicio()

if empieza == "v":
    empiezaVik()
else:
    empiezaSax()

muestraGana()
