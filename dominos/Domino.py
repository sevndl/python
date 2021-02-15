class Domino:
  def __init__(self, marque_gauche0 = 0, marque_droite0 = 0):
      if 0 <= marque_gauche0 <= 6:
        self.marque_gauche = marque_gauche0
      if 0 <= marque_droite0 <= 6:
        self.marque_droite = marque_droite0

  def getMarqueGauche(self):
    return self.marque_gauche

  def getMarqueDroite(self):
    return self.marque_droite

  def getValeur(self):
    return self.marque_droite + self.marque_gauche

  def inverser(self):
    tmp_marque_droite = self.marque_droite
    self.marque_droite = self.marque_gauche
    self.marque_gauche = tmp_marque_droite

  # def estEquivalent(self, Domino):
  #   return 

  def estDouble(self):
    return True if self.marque_droite == self.marque_gauche else False

  def afficher(self):
    return '[ ' + str(self.marque_gauche) + ' | ' + str(self.marque_droite) + ' ]'