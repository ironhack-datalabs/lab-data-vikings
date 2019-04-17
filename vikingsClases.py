
# Soldier
class Soldier():
	def __init__(self, health, strength):
		self.health=health
		self.strength=strength
	
	def attack(self):
		return self.strength
		
	def receiveDamage(self, damage):
		self.health-=damage
			
		
		


# Viking
class Viking(Soldier):
	def __init__(self, name, health, strength):
		self.name=name
		self.health=health
		self.strength=strength



'''
# Saxon
class Saxon(Soldier):
	def __init__(self, health, strength):
		self.health=health
		self.strength=strength



# War
class War:
	pass
'''
