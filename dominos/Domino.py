class Domino:
  def __init__(self, marque_gauche = 0, marque_droite = 0):
    if 0 <= marque_gauche <= 6:
      self.__marque_gauche = marque_gauche
    if 0 <= marque_droite <= 6:
      self.__marque_droite = marque_droite

  def afficher(self):
    if self.estDouble():
      return '[  |  ]'
    if self.__marque_droite == 0:
      return '[ ' + str(self.__marque_gauche) + ' |  ]'
    if self.__marque_gauche == 0:
      return '[  | ' + str(self.__marque_droite) + ' ]'
    return '[ ' + str(self.__marque_gauche) + ' | ' + str(self.__marque_droite) + ' ]'

  def getMarqueGauche(self):
    return self.__marque_gauche

  def getMarqueDroite(self):
    return self.__marque_droite

  def getValeur(self):
    return self.__marque_droite + self.__marque_gauche

  def inverser(self):
    tmp_marque_droite = self.__marque_droite
    self.__marque_droite = self.__marque_gauche
    self.__marque_gauche = tmp_marque_droite

  def estEquivalent(self, dominoATester):
    return True if self.getMarqueDroite() == dominoATester.getMarqueDroite() and self.getMarqueGauche() == dominoATester.getMarqueGauche() or self.getMarqueDroite() == dominoATester.getMarqueGauche() and self.getMarqueGauche() == dominoATester.getMarqueDroite() else False

  def estDouble(self):
    return True if self.__marque_droite == self.__marque_gauche else False

  def __lt__(self, dominoATester):
    return self.getValeur() < dominoATester.getValeur()
    
  def __le__(self, dominoATester):
    return self.getValeur() <= dominoATester.getValeur()

  def __eq__(self, dominoATester):
    return self.getValeur() == dominoATester.getValeur()

  def __gt__(self, dominoATester):
    return not(self <= dominoATester)

  def __ge__(self, dominoATester):
    return not(self < dominoATester)

  def __ne__(self, dominoATester):
    return not(self == dominoATester)