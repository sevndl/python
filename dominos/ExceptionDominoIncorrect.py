from ExceptionDomino import *

class ExceptionDominoIncorrect(ExceptionDomino):
  def __init__(self):
    ExceptionDomino.__init__(self, "ERREUR : Impossible d'ajouter ce domino.")