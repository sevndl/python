from Domino import *

class ChaineDominos(Domino):
  def __init__(self, domino = None):
    if domino is None:
      self.__chaine = []
    else:
      self.__chaine = [domino, Domino(1, 4)]

  def afficher(self):
    for domino in self.__chaine:
      if domino != self.dernierDomino():
        print(domino.afficher(), end = " - ")
      else:
        print(domino.afficher(), end = "\n")

  def valeur(self):
    somme = 0
    for domino in self.__chaine:
      somme += domino.valeur()
    return somme

  def premierDomino(self):
    return self.__chaine[0]

  def dernierDomino(self):
    return self.__chaine[-1]

  def getMarqueGauche(self):
    return self.premierDomino().getMarqueGauche()

  def getMarqueDroite(self):
    return self.premierDomino().getMarqueDroite()