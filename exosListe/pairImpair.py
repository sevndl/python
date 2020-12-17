def pairImpair(liste):
  pair = []
  impair = []
  for nombre in liste:
    if nombre % 2 == 0:
      pair.append(nombre)
    else:
      impair.append(nombre)
  return pair, impair

print(pairImpair([1, 2, 3, 4, 5, 6]))