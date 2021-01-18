def nbLignes(m):
  return len(m)

def nbColonnes(m):
  return len(m[0])

def calculer_luminosite(m):
  print("La matrice à traiter est : ", m)
  sum = 0
  for x in m:
    for y in x:
      sum += y
  return sum / (nbLignes(m) * nbColonnes(m))

print("La luminosité de la matrice est : ", calculer_luminosite([[1,2,3], [4,5,6], [7,8,9]]))