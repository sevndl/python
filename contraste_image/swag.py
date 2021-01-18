def nbLignes(m):
  return len(m)

def nbColonnes(m):
  return len(m[0])

def ecrire_matrice(m):
  for x in range(0,nbLignes(m)):
    print('[', end = '')
    for y in range(0,nbColonnes(m)):
      print(m[x][y], end = '')
      if y == nbColonnes(m) - 1:
        print(']')
      else:
        print(', ', end = '')

def initialiserMatrice(lignes, colonnes, valeur):
  if colonnes==0:
    # on a affaire à une matrice carrée lignes x lignes
    colonnes=lignes
  matrice= []
  for iLig in range(0,lignes):
    # ajouter (append) dans matrice une ligne avec colonnes valeurs
    uneLigne=[]
  for iCol in range(0,colonnes):
    uneLigne.append(valeur)
  matrice.append(uneLigne)
  return matrice

def calculer_luminosite(m):
  sum = 0
  for x in range(0, nbLignes(m)):
    for y in range(0, nbColonnes(m)):
      sum += m[x][y]
  return sum // (nbLignes(m) * nbColonnes(m))

# def calculer_luminosite(m):
#   print("La matrice à traiter est : ", m)
#   sum = 0
#   for x in m:
#     for y in x:
#       sum += y
#   return sum // (nbLignes(m) * nbColonnes(m))

def calculer_contraste(m, luminosite):
  mContraste = []
  for i in range(0, nbLignes(m)):
    mContraste.append([])
  for x in range(0, nbLignes(m)):
    for y in range(0, nbColonnes(m)):
      if m[x][y] < luminosite:
        mContraste[x].append(m[x][y] // 2)
        # m[x][y] //= 2
      else:
        mContraste[x].append(m[x][y] * 2)
        # m[x][y] *= 2
        if mContraste[x][y] > 100:
          mContraste[x][y] = 100
  print("Matrice initiale :")
  for ligne in m:
    print(ligne)
  print()
  print("Matrice contraste :")
  for ligne in mContraste:
    print(ligne)

### main ###

matrice = [[0,0,100,50], [0,0,100,100], [20,35,50,75]]
luminosite = calculer_luminosite(matrice)

print(ecrire_matrice(matrice))
print("La luminosité de la matrice est : ", luminosite)
print(calculer_contraste(matrice, luminosite))