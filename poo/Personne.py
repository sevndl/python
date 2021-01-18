## fichier de classe

class Personne:
  ## en python, on ne définit pas les attributs
  ## en python, dans une classe, toutes les méthodes DOIVENT avoir un paramètre self,
  ## faisant référence à l'objet courant

  ## si on déclare une variable en dehors des méthodes, cette variable sera static
  ## elle ne sera pas accessible depuis les objets mais depuis la classe directement
  ## ex: Personne.variable

  ## si on commence le nom d'une variable avec __ devant, elle devient 'privée'
  ## python renomme la variable en fait du coup la variable n'existe plus sous ce nom
  ## python la renomme en _Personne__nom, autrement dit _Classe__nom
  ## on peut donc créer un nouvel attribut qui s'appelle comme la variable initiale
  ## donc confusion

  def __init__(self, nom0, prenom0, anneeNaissance0):
    self.__nom = nom0
    self.prenom = prenom0
    self.anneeNaissance = anneeNaissance0

  def getNom(self):
    return self.__nom

  def setNom(self, nouveauNom):
    self.__nom = nouveauNom

  def afficher(self):
    print('Nom :', self.__nom)
    print('Prénom :', self.prenom)
    print('Année de naissance :', self.anneeNaissance)
