from Personne import *

moi = Personne('Nandillon', 'Séverin', 2000)
moi.afficher()

## attribut 'privé' avec les __
## print(moi.__nom)

print(moi.getNom())
moi.setNom("Nandille")
print(moi.getNom())

moi.afficher()