def union(liste1, liste2):
  listeUnion = []
  for nbListe1 in liste1:
    listeUnion.append(nbListe1)
  for nbListe2 in liste2:
    doublon = False
    for nbListeUnion in listeUnion:
      if nbListeUnion == nbListe2:
        doublon = True
        break
    if doublon == False:
      listeUnion.append(nbListe2)
  return listeUnion

print(union([3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7]))