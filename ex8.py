def compteMots(phrase):
  listeMots = phrase.split();
  cpt = 0;

  for i in listeMots:
    cpt += 1;
    
  return cpt;

def listeMots(phrase):
  listMots = phrase.split();
  return listMots;

print(compteMots("salut les amis 34"));
print(listeMots("salut les amis 34"));