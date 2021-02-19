from ExceptionDomino import *

class ExceptionChaineVide(ExceptionDomino):
  def __init__(self):
    ExceptionDomino.__init__(self, "ERREUR : La chaîne est vide.")
