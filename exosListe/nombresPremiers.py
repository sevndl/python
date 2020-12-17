def nombresPremiers(taille):
  nbPremiersBool = [True] * (taille)
  nbPremiers = []
  for nb in range(2, taille):
    if (nbPremiersBool[nb] == True):
      for n in range(2 * nb, taille, nb):
        nbPremiersBool[n] = False
  for index in range(2, len(nbPremiersBool)):
    if nbPremiersBool[index]:
      nbPremiers.append(index)
  return nbPremiers

print(nombresPremiers(1000))