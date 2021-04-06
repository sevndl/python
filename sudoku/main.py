from tkinter.font import Font
from Sudoku import *
from tkinter import *
from tkinter import filedialog

import math

########## FONCTIONS ##########

# Fonction pour charger la grille depuis un fichier texte
def chargerGrille(nomFichier, grilleARemplir):
  y = 1
  with open(nomFichier) as f:
    lignes = f.readlines()
  for ligne in lignes:
    x = 1
    for valeur in ligne.split(' '):
      grilleARemplir.setValeur(x, y, int(valeur))
      x += 1
    y += 1

# Fonction d'affichage de la grille
# Ligne plus épaisse toutes les (multiples de la
# racine carrée de la taille de la grille) cases
def affichageGrille():
  # Lignes verticales
  for x in range(0, tailleGrille + 1):
    playGround.create_line(
      (x * tailleCase) + 4,
      4,
      (x * tailleCase) + 4,
      (tailleGrille * tailleCase) + 4,
      width = 2 if (x % math.sqrt(tailleGrille) == 0) else 1
    )
  # Lignes horizontales
  for y in range(0, tailleGrille + 1):
    playGround.create_line(
      4,
      (y * tailleCase) + 4,
      (tailleGrille * tailleCase) + 4,
      (y * tailleCase) + 4,
      width = 2 if (y % math.sqrt(tailleGrille) == 0) else 1
    )

