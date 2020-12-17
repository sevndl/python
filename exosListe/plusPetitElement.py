def plusPetitElement(liste):
  nb = liste[0]
  for valeur in liste:
    if valeur < nb:
      nb = valeur
  return nb

print (plusPetitElement([2, 5, 1, 7, 6]))