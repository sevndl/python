from Sudoku import *
from tkinter import *
import math

# Définition des variables
grille = Sudoku(9)
tailleGrille = grille.getTaille()
tailleCase = 50
tailleCanvas = (tailleGrille * tailleCase) + 2
hauteurMainWindow = tailleCanvas + 100
largeurMainWindow = tailleCanvas + 100

grille.setValeur(1, 1, 8)
grille.setValeur(4, 7, 2)
grille.setValeur(5, 7, 6)

# Fonction d'affichage de la grille
# Ligne plus épaisse tous les (multiples de la
# racine carrée de la taille de la grille) cases
def affichageGrille():
  # Lignes verticales
  for x in range(0, tailleGrille + 1):
    playGround.create_line(
      (x * tailleCase) + 4,
      0,
      (x * tailleCase) + 4,
      (tailleGrille * tailleCase) + 4,
      width = 2 if (x % math.sqrt(tailleGrille) == 0) else 1
    )
  # Lignes horizontales
  for y in range(0, tailleGrille + 1):
    playGround.create_line(
      0,
      (y * tailleCase) + 4,
      (tailleGrille * tailleCase) + 4,
      (y * tailleCase) + 4,
      width = 2 if (y % math.sqrt(tailleGrille) == 0) else 1
    )

# Fonction d'affichage des valeurs dans la grille
def affichageValeurs():
  for x in range(1, tailleGrille + 1):
    for y in range(1, tailleGrille + 1):
      valeur = grille.getValeur(x, y)
      if valeur > 0:
        playGround.create_text(
          ((x * tailleCase) - (tailleCase / 2)) + 4 ,
          ((y * tailleCase) - (tailleCase / 2)) + 4,
          fill = "black",
          text = valeur
        )

# Fenêtre principale
mainWindow = Tk()
mainWindow.title("Projet sudoku en python")
mainWindow.minsize(width = largeurMainWindow, height = hauteurMainWindow)

# Canvas du plateau de jeu
playGround = Canvas(
  mainWindow,
  bg = 'light blue',
  height = tailleCanvas,
  width = tailleCanvas
)
playGround.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# Affichage de la grille
affichageGrille()
affichageValeurs()

# Affichage de la fenêtre principale,
# et intrinsèquement des éléments graphiques la composant
mainWindow.mainloop()
