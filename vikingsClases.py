import random
# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        self.kills = 0

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        self.isBerserker = False

    #attack se hereda automaticamente

    def __repr__(self):
        s = "["
        if self.isBerserker:
            s += '⚔ '
        s += self.name+"] "+"HP: "+str(self.health)+" AT: "+str(self.strength)
        if self.kills > 0:
            s += " ☠ "+str(self.kills)
        return s
    
    def becomeBerserker(self):
        self.isBerserker = True
        self.health = 250
        self.strength = 80

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if(self.health > 0):
            return self.name+" has received "+str(damage)+" points of damage"
        else:
            return self.name+" has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    #attack se hereda automaticamente
    def __repr__(self):
        s = "[a saxon] "+"HP: "+str(self.health)+" AT: "+str(self.strength)
        if self.kills > 0:
            s += " ☠ "+str(self.kills)
        return s

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if(self.health > 0):
            return "A Saxon has received "+str(damage)+" points of damage"
        else:
            return "A Saxon has died in combat"

# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def __repr__(self):
        s = "\n-----Standing battle members:-----\n"
        for i in self.vikingArmy:
            s += str(i) + '\n'
        print('\n\n')
        for j in self.saxonArmy:
            s += str(j) + '\n'
        return s

    def addViking(self,viking):
        self.vikingArmy.append(viking)

    def removeFirstViking(self):
        self.vikingArmy.remove(self.vikingArmy[0])

    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        viki = random.randint(0,len(self.vikingArmy)-1)
        saxo = random.randint(0,len(self.saxonArmy)-1)
        resultado = self.saxonArmy[saxo].receiveDamage(self.vikingArmy[viki].attack())
        if(resultado[-1] == "t"):
            self.saxonArmy.remove(self.saxonArmy[saxo])
            self.vikingArmy[viki].kills += 1
        return resultado

    def saxonAttack(self):
        viki = random.randint(0,len(self.vikingArmy)-1)
        saxo = random.randint(0,len(self.saxonArmy)-1)
        resultado = self.vikingArmy[viki].receiveDamage(self.saxonArmy[saxo].attack())
        if(resultado[-1] == "t"):
            self.vikingArmy.remove(self.vikingArmy[viki])
            self.saxonArmy[saxo].kills += 1
        return resultado

    def showStatus(self):
        if(len(self.saxonArmy) == 0):
            return "Vikings have won the war of the century!"
        elif(len(self.vikingArmy) == 0):
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    
    def heroesOfWar(self):
        if(len(self.saxonArmy) != 0):
            print("This battle will be long remembered...")
        elif(len(self.vikingArmy) != 0):
            remain = self.vikingArmy[0]
            for i in self.vikingArmy:
                if remain.kills < i.kills:
                    remain = i
            print("This battle will always be remembered as THE BATTLE OF MIGHTY "+str.upper(remain.name)+"\n")
        else:
            print("---")
        
    def vikingAttackCow(self):
        viki = random.randint(0,len(self.vikingArmy)-1)
        saxo = 0
        for i in range(len(self.saxonArmy)):
            if self.saxonArmy[saxo].health > self.saxonArmy[i].health:
                saxo = i
        resultado = self.saxonArmy[saxo].receiveDamage(self.vikingArmy[viki].attack())
        if(resultado[-1] == "t"):
            self.saxonArmy.remove(self.saxonArmy[saxo])
            self.vikingArmy[viki].kills += 1
        return resultado

    def saxonAttackCow(self):
        saxo = random.randint(0,len(self.saxonArmy)-1)
        viki = 0
        for i in range(len(self.vikingArmy)):
            if self.vikingArmy[viki].health > self.vikingArmy[i].health:
                viki = i
        resultado = self.vikingArmy[viki].receiveDamage(self.saxonArmy[saxo].attack())
        if(resultado[-1] == "t"):
            self.vikingArmy.remove(self.vikingArmy[viki])
            self.saxonArmy[saxo].kills += 1
        return resultado

    def vikingAttackStrong(self):
        viki = 0
        for i in range(len(self.vikingArmy)):
            if self.vikingArmy[viki].strength < self.vikingArmy[i].strength:
                viki = i
        saxo = 0
        for i in range(len(self.saxonArmy)):
            if self.saxonArmy[saxo].strength < self.saxonArmy[i].strength:
                saxo = i
        resultado = self.saxonArmy[saxo].receiveDamage(self.vikingArmy[viki].attack())
        if(resultado[-1] == "t"):
            self.saxonArmy.remove(self.saxonArmy[saxo])
            self.vikingArmy[viki].kills += 1
        return resultado

    def saxonAttackStrong(self):
        saxo = 0
        for i in range(len(self.saxonArmy)):
            if self.saxonArmy[saxo].strength < self.saxonArmy[i].strength:
                saxo = i
        viki = 0
        for i in range(len(self.vikingArmy)):
            if self.vikingArmy[viki].health > self.vikingArmy[i].health:
                viki = i
        resultado = self.vikingArmy[viki].receiveDamage(self.saxonArmy[saxo].attack())
        if(resultado[-1] == "t"):
            self.vikingArmy.remove(self.vikingArmy[viki])
            self.saxonArmy[saxo].kills += 1
        return resultado



