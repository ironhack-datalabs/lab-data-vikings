from vikingsClases import War
from vikingsClases import Viking
from vikingsClases import Saxon
import random



guerra = War()
nombres_vikingos = ['Aren','Axe','Bjorn','Daven','Egil','Einar','Erik','Esben','Gerd','Gisli','Haakon','Helge','Hans',\
    'Harald','Ivar','Jensen','Jorgen','Lars','Niels','Olav','Olson','Olson','Sveinn','Thor','Viggo']

v = Viking(random.choice(nombres_vikingos),100,30)
s = Saxon(100,20)

print(v)
print(s)

#print(guerra)