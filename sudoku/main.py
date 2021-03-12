from Sudoku import *
from tkinter import *
import math

########## FONCTIONS ##########

# Fonction pour charger la grille depuis un fichier texte
def chargerGrille(nomFichier, grilleARemplir):
  y = 1
  with open(nomFichier) as f:
    lignes = f.readlines()
  for ligne in lignes:
    x = 1
    for valeur in ligne.split(" "):
      grilleARemplir.setValeur(x, y, int(valeur))
      x += 1
    y += 1

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

def affichageValeurs():
  for x in range(1, tailleGrille + 1):
    for y in range(1, tailleGrille + 1):
      valeur = grilleDeJeu.getValeur(x, y)
      if valeur > 0:
        playGround.create_text(
          ((x * tailleCase) - (tailleCase / 2)) + 4 ,
          ((y * tailleCase) - (tailleCase / 2)) + 4,
          fill = 'black',
          text = valeur
        )

def getColonne(x):
  return (x // tailleCase) + 1

def getLigne(y):
  return (y // tailleCase) + 1

def getValeurCase(x, y):
  return grilleDeJeu.getValeur(getColonne(x), getLigne(y))

def inverserValeur(colonne, ligne):
  return getValeurCase(colonne, ligne) * -1

# Fonction pour vérifier si un nombre est déjà dans la case
def nombreEstDansLaCase(event):
  caseCliqueeX.set(event.x)
  caseCliqueeY.set(event.y)
  entry.delete(0, END)
  if getValeurCase(caseCliqueeX.get(), caseCliqueeY.get()) <= 0:
    entry.config(state = NORMAL)
    entry.focus()
    entry.bind('<Return>', verifierEntree)
  else:
    entry.config(state = DISABLED)
    mainWindow.focus_set()

# Fonction pour valider l'entrée de l'utilisateur
def verifierEntree(event):
  if valeurUtilisateur.get().isdigit():
    valeurAValider = int(valeurUtilisateur.get())
    if 1 <= valeurAValider <= 9:
      if valeurAValider == inverserValeur(caseCliqueeX.get(), caseCliqueeY.get()):
        grilleDeJeu.setValeur(getColonne(caseCliqueeX.get()), getLigne(caseCliqueeY.get()), valeurAValider)
        affichageValeurs()
  entry.delete(0, END)
  mainWindow.focus_set()

########## MAIN ##########

# Déclaration des variables
grilleInitiale = Sudoku(9)
grilleDeJeu = Sudoku(9)
tailleGrille = grilleDeJeu.getTaille()
tailleCase = 50
tailleCanvas = (tailleGrille * tailleCase) + 2
marges = 100
hauteurMainWindow = tailleCanvas + marges
largeurMainWindow = tailleCanvas + marges

# Fenêtre principale
mainWindow = Tk()
mainWindow.title('Projet sudoku en python')
mainWindow.minsize(width = largeurMainWindow, height = hauteurMainWindow)

# Déclaration des variables de contrôle
valeurUtilisateur = StringVar()
caseCliqueeX = IntVar()
caseCliqueeY = IntVar()

# Champ d'entrée de l'utilisateur
entry = Entry(mainWindow, textvariable = valeurUtilisateur)
entry.config(state = DISABLED)
entry.pack()

# Canvas du plateau de jeu
playGround = Canvas(mainWindow, bg = 'light blue', height = tailleCanvas, width = tailleCanvas)
playGround.place(relx = 0.5, rely = 0.5, anchor = CENTER)
playGround.bind('<Button-1>', nombreEstDansLaCase)

# Affichage de la grille
chargerGrille('/Users/sevndl/Desktop/code/python/sudoku/bordel.txt', grilleInitiale)
chargerGrille('/Users/sevndl/Desktop/code/python/sudoku/bordel.txt', grilleDeJeu)
affichageGrille()
affichageValeurs()

# Affichage de la fenêtre principale,
# et intrinsèquement des éléments graphiques la composant
mainWindow.mainloop()
