def minmax(liste):
  minimum = liste[0]
  maximum = liste[0]
  for valeur in liste:
    if valeur < minimum:
      minimum = valeur
    if valeur > maximum:
      maximum = valeur
  return minimum, maximum

print (minmax([2, 5, 1, 7, 6]))