from os import times
from time import time
import tkinter
from Sudoku import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.font import Font
from functools import partial

import math
import glob
import random

########## FONCTIONS ##########
"""
Fonction pour charger la grille depuis un fichier texte
"""
def chargerGrille(nomFichier, grilleARemplir):
  # Réinitialisation des variables pour le timer
  minutes.set(0)
  secondes.set(0)
  y = 1
  with open(nomFichier) as f:
    lignes = f.readlines()
  for ligne in lignes:
    x = 1
    for valeur in ligne.split(' '):
      # Remplissage de la grille avec les valeurs du fichier
      grilleARemplir.setValeur(x, y, int(valeur))
      x += 1
    y += 1

"""
Fonction d'affichage de la grille
Ligne plus épaisse toutes les (multiples de la
racine carrée de la taille de la grille) cases
"""
def affichageGrille():
  for x in range(0, tailleGrille + 1):
    # Lignes verticales
    playGround.create_line(
      (x * tailleCase) + 4,
      4,
      (x * tailleCase) + 4,
      (tailleGrille * tailleCase) + 4,
      width = 2 if (x % math.sqrt(tailleGrille) == 0) else 1
    )
    # Lignes horizontales
    playGround.create_line(
      4,
      (x * tailleCase) + 4,
      (tailleGrille * tailleCase) + 4,
      (x * tailleCase) + 4,
      width = 2 if (x % math.sqrt(tailleGrille) == 0) else 1
    )

