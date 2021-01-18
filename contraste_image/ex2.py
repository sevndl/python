def nbLignes(m):
  return len(m)

def nbColonnes(m):
  return len(m[0])

def calculer_luminosite(m):
  print("La matrice à traiter est : ", m)
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

print("La luminosité de la matrice est : ", calculer_luminosite([[0,0,100,50], [0,0,100,100], [20,35,50,75]]))