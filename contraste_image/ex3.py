def nbL(m):
  return len(m)

def nbC(m):
  return len(m[0])

def calculer_contraste(m, luminosite):
  mContraste = []
  for i in range(0, nbL(m)):
    mContraste.append([])
  for x in range(0, nbL(m)):
    for y in range(0, nbC(m)):
      if m[x][y] < luminosite:
        mContraste[x].append(m[x][y] // 2)
        # m[x][y] //= 2
      else:
        mContraste[x].append(m[x][y] * 2)
        # m[x][y] *= 2
        if mContraste[x][y] > 100:
          mContraste[x][y] = 100
  print("Matrice initiale :")
  for ligne in m:
    print(ligne)
  print()
  print("Matrice contraste :")
  for ligne in mContraste:
    print(ligne)

print(calculer_contraste([[0,0,100,50], [0,0,100,100], [20,35,50,75]], 44))