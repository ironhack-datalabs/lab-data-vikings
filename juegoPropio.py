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

# Con esta función añado los equipos a los ejércitos convertidos en Vikings y Saxons con fuerza y salud


def creandoEquipos():
    for v in nombres1:
        vikingTeam.append(Viking(v, 100, random.sample(range(50), 1)))
    for s in nombres2:
        saxonTeam.append(Saxon(s, 100, random.sample(range(50), 1)))

# Como lo dejo a medias, aquí hay unas pruebas para comprobar que crea dos equipos


creandoEquipos()
print("Vikingos")
for i in vikingTeam:
    print(i.__dict__)
print("Sajones")
for i in saxonTeam:
    print(i.__dict__)