"""
Fonctions retournant la colonne et la ligne de la case en fonction des coordonnées du clic (passé en paramètre)
"""
def getColonne(x):
  return (x // tailleCase) + 1

def getLigne(y):
  return (y // tailleCase) + 1

"""
Fonction d'affichage des valeurs
Pour chaque couple de coordonnées de case :
  - on récupère les valeurs de chacune des trois grilles utilisées
  - si la valeur est strictement inférieure à 1 :
    - on efface par précaution le label existant dans cette case
  - sinon:
    - on récupère les tags du texte existant dans cette case (s'il y en a) puis on l'efface
    - on définit les variables de couleur et d'état selon la valeur (correcte, initiale, non vérifiée ou incorrecte)
    - on supprime tous les indices présents dans cette case s'il y en a
    - on écrit un nouveau texte dans cette case avec les données définies juste avant
"""
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
          playGround.delete('valeurpossible&' + str(x) + '&' + str(y) + '&' + str(i))
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

"""
Fonction pour afficher les indices
- On supprime la valeur potentiellement existante dans cette case (visuellement et dans la grille de jeu)
- On raffiche les valeurs sans celle-ci
- On calcule la position de l'indice dans la case en fonction de sa valeur et de la taille de la grille
- On affiche le texte en petit, avec la couleur selon le mode indice ou valeurs possibles
"""
def affichageIndice(colonne, ligne, valeur, tag, mode = 'indice'):
  playGround.delete('valeur&' + str(colonne), '&' + str(ligne))
  grilleDeJeu.removeValeur(colonne, ligne)
  affichageValeurs()
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
    fill = 'grey' if mode == 'indice' else 'orange',
    font = Font(size = int(taillePoliceIndices), weight = 'normal'),
  )

"""
Fonction pour inverser la valeur passée en paramètre (utilisée pour vérifier la valeur de la grille de jeu
par rapport à la valeur de la grille vérifiée)
"""
def inverserValeur(valeur):
  return valeur * -1

"""
Fonction pour vérifier si un nombre est déjà dans la case
Si c'est le cas, on efface le petit carré bleu et on enlève le focus
Sinon, on crée un petit carré bleu de la taille de la case pour montrer la case sélectionnée
"""
def nombreEstDansLaCase(event):
  caseCliqueeX.set(event.x)
  caseCliqueeY.set(event.y)
  global colonne
  colonne = getColonne(caseCliqueeX.get())
  global ligne
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

"""
Fonction qui redirige vers la bonne fonction selon le mode sélectionné au moment de l'appui sur un bouton de valeur
"""
def modeChecker(valeur):
  if not partieTerminee.get() and not timeStop.get():
    if caseVide.get():
      valeurUtilisateur.set(valeur)
      verifierIndice() if modeIndice.get() else verifierEntree()

"""
Fonction pour vérifier l'indice entré
- On récupère la valeur de l'utilisateur
- On supprime la valeur présente dans la case s'il y en a une
- Si la valeur de l'indice est déjà présente dans la case
  - on l'efface
- Sinon, on affiche le nouvel indice
"""
def verifierIndice():
  valeurAValider = int(valeurUtilisateur.get())
  playGround.delete('valeur&' + str(colonne) + '&' + str(ligne))
  playGround.delete('valeurpossible&' + str(colonne) + '&' + str(ligne))
  grilleDeJeu.removeValeur(colonne, ligne)
  tagPrefix = 'indice&'
  tagIndice = tagPrefix + str(colonne) + '&' + str(ligne) + '&' + str(valeurAValider)
  tags = playGround.gettags(tagIndice)
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

"""
Fonction pour valider l'entrée de l'utilisateur à chaque case remplie
- On récupère la valeur de l'utilisateur
- Si la valeur est déjà présente dans la case
  - on l'efface et on raffiche les valeurs
- Sinon
  - on supprime une potentielle valeur déjà présente et on affiche la valeur de l'utilisateur
"""
def verifierEntree(c = 0, l = 0, valeurAValider = 0):
  if valeurAValider == 0:
    valeurAValider = int(valeurUtilisateur.get())
  if c == 0:
    c = colonne
  if l == 0:
    l = ligne
  if 1 <= valeurAValider <= tailleGrille:
    if valeurAValider == grilleDeJeu.getValeur(c, l):
      playGround.delete('valeur&' + str(c) + '&' + str(l))
      grilleDeJeu.removeValeur(c, l)
    else:
      grilleDeJeu.setValeur(c, l, valeurAValider)
      tagPrefix = 'valeur&'
      tagValeur = (tagPrefix + str(c) + '&' + str(l), 'nonVerifie')
      # Attribution du tag
      playGround.itemconfig(
        tagPrefix + str(c) + '&' + str(l),
        tag = tagValeur
      )
    affichageValeurs()

"""
Fonction pour vérifier si la valeur de chaque case remplie est correcte
"""
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
    # On lance la vérification de la partie terminée après 500ms pour laisser le temps à l'affichage
    playGround.after(500, verificationPartieTerminee)

"""
Fonction pour vérifier si la partie est terminée
- Pour chaque case, si sa valeur est négative dans la grille vérifiée, cela signifie qu'elle n'a pas été découverte et donc on met la variable booléenne à False
- Sinon, on affiche une pop-up de victoire et on offre le choix d'une nouvelle partie ou de quitter l'application
"""
def verificationPartieTerminee():
  casesRestantes = 0
  for x in range(1, tailleGrille + 1):
    for y in range(1, tailleGrille + 1):
      valeurCaseCourante = grilleVerifiee.getValeur(x, y)
      if valeurCaseCourante <= 0:
        casesRestantes += 1
  partieTerminee.set(True if casesRestantes == 0 else False)
  if partieTerminee.get():
    timeStop.set(True)
    boutonModeIndice.config(state = DISABLED)
    playGround.unbind('<Button-1>')
    playGround.delete('caseFocused')
    nouvellePartie = messagebox.askyesno(title = 'Victoire en ' + str(minutes.get()) + 'minute(s) et ' + str(secondes.get()) + 'seconde(s).', message = 'Nouvelle partie ? \n(Yes : démarrer une nouvelle partie | No : quitter)')
    if nouvellePartie:
      chargementGrilleAleatoire()
    else:
      mainWindow.quit()

"""
Fonction pour sauvegarder la partie dans un fichier .txt
- On récupère les valeurs de chaque ligne et chaque colonne dans une chaîne de caractères
- On écrit cette chaîne de caractères dans un fichier
"""
def sauvegarderPartie():
  sauvegardeFichier = filedialog.asksaveasfilename(
    title = 'Enregistrer sous...',
    initialfile = 'partie.' + grilleAleatoire,
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

"""
Fonction pour charger une partie depuis un fichier .txt
- Si le nom de fichier ne correspond pas à la partie en cours, on affiche un message d'erreur
- Sinon on réinitialise la grille de jeu avec chaque valeur du fichier
"""
def chargerPartie():
  fichierACharger = filedialog.askopenfilename(
    title = 'Charger une grille...',
    defaultextension = 'txt',
    filetypes = [('Text File', 'txt')])
  if fichierACharger != '' and fichierACharger.split('/')[-1] == 'partie.' + grilleAleatoire:
    chargerGrille(fichierACharger, grilleDeJeu)
    affichageValeurs()
    verifierGrille()
  else:
    messagebox.showerror(title = 'Erreur', message = 'La partie sélectionnée n\'est pas reconnue ou ne correspond pas à la partie en cours.')

"""
Fonction pour changer de mode
"""
def switchMode():
  modeIndice.set(not modeIndice.get())

"""
Fonction qui charge une grille aléatoire
- On sélectionne un fichier .txt aléatoire parmi ceux du répertoire courant
- On charge ses valeurs dans les grilles de sudoku
- On crée un écouteur d'évènement pour le clic de la souris
"""
def chargementGrilleAleatoire():
  timeStop.set(False)
  global grilleAleatoire
  listeGrillesRepertoire = []
  playGround.delete('caseFocused')
  for fichierGrille in glob.glob('*.txt'):
    listeGrillesRepertoire.append(fichierGrille)
  grilleAleatoire = random.choice(listeGrillesRepertoire)
  chargerGrille(grilleAleatoire, grilleInitiale)
  chargerGrille(grilleAleatoire, grilleVerifiee)
  chargerGrille(grilleAleatoire, grilleDeJeu)
  affichageGrille()
  affichageValeurs()
  playGround.bind('<Button-1>', nombreEstDansLaCase)
  boutonModeIndice.config(state = NORMAL)
  partieTerminee.set(False)

"""
Fonction qui récupère les valeurs possibles dans une case
- Je n'ai pas eu le temps de mettre en place les valeurs du carré de la case
"""
def valeursPossiblesDansCase(colonne, ligne):
  valeursLigne = []
  valeursColonne = []
  valeursCarre = []
  valeursPossibles = []

  # Récupération des valeurs uniquement positives de la colonne sélectionnée
  for val in grilleVerifiee.getGrille()[colonne - 1]:
    valeursColonne.append(val)
  for val in valeursColonne:
    if val <= 0:
      valeursColonne.remove(val)

  # Récupération des valeurs uniquement positives de la ligne sélectionnée
  for x in range(1, tailleGrille + 1):
    valeursLigne.append(grilleVerifiee.getValeur(x, ligne))
  for val in valeursLigne:
    if val <= 0:
      valeursLigne.remove(val)

  # Ajout des valeurs possibles => valeurs non présentes dans chacune des deux listes précédentes
  for val in range(1, tailleGrille + 1):
    if not val in valeursLigne and not val in valeursColonne:
      valeursPossibles.append(val)

  return valeursPossibles

"""
Fonction qui affiche les valeurs possibles dans une case
"""
def affichageValeursPossiblesDansCase():
  if 'colonne' in globals() and 'ligne' in globals():
    valeursPossibles = valeursPossiblesDansCase(colonne, ligne)
    if len(valeursPossibles) > 1:
      for value in valeursPossibles:
        affichageIndice(colonne, ligne, value, 'valeurpossible&' + str(colonne) + '&' + str(ligne) + '&' + str(value), 'valeurspossibles')
    else:
      grilleDeJeu.setValeur(colonne, ligne, valeursPossibles[0])
      affichageValeurs()
      verifierGrille()

"""
Fonction de remplissage automatique des cases avec une seule possibilité
"""
def remplissageAutomatique():
  for c in range(1, tailleGrille + 1):
    for l in range(1, tailleGrille + 1):
      if len(valeursPossiblesDansCase(c, l)) == 1:
        verifierEntree(c, l, valeursPossiblesDansCase(c, l)[0])
  verifierGrille()

"""
Fonction pour mettre en pause et masquer le canvas
"""
def switchPause():
  timeStop.set(not timeStop.get())
  if timeStop.get():
    playGround.pack_forget()
  else:
    playGround.pack(side = TOP)
    updateTimer()

"""
Fonction pour mettre à jour le temps
"""
def updateTimer():
  secondes.set(secondes.get() + 1)
  if secondes.get() >= 60:
    minutes.set(minutes.get() + 1)
    secondes.set(0)
  timer.config(text = '{:d}:{:d}'.format(minutes.get(), secondes.get()))
  if not timeStop.get():
    mainWindow.after(1000, updateTimer)

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
secondes = IntVar()
minutes = IntVar()
modeIndice = BooleanVar(False)
caseVide = BooleanVar(False)
partieTerminee = BooleanVar(False)
timeStop = BooleanVar(False)

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
optionsMenu.add_command(label = 'Afficher les valeurs possibles dans la case sélectionnée', command = lambda: affichageValeursPossiblesDansCase())
optionsMenu.add_command(label = 'Remplir les cases avec une seule possibilité', command = lambda: remplissageAutomatique())

barreDeMenus.add_cascade(label = 'Fichier', menu = menuFichier)
barreDeMenus.add_cascade(label = 'Options', menu = optionsMenu)
mainWindow.config(menu = barreDeMenus)

# Remplissage du header avec le timer
timer = Label(headerFrame, text = '0:0')
timer.pack(side = LEFT)

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

# Affichage d'un bouton par valeur, en fonction de la taille de la grille
for i in range(1, tailleGrille + 1):
  Button(inputFrame, command = partial(modeChecker, i), text = i, padx = 5, pady = 5).pack(side = LEFT) 

# Bouton de changement de mode (indice ou pas)
boutonModeIndice = Checkbutton(indiceFrame, text = 'Mode indice', command = switchMode)
boutonModeIndice.pack()

# Bouton de pause du temps
boutonPause = Checkbutton(indiceFrame, text = 'Pause', command = switchPause)
boutonPause.pack(side = LEFT)

# Affichage de la grille
chargementGrilleAleatoire()
updateTimer()

# Affichage de la fenêtre principale,
# et intrinsèquement des éléments graphiques la composant
mainWindow.mainloop()
