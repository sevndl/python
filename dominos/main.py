from Domino import *
from ChaineDominos import *


# print(d1.getMarqueGauche())
# print(d1.getMarqueDroite())
# print(d1.getValeur())
# print(d1.afficher())
# d1.inverser()
# print(d1.getMarqueGauche())
# print(d1.getMarqueDroite())
# print(d1.estDouble())
# print(d1.afficher())
# print(d1.estEquivalent(d2))
# print('d1 != d2' if d1.__ne__(d2) else 'd1 == d2')

d1 = Domino(5, 3)
d2 = Domino(3, 5)
chaine = ChaineDominos(d1)
chaine.afficher()
print(chaine.valeur())
print(chaine.getMarqueGauche())
print(chaine.getMarqueDroite())