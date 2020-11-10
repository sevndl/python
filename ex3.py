def contientE(phrase):
  i = 0;
  for i in phrase:
    if i == 'e':
      print("La phrase contient au moins un 'e'");
      return 1;
  print("pas de 'e'");
  return 0;

contientE("salut");