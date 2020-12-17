def minmax(liste):
  min = liste[0]
  max = liste[0]
  for valeur in liste:
    if valeur < min:
      min = valeur
    if valeur > max:
      max = valeur
  return min, max

print (minmax([2, 5, 1, 7, 6]))