def compterE(phrase):
  cpt = 0;

  for i in phrase:
    if i == 'e':
      cpt += 1;
  return cpt;

print(compterE("salut les potes"));