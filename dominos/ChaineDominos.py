from Domino import *
from ExceptionChaineVide import *
from ExceptionDominoIncorrect import *

class ChaineDominos(Domino):
  def __init__(self, domino = None):
    if domino is None:
      self.__chaine = []
    else:
      self.__chaine = [domino]

  def getChaine(self):
    return self.__chaine

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
    if len(self.__chaine) == 0:
      raise ExceptionChaineVide()
    return self.__chaine[0]

  def dernierDomino(self):
    if len(self.__chaine) == 0:
      raise ExceptionChaineVide()
    return self.__chaine[-1]

  def getMarqueGauche(self):
    return self.premierDomino().getMarqueGauche()

  def getMarqueDroite(self):
    return self.dernierDomino().getMarqueDroite()

  def ajouterDomino(self, domino):
    return self.__chaine.append(domino)

  def __add__(self, domino):
    if len(self.__chaine) == 0:
      self.__chaine.append(domino)
    else:
      if self.getMarqueDroite() == domino.getMarqueGauche():
        self.__chaine.append(domino)
      elif self.getMarqueDroite() == domino.getMarqueDroite():
        self.__chaine.append(domino.inverser())
      else:
        raise ExceptionDominoIncorrect()
    return self