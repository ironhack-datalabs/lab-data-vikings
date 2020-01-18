from vikingsClases import BootcampWar
from vikingsClases import Teacher
from vikingsClases import Alumn
import random

# Generar ejércitos (pedir por teclado cantidad o hacer random)
# generar salud y fuerza aleatorias entre un minimo y un maximo
# preguntar quién inicia el conflicto
# Hacer métodos de representación para las clases (poder hacer print de un soldado y del estado de los ejercitos)
# versión "coward mode" de VikingAttack y SaxonAttack en los que, en lugar de elegirlos de forma aleatoria, sea el más fuerte el que ataque al contrario de menos salud


nombres_TAs = ['Felipe','Blanca','Clara','Fran']
nombres_alumnos = ['Jose','Jose','Patri','Miguel','Eduardo','Ricardo','Fer','Alex','Santi','Guille','Irene','Elisa',\
    'Cristina','Sergio','Laura','Fabian','Guillermo','Eduardo','Maria','Amanda','Xabier','Marlena','Iván','Héctor']

'''
def askArmySize():
    while True:
        try:
            tam = int(input("How many soldiers will fight for each army? (max 10) -> "))
            if tam > 0:
                return tam
            else:
                raise Exception
        except:
            print('invalid value. try again')

def askWhichOneStarts():
    while True:
        try:
            ini = input("Who will start the war? [t/a] -> ")
            if ini not in ("t","a"):
                raise NameError("Not in [t/a]")
            else:
                return ini
        except:
            print('invalid value. try again')
'''
def generateArmies(g):
    for i in nombres_TAs:
        g.addTeacher(Teacher(i,random.randint(1,51)+50,random.randint(1,11)+25))
    for i in g.teachersArmy:
        i.becomeBerserker()
    for j in nombres_alumnos:
        g.addAlumn(Alumn(j,random.randint(1,51)+50,random.randint(1,16)+25))


def battle(g,turno):
    while len(g.teachersArmy) != 0 and len(g.alumnsArmy) != 0:
        if(turno=="t"):
            g.teacherAttack()
            turno="a"
        else:
            g.alumnAttack()
            turno="t"
        print(g)
        #print(g.showStatus())
        try:
            input("Press enter to continue")
        except SyntaxError:
            pass

guerra = BootcampWar()

#n = askArmySize()
generateArmies(guerra)
print(guerra)
emp = "a" #askWhichOneStarts()
if emp == "a":
    print("Alumns will start the war")
else:
    print("Teachers will start the war")

battle(guerra,emp)
print(guerra.showStatus())
guerra.heroesOfWar()



