import tkinter
from Sudoku import *
from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
from functools import partial
from random import randint

import math
import glob

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
        precedentEtat = playGround.gettags('valeur&' + str(x) + '&' + str(y))
        playGround.delete('valeur&' + str(x) + '&' + str(y))
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
          elif precedentEtat == ('valeur&' + str(x) + '&' + str(y), 'incorrect'):
            couleur = 'red'
            etat = 'incorrect'
        for i in range(1, tailleGrille + 1):
          playGround.delete('indice&' + str(x) + '&' + str(y) + '&' + str(i))
        playGround.create_text(
          ((x * tailleCase) - (tailleCase / 2)) + 4,
          ((y * tailleCase) - (tailleCase / 2)) + 4,
          fill = couleur,
          font = Font(size = int(taillePoliceValeurs), weight = 'normal'),
          text = valeurJeu,
          tag = ('valeur&' + str(x) + '&' + str(y), etat)
        )
      else:
        playGround.delete('valeur&' + str(x) + '&' + str(y))

# Fonction pour afficher les indices
def affichageIndice(colonne, ligne, valeur, tag):
  portionCase = tailleCase // math.sqrt(tailleGrille)
  if valeur % math.sqrt(tailleGrille) == 0:
    niveauColonne = math.sqrt(tailleGrille)
    niveauLigne = valeur // math.sqrt(tailleGrille)
  else:
    niveauColonne = valeur % math.sqrt(tailleGrille)
    niveauLigne = valeur // math.sqrt(tailleGrille) + 1
  colonne = ((colonne - 1) * tailleCase) + ((niveauColonne * portionCase) - (portionCase / 2))
  ligne = ((ligne - 1) * tailleCase) + ((niveauLigne * portionCase) - (portionCase / 2))
  playGround.create_text(
    colonne + 2,
    ligne + 2,
    text = valeur,
    tag = tag,
    fill = 'grey',
    font = Font(size = int(taillePoliceIndices), weight = 'normal'),
  )

def inverserValeur(valeur):
  return valeur * -1

# Fonction pour vérifier si un nombre est déjà dans la case
def nombreEstDansLaCase(event):
  caseCliqueeX.set(event.x)
  caseCliqueeY.set(event.y)
  colonne = getColonne(caseCliqueeX.get())
  ligne = getColonne(caseCliqueeY.get())

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
    caseVide.set(True)
  else:
    playGround.delete('caseFocused')
    mainWindow.focus_set()
    caseVide.set(False)

# Fonction qui redirige vers la bonne fonction selon le mode sélectionné au moment
# de l'appui sur la touche Entrer
def modeChecker(valeur):
  if not partieTerminee.get():
    if caseVide.get():
      valeurUtilisateur.set(valeur)
      verifierIndice() if modeIndice.get() else verifierEntree()

# Fonction pour vérifier l'indice entré
def verifierIndice():
  colonne = getColonne(caseCliqueeX.get())
  ligne = getLigne(caseCliqueeY.get())
  valeurAValider = int(valeurUtilisateur.get())
  playGround.delete('valeur&' + str(colonne) + '&' + str(ligne))
  grilleDeJeu.removeValeur(colonne, ligne)
  tagPrefix = 'indice&'
  tagIndice = (tagPrefix + str(colonne) + '&' + str(ligne) + '&' + str(valeurAValider))
  tags = playGround.gettags(tagPrefix + str(colonne) + '&' + str(ligne) + '&' + str(valeurAValider))
  indiceSupprime = False
  if len(tags) > 0:
    for tag in tags:
      valeur = tag.split('&')[3]
      if valeur == str(valeurAValider):
        playGround.delete(tag)
        indiceSupprime = True
        break
  if not indiceSupprime:
    affichageIndice(colonne, ligne, valeurAValider, tagIndice)
  mainWindow.focus_set()

