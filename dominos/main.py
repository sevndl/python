from Domino import *

d1 = Domino(4, 3)
d2 = Domino(3, 5)

print(d1.getMarqueGauche())
print(d1.getMarqueDroite())
print(d1.getValeur())
print(d1.afficher())
d1.inverser()
print(d1.getMarqueGauche())
print(d1.getMarqueDroite())
print(d1.estDouble())
print(d1.afficher())
print(d1.estEquivalent(d2))