def getColonne(x):
  return (x // tailleCase) + 1

def getLigne(y):
  return (y // tailleCase) + 1

def affichageValeurs():
  for x in range(1, tailleGrille + 1):
    for y in range(1, tailleGrille + 1):
      valeurJeu = grilleDeJeu.getValeur(x, y)
      valeurVerifiee = grilleVerifiee.getValeur(x, y)
      valeurInitiale = grilleInitiale.getValeur(x, y)
      if valeurJeu > 0:
        precedentEtat = playGround.gettags('valeur' + str(x) + str(y))
        playGround.delete('valeur' + str(x) + str(y))
        if valeurJeu == valeurInitiale:
          couleur = 'black'
          etat = 'initial'
        elif valeurJeu == valeurVerifiee:
          couleur = 'green'
          etat = 'correct'
        else:
          if precedentEtat == () or precedentEtat[1] == 'nonVerifie':
            couleur = 'orange'
            etat = 'nonVerifie'
          elif precedentEtat == ('valeur' + str(x) + str(y), 'incorrect'):
            couleur = 'red'
            etat = 'incorrect'
        playGround.delete('caseFocused')
        playGround.create_text(
          ((x * tailleCase) - (tailleCase / 2)) + 4,
          ((y * tailleCase) - (tailleCase / 2)) + 4,
          fill = couleur,
          font = Font(size = 15, weight = 'normal'),
          text = valeurJeu,
          tag = ('valeur' + str(x) + str(y), etat)
        )
      else:
        precedentEtat = playGround.gettags('valeur' + str(x) + str(y))
        playGround.delete('valeur' + str(x) + str(y))

def inverserValeur(valeur):
  return valeur * -1

# Fonction pour vérifier si un nombre est déjà dans la case
def nombreEstDansLaCase(event):
  caseCliqueeX.set(event.x)
  caseCliqueeY.set(event.y)
  colonne = getColonne(caseCliqueeX.get())
  ligne = getColonne(caseCliqueeY.get())
  entreeUtilisateur.delete(0, END)
  if grilleVerifiee.getValeur(colonne, ligne) <= 0:
    playGround.delete('caseFocused')
    playGround.create_rectangle(
      ((colonne - 1) * tailleCase) + 4,
      ((ligne - 1) * tailleCase) + 4,
      ((colonne * tailleCase)) + 4,
      ((ligne * tailleCase)) + 4,
      width = 2,
      outline = '#8EC2F7',
      tag = 'caseFocused'
    )
    entreeUtilisateur.config(state = NORMAL)
    entreeUtilisateur.focus()
    entreeUtilisateur.bind('<Return>', verifierEntree)
  else:
    playGround.delete('caseFocused')
    entreeUtilisateur.config(state = DISABLED)
    mainWindow.focus_set()

# Fonction pour valider l'entrée de l'utilisateur à chaque case remplie
def verifierEntree(event):
  if valeurUtilisateur.get() == '':
    playGround.delete('valeur' + str(getColonne(caseCliqueeX.get())) + str(getLigne(caseCliqueeY.get())))
    playGround.delete('caseFocused')
  if valeurUtilisateur.get().isdigit():
    valeurAValider = int(valeurUtilisateur.get())
    if 1 <= valeurAValider <= 9:
      grilleDeJeu.setValeur(getColonne(caseCliqueeX.get()), getLigne(caseCliqueeY.get()), valeurAValider)
      playGround.itemconfig(
        'valeur' + str(getColonne(caseCliqueeX.get())) + str(getLigne(caseCliqueeY.get())),
        tag = ('valeur' + str(getColonne(caseCliqueeX.get())) + str(getLigne(caseCliqueeY.get())), 'nonVerifie')
      )
      affichageValeurs()
  entreeUtilisateur.delete(0, END)
  entreeUtilisateur.config(state = DISABLED)
  mainWindow.focus_set()

# Fonction pour vérifier si la valeur de chaque case remplie est correcte
def verifierGrille():
  for x in range(1, tailleGrille + 1):
    for y in range(1, tailleGrille + 1):
      precedentEtat = playGround.gettags('valeur' + str(x) + str(y))
      if precedentEtat != ('valeur' + str(x) + str(y), 'correct'):
        valeurJeu = grilleDeJeu.getValeur(x, y)
        valeurVerifiee = inverserValeur(grilleVerifiee.getValeur(x, y))
        if valeurJeu == valeurVerifiee:
          grilleVerifiee.setValeur(x, y, valeurJeu)
        else:
          playGround.itemconfig('valeur' + str(x) + str(y), tag = ('valeur' + str(x) + str(y), 'incorrect'))
  affichageValeurs()
  if verificationPartieTerminee():
    boutonVerification.config(state = DISABLED)
    entreeUtilisateur.config(state = DISABLED)
    messageGagne = Label(utilisateurFrame, text = 'Gagné !')
    messageGagne.pack()

# Fonction pour vérifier si la partie est terminée
def verificationPartieTerminee():
  casesRestantes = 0
  for x in range(1, tailleGrille + 1):
    for y in range(1, tailleGrille + 1):
      valeurCaseCourante = grilleVerifiee.getValeur(x, y)
      if valeurCaseCourante <= 0:
        casesRestantes += 1
  return True if casesRestantes == 0 else False

# Fonction pour sauvegarder la partie dans un fichier .txt
def sauvegarderPartie():
  sauvegardeFichier = filedialog.asksaveasfilename(
    title = 'Enregistrer sous...',
    defaultextension = 'txt',
    filetypes = [('Text File', 'txt')])
  grille = ''
  for x in range(1, tailleGrille + 1):
    for y in range(1, tailleGrille + 1):
      valeurJeu = grilleDeJeu.getValeur(y, x)
      if valeurJeu < 1:
        valeurJeu = 0
      valeurJeu = str(valeurJeu)
      grille += valeurJeu + ' ' if y < tailleGrille else valeurJeu + '\n'
  with open(sauvegardeFichier, 'w') as f:
    f.write(grille)

# Fonction pour charger une partie depuis un fichier .txt
def chargerPartie():
  fichierACharger = filedialog.askopenfilename(
    title = 'Charger une grille...',
    defaultextension = 'txt',
    filetypes = [('Text File', 'txt')])
  chargerGrille(fichierACharger, grilleDeJeu)
  affichageValeurs()
  verifierGrille()

########## CODE PRINCIPAL ##########

# Déclaration des variables
grilleInitiale = Sudoku(9)
grilleVerifiee = Sudoku(9)
grilleDeJeu = Sudoku(9)
tailleGrille = grilleDeJeu.getTaille()
tailleCase = 75
tailleCanvas = (tailleGrille * tailleCase) + 4
marges = 300
hauteurMainWindow = tailleCanvas
largeurMainWindow = tailleCanvas + marges

# Fenêtre principale
mainWindow = Tk()
mainWindow.title('Projet sudoku en python')
mainWindow.minsize(width = largeurMainWindow, height = hauteurMainWindow)

# Position initiale de la fenêtre au centre de l'écran
largeurEcran = mainWindow.winfo_screenwidth()
hauteurEcran = mainWindow.winfo_screenheight()
mainWindow.geometry('+{}+{}'.format(int(largeurEcran / 2 - largeurMainWindow / 2), int(hauteurEcran / 2 - hauteurMainWindow / 2)))

# Frame du header
headerFrame = Frame(
  mainWindow,
  padx = 10,
  pady = 10
)
headerFrame.pack(side = TOP)

# Frame du plateau
plateauFrame = Frame(
  mainWindow,
  padx = 10,
  pady = 10
)
plateauFrame.pack(side = LEFT)

# Frame des contrôles utilisateur
utilisateurFrame = Frame(
  mainWindow,
  padx = 10,
  pady = 10
)
utilisateurFrame.pack(side = LEFT)

# Déclaration des variables de contrôle
valeurUtilisateur = StringVar()
caseCliqueeX = IntVar()
caseCliqueeY = IntVar()

# Remplissage du header
titre = Label(headerFrame, text = 'SUDOKU')
titre.pack(side = TOP)

# Canvas du plateau de jeu
playGround = Canvas(
  plateauFrame,
  height = tailleCanvas,
  width = tailleCanvas
)
playGround.pack(side = LEFT)
playGround.bind('<Button-1>', nombreEstDansLaCase)

# Champ d'entrée de l'utilisateur
entreeUtilisateur = Entry(utilisateurFrame, textvariable = valeurUtilisateur)
entreeUtilisateur.config(state = DISABLED)
entreeUtilisateur.pack()

# Bouton de vérification de la grille
boutonVerification = Button(utilisateurFrame, text = 'Vérifier la grille', command = verifierGrille)
boutonVerification.pack()

# Bouton de sauvegarde de la partie dans un fichier .txt
btnSauvegarderPartie = Button(utilisateurFrame, text = 'Sauvegarder la partie dans un fichier .txt', command = sauvegarderPartie)
btnSauvegarderPartie.pack()

# Bouton de chargement de la partie depuis un fichier .txt
btnChargerPartie = Button(utilisateurFrame, text = 'Charger une partie depuis un fichier .txt', command = chargerPartie)
btnChargerPartie.pack()

# Affichage de la grille
chargerGrille('bordel.txt', grilleInitiale)
chargerGrille('bordel.txt', grilleVerifiee)
chargerGrille('bordel.txt', grilleDeJeu)
affichageGrille()
affichageValeurs()

# Affichage de la fenêtre principale,
# et intrinsèquement des éléments graphiques la composant
mainWindow.mainloop()
