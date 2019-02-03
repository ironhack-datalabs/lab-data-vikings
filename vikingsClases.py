#Project lab-data-vikings


# Soldier (constructor, ataque y daño)
class Soldier:
  #Constructor: contiene las propiedades self, health y strength
  def __init__(self, health, strength):
    self.health = healt
    self.strength = strength
  #Método 'attack' no recive ninguna variable aparte de self. Este método devuelve la propiedad 'strength'.
  def attack(self):
    return self.strength
  #Método 'receiveDamage' recibe la variable daño ('skadi') la cual afecta a la propiedad 'health'
  def receiveDamage(self, skadi):
    self.health = self.health - skadi

# Viking
class Viking:
  pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