# Fonction pour valider l'entrée de l'utilisateur à chaque case remplie
def verifierEntree():
  colonne = getColonne(caseCliqueeX.get())
  ligne = getLigne(caseCliqueeY.get())
  if valeurUtilisateur.get() == '':
    playGround.delete('valeur&' + str(colonne) + '&' + str(ligne))
    grilleDeJeu.removeValeur(colonne, ligne)
  valeurAValider = int(valeurUtilisateur.get())
  if 1 <= valeurAValider <= tailleGrille:
    grilleDeJeu.setValeur(colonne, ligne, valeurAValider)
    tagPrefix = 'valeur&'
    tagValeur = (tagPrefix + str(colonne) + '&' + str(ligne), 'nonVerifie')
    # Attribution du tag
    playGround.itemconfig(
      tagPrefix + str(colonne) + '&' + str(ligne),
      tag = tagValeur
    )
    affichageValeurs()

# Fonction pour vérifier si la valeur de chaque case remplie est correcte
def verifierGrille():
  if not verificationPartieTerminee():
    caseVide.set(False)
    playGround.delete('caseFocused')
    mainWindow.focus_set()
    for x in range(1, tailleGrille + 1):
      for y in range(1, tailleGrille + 1):
        precedentEtat = playGround.gettags('valeur&' + str(x) + '&' + str(y))
        if precedentEtat != ('valeur&' + str(x) + '&' + str(y), 'correct'):
          valeurJeu = grilleDeJeu.getValeur(x, y)
          valeurVerifiee = inverserValeur(grilleVerifiee.getValeur(x, y))
          if valeurJeu == valeurVerifiee:
            grilleVerifiee.setValeur(x, y, valeurJeu)
          else:
            playGround.itemconfig('valeur&' + str(x) + '&' + str(y), tag = ('valeur&' + str(x) + '&' + str(y), 'incorrect'))
    affichageValeurs()
    verificationPartieTerminee()
    if partieTerminee.get():
      boutonModeIndice.config(state = DISABLED)
      playGround.unbind('<Button-1>')
      playGround.delete('caseFocused')
      global messageGagne
      messageGagne = Label(indiceFrame, text = 'Gagné !')
      messageGagne.pack(side = RIGHT)

# Fonction pour vérifier si la partie est terminée
def verificationPartieTerminee():
  casesRestantes = 0
  for x in range(1, tailleGrille + 1):
    for y in range(1, tailleGrille + 1):
      valeurCaseCourante = grilleVerifiee.getValeur(x, y)
      if valeurCaseCourante <= 0:
        casesRestantes += 1
  partieTerminee.set(True if casesRestantes == 0 else False)

# Fonction pour sauvegarder la partie dans un fichier .txt
def sauvegarderPartie():
  sauvegardeFichier = filedialog.asksaveasfilename(
    title = 'Enregistrer sous...',
    defaultextension = 'txt',
    filetypes = [('Text File', 'txt')])
  if sauvegardeFichier != '':
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
  if fichierACharger != '':
    chargerGrille(fichierACharger, grilleDeJeu)
    affichageValeurs()
    verifierGrille()

# Fonction pour changer de mode
def switchMode():
  modeIndice.set(not modeIndice.get())

# Fonction qui charge une grille aléatoire
def chargementGrilleAleatoire():
  global numeroGrille
  listeGrillesRepertoire = []
  if partieTerminee.get():
    messageGagne.destroy()
  for fichierGrille in glob.glob('./*.txt'):
    listeGrillesRepertoire.append(fichierGrille)
  numeroGrille = randint(0, len(listeGrillesRepertoire) - 1)
  chargerGrille(listeGrillesRepertoire[numeroGrille], grilleInitiale)
  chargerGrille(listeGrillesRepertoire[numeroGrille], grilleVerifiee)
  chargerGrille(listeGrillesRepertoire[numeroGrille], grilleDeJeu)
  affichageGrille()
  affichageValeurs()
  playGround.bind('<Button-1>', nombreEstDansLaCase)
  boutonModeIndice.config(state = NORMAL)
  partieTerminee.set(False)

