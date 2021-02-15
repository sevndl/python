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

  def estEquivalent(self, dominoATester):
    return True if self.getMarqueDroite() == dominoATester.getMarqueDroite() and self.getMarqueGauche() == dominoATester.getMarqueGauche() or self.getMarqueDroite() == dominoATester.getMarqueGauche() and self.getMarqueGauche() == dominoATester.getMarqueDroite() else False

  def estDouble(self):
    return True if self.marque_droite == self.marque_gauche else False

  def afficher(self):
    if self.marque_droite == 0:
      return '[ ' + str(self.marque_gauche) + ' |  ]'
    if self.marque_gauche == 0:
      return '[  | ' + str(self.marque_droite) + ' ]'
    return '[ ' + str(self.marque_gauche) + ' | ' + str(self.marque_droite) + ' ]'