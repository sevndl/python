def compteMots(phrase):
  listeMots = phrase.split();
  cpt = 0;

  for i in listeMots:
    cpt += 1;
    
  print(cpt);

compteMots("salut les amis");