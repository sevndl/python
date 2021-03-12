class Sudoku:
  def __init__(self, taille = 9, valeur = 0):
    self.taille = taille
    self.grille = self.initialiserGrille(taille, 0)

  def initialiserGrille(self, taille = 9, valeur = 0):
    return [[valeur for iCol in range(0, taille)] for iLig in range(0, taille)]

  def getTaille(self):
    return self.taille

  def getGrille(self):
    return self.grille

  def getValeur(self, colonne, ligne):
    return self.getGrille()[colonne - 1][ligne - 1]

  def setValeur(self, colonne, ligne, valeur):
    if valeur <= self.getTaille():
      self.getGrille()[colonne - 1][ligne - 1] = valeur