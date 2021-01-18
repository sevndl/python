def calculer_contraste(m, luminosite):
  for x in range(0, len(m)):
    for y in range(0, len(m[0])):
      if m[x][y] < luminosite:
        m[x][y] //= 2
      else:
        m[x][y] *= 2
        if m[x][y] > 100:
          m[x][y] = 100
  for ligne in m:
    print(ligne)

print(calculer_contraste([[0,0,100,50], [0,0,100,100], [20,35,50,75]], 44))