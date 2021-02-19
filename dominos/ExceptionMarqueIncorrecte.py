from ExceptionDomino import *

class ExceptionMarqueIncorrecte(ExceptionDomino):
  def __init__(self, marque = ""):
    if marque != "":
      ExceptionDomino.__init__(self, "ERREUR : La marque " + str(marque) + " est incorrecte.")
    else:
      ExceptionDomino.__init__(self, "ERREUR : Les marques doivent être comprises entre 1 et 6.")