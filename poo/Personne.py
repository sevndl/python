## fichier de classe

class Personne:
  ## en python, on ne définit pas les attributs
  ## en python, dans une classe, toutes les méthodes DOIVENT avoir un paramètre self,
  ## faisant référence à l'objet courant

  def __init__(self, nom0, prenom0, anneeNaissance0):
    self.nom = nom0
    self.prenom = prenom0
    self.anneeNaissance = anneeNaissance0

  def afficher(self):
    print('Nom :', self.nom)
    print('Prénom :', self.prenom)
    print('Année de naissance :', self.anneeNaissance)
