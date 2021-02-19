from ChaineDominos import *
from Domino import *
from ExceptionChaineVide import *
from ExceptionMarqueIncorrecte import *
from ExceptionDominoIncorrect import *

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
  d1 = Domino(3, 1)
  d2 = Domino(1, 5)
  d3 = Domino(5, 0)
  d4 = Domino(4, 3)
  chaine = ChaineDominos(d1)
  chaine.afficher()
  chaine = chaine + d2
  chaine.afficher()
  chaine = chaine + d3
  chaine.afficher()
  chaine = chaine + d4
  chaine.afficher()
  print("Valeur :", chaine.valeur())
  print("Marque gauche :", chaine.getMarqueGauche())
  print("Marque droite :", chaine.getMarqueDroite())
  if chaine.estDouble():
    print("chaine double")
  else:
    print("pas double")
except ExceptionMarqueIncorrecte as e:
  print(e.message)
except ExceptionChaineVide as e:
  print(e.message)
except ExceptionDominoIncorrect as e:
  print(e.message)