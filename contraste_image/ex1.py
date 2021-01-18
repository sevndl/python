def nbLignes(M):
  return len(M)

def nbColonnes(M):
  return len(M[0])

def ecrire_matrice(m):
  print("La matrice à traiter est : ", m)
  for x in range(0,nbLignes(m)):
    print('[', end = '')
    for y in range(0,nbColonnes(m)):
      print(m[x][y], end = '')
      if y == nbColonnes(m) - 1:
        print(']')
      else:
        print(',', end = '')

print(ecrire_matrice([[1,2,3], [4,5,6], [7,8,9]]))

# def initialiserMatrice(lignes, colonnes=0, valeur=0):
#   if colonnes==0:
#     # on a affaire à une matrice carrée lignes x lignes
#     colonnes=lignes
#   matrice= []
#   for iLig in range(0,lignes):
#     # ajouter (append) dans matrice une ligne avec colonnes valeurs
#     uneLigne=[]
#   for iCol in range(0,colonnes):
#     uneLigne.append(valeur)
#   matrice.append(uneLigne)

#   return matrice