# l: inicio del espacio de búsqueda
# h: fin del espacio de búsqueda
# Requiere que la propiedad sea "monótona": es falsa hasta cierto punto. Después de ese punto y en adelante es siempre verdadera.
# Busca el primer valor entre l y h que hace a la propiedad verdadera.

P = [11, 9, 1, 8, 2, 7, 3, 6, 4, 5]
T = [1, 3, 5, 7, 9, 11]
O = []
for p in P:
    l = 0
    h = len(T) - 1
    m = 0
    while (l < h):
      m = l + (h - l)//2
      if p <= T[m]:
        h = m;
      else:
        l = m + 1;
    if p == T[l]: 
        O.append(T[l])
        
print(O)