from ExceptionMarqueIncorrecte import *
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
try:
  d1 = Domino(21, 3)
  d2 = Domino(3, 5)
  chaine = ChaineDominos(d1)
  chaine.afficher()
  print("Valeur : " + chaine.valeur())
  print("Marque gauche" + chaine.getMarqueGauche())
  print("Marque droite" + chaine.getMarqueDroite())
except ExceptionMarqueIncorrecte as e:
  print(e.message)
