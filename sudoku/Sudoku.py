class Sudoku:
  def __init__(self, taille = 9, valeur = 0):
    self.taille = taille
    self.grille = self.initialiserGrille(taille, 0)
    # self.grille = []

  def initialiserGrille(self, taille = 9, valeur = 0):
    return [[valeur for iCol in range(0, taille)] for iLig in range(0, taille)]

  def afficher(self):
    for x in range(1, self.getTaille() + 1):
      for y in range(1, self.getTaille() + 1):
        valeur = self.getValeur(x, y)
        if valeur > 0:
          print(valeur, end = ' ')
        else:
          print('_', end = ' ')
      print()

  def getTaille(self):
    return self.taille

  def getGrille(self):
    return self.grille

  def getValeur(self, ligne, colonne):
    # valeurs entre 1 et 9
    return self.getGrille()[ligne - 1][colonne - 1]

  def setValeur(self, ligne, colonne, valeur):
    # valeurs entre 1 et 9
    if 1 <= valeur <= 9:
      self.getGrille()[ligne - 1][colonne - 1] = valeur