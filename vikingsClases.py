#Project lab-data-vikings


# Soldier (constructor, ataque y daño)
class Soldier:
  
  #Constructor: contiene las propiedades self, health y strength
  def __init__(self, health, strength):
    self.health = health
    self.strength = strength
  
  #Método 'attack' no recive ninguna variable aparte de self. Este método devuelve la propiedad 'strength'.
  def attack(self):
    return self.strength
  
  #Método 'receiveDamage' recibe la variable daño ('skadi') la cual afecta a la propiedad 'health'
  def receiveDamage(self, skadi):
    self.health = self.health - skadi



# Viking
class Viking(Soldier):
  
  #Constructor: hereda de Soldier las propiedades health y strength e incorpora adicionalmente la propiedad name.
  def __init__(self, name, health, strength):
    super().__init__(health, strength)
    self.name = name
  
  #Método 'attack' se hereda de soldier.
  def attack(self):
    return super().attack
  
  #Método 'receiveDamage' recibe la variable daño ('skadi') la cual afecta a la propiedad 'health'. Adicionalmente este método devuelve un mensaje en función del estado del vikingo (si 'health' <= 0 es que ha muerto).
  def receiveDamage(self, skadi):
    self.health = self.health - skadi
    if self.health > 0:
      return ('{} has received {} points of damage').format(self.name, skadi)
    elif self.health <= 0:
      return ('{} has died in act of combat').format(self.name)
  
  #Método 'battleCry' devuelve el grito de guerra de los vikingos.
  def battleCry(self):
    return 'Odin Owns You All!'



# Saxon


class Saxon:
    pass

# War


class War:
    pass