class Teacher(Viking):
    def __init__(self, name, health, strength):
        super().__init__(name, health, strength)
    
    def receiveDamage(self, damage):
        return super().receiveDamage(damage)
    
    def becomeBerserker(self):
        super().becomeBerserker()

class Alumn(Viking):
    def __init__(self, name, health, strength):
        super().__init__(name, health, strength)
    
    def receiveDamage(self, damage):
        return super().receiveDamage(damage)


class BootcampWar:
    def __init__(self):
        self.teachersArmy = []
        self.alumnsArmy = []

    def __repr__(self):
        s = "\n-----Standing battle members:-----\n"
        for i in self.teachersArmy:
            s += str(i) + '\n'
        print('\n\n')
        for j in self.alumnsArmy:
            s += str(j) + '\n'
        return s

    def addTeacher(self,teacher):
        self.teachersArmy.append(teacher)

    def addAlumn(self,alumn):
        self.alumnsArmy.append(alumn)

    def alumnAttack(self):
        alu = random.randint(0,len(self.alumnsArmy)-1)
        tea = random.randint(0,len(self.teachersArmy)-1)
        resultado = self.teachersArmy[tea].receiveDamage(self.alumnsArmy[alu].attack())
        if(resultado[-1] == "t"):
            self.teachersArmy.remove(self.teachersArmy[tea])
            self.alumnsArmy[alu].kills += 1
        return resultado

    def teacherAttack(self):
        alu = random.randint(0,len(self.alumnsArmy)-1)
        tea = random.randint(0,len(self.teachersArmy)-1)
        resultado = self.alumnsArmy[alu].receiveDamage(self.teachersArmy[tea].attack())
        if(resultado[-1] == "t"):
            self.alumnsArmy.remove(self.alumnsArmy[alu])
            self.teachersArmy[tea].kills += 1
        return resultado

    def showStatus(self):
        if(len(self.teachersArmy) == 0):
            return "Alumns have won the war of the century!"
        elif(len(self.alumnsArmy) == 0):
            return "Teachers suspended the whole class"
        else:
            return "Alumns and Teachers are still in the thick of battle."

    def heroesOfWar(self):
        if(len(self.alumnsArmy) != 0):
            remain = self.alumnsArmy[0]
            for i in self.alumnsArmy:
                if remain.kills < i.kills:
                    remain = i
            print("ALL HAIL "+str.upper(remain.name)+"!\n")
        elif(len(self.teachersArmy) != 0):
            remain = self.teachersArmy[0]
            for i in self.teachersArmy:
                if remain.kills < i.kills:
                    remain = i
            print(str.upper(remain.name)+" has been a pain in the ass for us\n")
        else:
            print("---")