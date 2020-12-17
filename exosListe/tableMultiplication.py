def tableMultiplication(nombre):
  table = []
  for i in range(1, 10 + 1):
    table.append(i * nombre)
  return table

print(tableMultiplication(5))