# Fonction qui cherche les valeurs possibles dans une case
def valeursPossiblesDansCase(colonne, ligne):
  valeursLigne = []
  valeursColonne = grilleDeJeu.getGrille()[colonne - 1]
  valeursCarre = []
  valeursPossibles = []

  for x in range(1, tailleGrille + 1):
    valeursLigne.append(grilleDeJeu.getValeur(x, ligne))

  # for val in valeursColonne:
  #   if val <= 0:
  #     valeursColonne.pop(val)
  # for val in valeursLigne:
  #   if val <= 0:
  #     valeursLigne.pop(val)

  # print(valeursColonne)
  # print(valeursLigne)

########## CODE PRINCIPAL ##########

# Déclaration des variables
grilleInitiale = Sudoku(9)
grilleVerifiee = Sudoku(9)
grilleDeJeu = Sudoku(9)
tailleGrille = grilleDeJeu.getTaille()
tailleCase = 100 - (tailleGrille * 3)
tailleCanvas = (tailleGrille * tailleCase) + 4
taillePoliceValeurs = tailleCase / 4
taillePoliceIndices = taillePoliceValeurs / 2
margesX = 40
margesY = 150
hauteurMainWindow = tailleCanvas + margesY
largeurMainWindow = tailleCanvas + margesX

# Fenêtre principale
mainWindow = Tk()
mainWindow.title('Projet sudoku en python')
mainWindow.minsize(width = largeurMainWindow, height = hauteurMainWindow)
mainWindow.maxsize(width = largeurMainWindow, height = hauteurMainWindow)

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
plateauFrame.pack(side = TOP)

# Frame des contrôles utilisateur
inputFrame = Frame(
  mainWindow,
  padx = 10,
  pady = 10
)
inputFrame.pack(side = LEFT)

# Frame du mode indice
indiceFrame = Frame(
  mainWindow,
  padx = 10,
  pady = 10
)
indiceFrame.pack(side = LEFT)

# Déclaration des variables de contrôle
valeurUtilisateur = StringVar()
caseCliqueeX = IntVar()
caseCliqueeY = IntVar()
modeIndice = BooleanVar(False)
caseVide = BooleanVar(False)
partieTerminee = BooleanVar(False)

# Mise en place de la barre de menus
barreDeMenus = tkinter.Menu(mainWindow)

menuFichier = tkinter.Menu(barreDeMenus)
menuFichier.add_command(label = 'Nouvelle partie', command = chargementGrilleAleatoire)
menuFichier.add_command(label = 'Sauvegarder la partie...', command = sauvegarderPartie)
menuFichier.add_command(label = 'Charger une partie...', command = chargerPartie)
menuFichier.add_separator()
menuFichier.add_command(label = 'Quitter', command = mainWindow.quit)

optionsMenu = tkinter.Menu(mainWindow)
optionsMenu.add_command(label = 'Vérifier la grille', command = verifierGrille)

barreDeMenus.add_cascade(label = 'Fichier', menu = menuFichier)
barreDeMenus.add_cascade(label = 'Options', menu = optionsMenu)
mainWindow.config(menu = barreDeMenus)

# Remplissage du header
titre = Label(headerFrame, text = 'SUDOKU')
titre.pack(side = TOP)

# Canvas du plateau de jeu
playGround = Canvas(
  plateauFrame,
  height = tailleCanvas,
  width = tailleCanvas
)
playGround.pack(side = TOP)

# Champ d'entrée des valeurs
label = Label(inputFrame, text = 'Valeur :')
label.pack(side = LEFT)
for i in range(1, tailleGrille + 1):
  Button(inputFrame, command = partial(modeChecker, i), text = i, padx = 5, pady = 5).pack(side = LEFT) 

# Bouton de changement de mode (indice ou pas)
boutonModeIndice = Checkbutton(indiceFrame, text = 'Mode indice', command = switchMode)
boutonModeIndice.pack()

# Affichage de la grille
chargementGrilleAleatoire()

# Affichage de la fenêtre principale,
# et intrinsèquement des éléments graphiques la composant
mainWindow.mainloop()
