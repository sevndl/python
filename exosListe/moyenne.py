def moyenne(liste):
  somme = 0
  for valeur in liste:
    somme += valeur
  return somme / len(liste)


print(moyenne([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))