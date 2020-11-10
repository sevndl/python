def compteMots(phrase):
  listeMots = phrase.split();
  cpt = 0;

  for i in listeMots:
    cpt += 1;
    
  print(cpt);

def listeMots(phrase):
  listMots = phrase.split();
  print(listMots);

compteMots("salut les amis 34");
listeMots("salut les amis 34");