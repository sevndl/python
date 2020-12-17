def supprimerDoublons(liste):
  nouvelleListe = []
  for nbListe in liste:
    doublon = False
    for nbNouvelleListe in nouvelleListe:
      if nbListe == nbNouvelleListe:
        doublon = True
        break
    if doublon == False:
      nouvelleListe.append(nbListe)
  return nouvelleListe

print(supprimerDoublons([1, 2, 3, 3, 4, 5, 5, 5, 6, 5]))