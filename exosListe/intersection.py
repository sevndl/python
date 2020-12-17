def intersection(liste1, liste2):
  listeCommune = []
  for nbListe1 in liste1:
    for nbListe2 in liste2:
      if nbListe1 == nbListe2:
        listeCommune.append(nbListe1)
  return listeCommune

print(intersection([1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7]))
